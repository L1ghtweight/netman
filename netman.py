#!/bin/python

import sys
import threading
import json
import tabulate
from prettytable import PrettyTable

import send_mail
from get_usage import getUsage

us = []
notus = []

tabular_fields = ["Username", "Usage"]
tabular_table = PrettyTable()
tabular_table.field_names = tabular_fields 

def getUsageTable():
    with open("credentials.json", "r") as credentials:
        data = json.load(credentials)

        table = []

        for user in data:

            try:
                username, pwd = data[user]['username'], data[user]['password']
                email = data[user]['email']
                usage = getUsage(username, pwd)
                if data[user]['us'] == True:
                    tabular_table.add_row([username, usage])
                    us.append([username, email, usage])
                else:
                    notus.append([username, email, usage])

                entry = [username, usage]
                table.append(entry)
            except:
                print("Error occured")

    return table

if __name__ == "__main__":
    print("Getting usage...")
    table = getUsageTable()

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

    if "--no-mail" not in sys.argv and "-nm" not in sys.argv:
        # Send mail to 'us' group
        for person in us:
            threading.Thread(target=send_mail.sendMail, args=(person[1], person[0], person[2], html_table)).start()

        # Send mail to 'not us' group
        for person in notus:
            threading.Thread(target=send_mail.sendMail, args=(person[1], person[0], person[2])).start()
    else:
        print("Exiting without sending mails.")
    
