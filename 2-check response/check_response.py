#!/usr/bin/python3
from asyncore import write
from datetime import date, datetime
from time import time
import requests
import datetime
import json


current_date = str(datetime.datetime.now())

url = 'https://t72.ru'

response = requests.get(url, timeout=5).status_code

dictionary = {
    "checkTime": current_date,
    "responseCode": response
}

if response == 200:

    with open("good.json", "a") as f:
        json.dump(dictionary, f)

else:
    with open("bad.json", "a") as f:
        json.dump(dictionary, f)