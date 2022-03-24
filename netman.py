#!/bin/python

import time
import json
import smtplib
import ssl
from getpass import getpass
from prettytable import PrettyTable
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


import mail
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


        for user in data:

            username, pwd = data[user]['username'], data[user]['password']
            email = data[user]['email']
            usage = getMinutes(driver, username, pwd)



            if data[user]['us'] == True:
                tabular_table.add_row([username, usage])
                us.append([username, email, usage])
            else:
                notus.append([username, email, usage])



            print(f"Usage of {username}: {usage}")


if __name__ == "__main__":

    options = Options()
    options.headless = True
    s = Service()

    introMessage()

    
    """ Starting chromedriver """
    driver = webdriver.Chrome(service = s, options = options)
    print("Driver initiated..")
    """ Driver started """

    print("Getting to iusers page..")
    driver.get("http://10.220.20.12/index.php/home/login")
    print("Done!\n\n")


    main(driver)

    html_table = "<p>Usage of all people in 'us' list:<p>" + tabular_table.get_html_string()

    # Send mail to 'us' group
    for person in us:
        send_mail.sendMail(person[1], person[0], person[2], html_table)


    # Send mail to 'not us' group
    for person in notus:
        send_mail.sendMail(person[1],person[0],person[2])
    

    driver.quit()
    print("\n\nDriver quitted.")

