# from HW_review import odd_to_five
#
# print(odd_to_five)
from pprint import pprint

from __init__ import CONST_STR as str_const
# написать верный пример про управление импортами



# import random
#
#
# import os
#
# import sys
#
# from datetime import datetime, timedelta
#
# now = datetime.now()
#
# print(now.time())
# print(now.date())
# print(now.strftime('%Y-%m-%d'))
# print(now.isoformat())
# print(datetime.strptime('23-03-2021', '%d-%m-%Y'))
# print(datetime.strptime('23-03-2021', '%d-%m-%Y') + timedelta(hours=2, minutes=10))
# print(type(datetime.strptime('23-03-2021', '%d-%m-%Y')))


# стронние модули и как с ними быть
#
# import requests
#
# response = requests.get('http://www.mocky.io/v2/5e56aa7030000046d228e971')
# pprint(response.json(), indent=4)


# files read

# file = open('hello.txt')
# data = file.read()
# print(data)
# file.close()


# files write


# file = open('hello2.txt', mode='w')
#
# file.write('Привет)))')
# file.close()


with open('hello.txt') as file:
    data = file.read()
    print(data)
