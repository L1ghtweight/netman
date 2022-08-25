#!/bin/python

import os
import threading
import json
import smtplib
import ssl
import tabulate
from getpass import getpass
from prettytable import PrettyTable
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

import send_mail
import secrets

us = []
notus = []

tabular_fields = ["Username", "Usage"]
tabular_table = PrettyTable()
tabular_table.field_names = tabular_fields 


def introMessage():

    print()

    print('███╗░░██╗███████╗████████╗███╗░░░███╗░█████╗░███╗░░██╗')
    print('████╗░██║██╔════╝╚══██╔══╝████╗░████║██╔══██╗████╗░██║')
    print('██╔██╗██║█████╗░░░░░██║░░░██╔████╔██║███████║██╔██╗██║')
    print('██║╚████║██╔══╝░░░░░██║░░░██║╚██╔╝██║██╔══██║██║╚████║')
    print('██║░╚███║███████╗░░░██║░░░██║░╚═╝░██║██║░░██║██║░╚███║')
    print('╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝')

    print()


def getMinutes(driver, username, pwd):

    # default value, necessary to avoid unbounded variable issue
    minutes = "000000"
    try:
        driver.find_element(By.XPATH, ("/html/body/div/div/form/div[1]/div/input")).send_keys(username)
        # print("Inserted username..")
        driver.find_element(By.XPATH, ("/html/body/div/div/form/div[2]/div/input")).send_keys(pwd)
        # print("Inserted password..")

        driver.find_element(By.XPATH, ("/html/body/div/div/form/button")).click()

        minutes = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[3]/div/div[1]/table/tbody/tr[6]/td[2]").text

        # print("Total usage for " + username + ": " + minutes + "\n")
        driver.find_element(By.XPATH, ("/html/body/div[1]/div[2]/ul/li[4]/a/span")).click()
    except Exception as exception:
        print(exception)

    return int(minutes[:-6].strip(' '))


def main(driver):
    with open("credentials.json", "r") as credentials:
        data = json.load(credentials)

        table = []

        for user in data:

            username, pwd = data[user]['username'], data[user]['password']
            email = data[user]['email']
            usage = getMinutes(driver, username, pwd)

            if data[user]['us'] == True:
                tabular_table.add_row([username, usage])
                us.append([username, email, usage])
            else:
                notus.append([username, email, usage])

            entry = [username, usage]
            table.append(entry)

    return table

if __name__ == "__main__":

    options = Options()
    options.headless = True
    s = Service()

    # introMessage()
    
    driver = webdriver.Chrome(service = s, options = options)

    print("Getting to iusers page..")
    driver.get("http://10.220.20.12/index.php/home/login")

    print("Getting usage...")
    table = main(driver)
    driver.quit()

    # List of table formats
    # "plain" , "simple" , "github" , "grid" , "fancy_grid" , "pipe" , "orgtbl" , "jira"
    # "presto" , "pretty" , "psql" , "rst" , "mediawiki" , "moinmoin" , "youtrack" , "html"
    # "unsafehtml" , "latex" , "latex_raw" , "latex_booktabs" , "latex_longtable" , "textile" , "tsv"
    print(tabulate.tabulate(table, headers=tabular_fields, tablefmt="pretty"))

    html_table = "<p>Usage of all people in 'us' list:<p>"

    html_table += tabular_table.get_html_string(attributes={
        "border": "1",
        "style": """border-collapse: collapse;
        margin: 25px 0;
        font-size: 0.9em;
        font-family: sans-serif;
        min-width: 400px;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);"""
    })

    # Send mail to 'us' group
    for person in us:
        threading.Thread(target=send_mail.sendMail, args=(person[1], person[0], person[2], html_table)).start()

    # Send mail to 'not us' group
    for person in notus:
        send_mail.sendMail(person[1],person[0],person[2])
