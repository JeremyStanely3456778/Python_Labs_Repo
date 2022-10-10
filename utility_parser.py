import urllib
import json
import csv
import argparse
import requests
import validators
import requests
import os
import pandas as pd



#test data URLS 'uuuuuhttps://jsonplaceholder.typicode.com/todos' https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv

#Take url as input
url = str(input('Enter URL here: '))

#check if input follows proper format of http url, then if not restarts program and prompts user again
valid = validators.url(url)
if valid == True:
    response = requests.get(url)
    print("Url is valid....!")
    response_utf_8 = response.content.decode('utf-8')

    #check if contents is in csv or json format write to local directory
    try:
        a_json = json.loads(response_utf_8)
        print('Its in json format....!')
        with open('parse_data.json', 'wb') as file:
            file.write(response.content)
        print('Data saved to json file....!')
    except:
        if ";" in response_utf_8:
            print('Contents of response cannot be converted to csv file....!')
        elif "," in response_utf_8:
            print('Its in csv format....!')
            with open('parse_data.csv', 'wb') as file:
                file.write(response.content)
            print('Data saved to csv file....!')


else:
    print("\nInvalid url Please make sure URL is in correct format......!")
    os.system("python utility_parser.py")

