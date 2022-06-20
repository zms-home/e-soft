#!/usr/bin/python3

#импортируем модули
from asyncore import write
from datetime import date, datetime
from time import time
import requests
import datetime
import json

#Записываем в переменную текущую дату
current_date = str(datetime.datetime.now())

url = 'https://t72.ru'

#Получаем код ответа и записываем его в пременную
response = requests.get(url, timeout=5).status_code

#Создаем словарь и записываем в него дату и код ответа
dictionary = {
    "checkTime": current_date,
    "responseCode": response
}
#В зависимости от кода ответа создаем файл
if response == 200:

    with open("good.json", "a") as f:
        json.dump(dictionary, f)

else:
    with open("bad.json", "a") as f:
        json.dump(dictionary, f)
