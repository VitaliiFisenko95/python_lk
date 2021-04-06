"""
1
Написать функцию для сортировки для  списка словарей.

Сортировать по ключу `name`, если такого ключа нету в словаре, то по ключу `lastname`
"""

# def sort_by_key(value):
#     return value.get('name') or value.get('lastname')
#
#
# dictionary = {'name': 'Aiuvan', 'lastname': 'Ivanov'}
# dictionaries = [dictionary, {'lastname': 'AAcIvanov'}, {'name': 'Abvan', 'lastname': 'Bvanov'}]
# dictionaries.sort(key=sort_by_key)
# dictionaries.sort(key=lambda a: a.get('name') or a.get('lastname'))
# print(dictionaries)


# Антипаттерн
import time
from random import randint

func = lambda a, b: a + b

# print(func(3, 4))


# def calc(value1, operation, value2):
#     operations = {
#         '+': lambda a, b: a + b,
#         '-': lambda a, b: a - b,
#         '*': lambda a, b: a * b,
#         '/': lambda a, b: a / b,
#     }
#
#     try:
#         return operations[operation](value1, value2)
#     except Exception:
#         print('AAAAAA')


# for i in range(1000000):
#     print(lambda i: i * i)

# MAP

# print(list(map(str, range(11))))
# Алтернативный вариант

# empty_list = []
# for i in range(11):
#     empty_list.append(str(i))
#
#
# print(empty_list)

# print(list(map(lambda a: a * a, range(11))))

# Алтернативный вариант

# print([item * item for item in range(11)])


# REDUCE

from functools import reduce


# print(reduce(lambda x, y: x + y, map(str, [1, 2, 3, 4, 5])))


# FILTER
def filter_func(value):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    if value in vowels:
        return True
    return False


# def filter_func(value):
#     return value in {'a', 'e', 'i', 'o', 'u', 'y'}

vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
# print(list(filter(filter_func, 'kjksjdcsvuasyxikehf')))
# print(list(filter(lambda a: a in vowels, 'kjksjdcsvuasyxikehf')))

# print(filter_func('kjksjdcsvuasyxikehf'.split()))


# SORTED


dictionary = {'name': 'Aiuvan', 'lastname': 'Ivanov'}
initial_dictionaries = [dictionary, {'lastname': 'AAcIvanov'}, {'name': 'Abvan', 'lastname': 'Bvanov'}]
dictionaries = initial_dictionaries
dictionaries.sort(key=lambda a: a.get('name') or a.get('lastname'))
# print(dictionaries)
# print(id(dictionaries))

new_list = sorted(tuple(initial_dictionaries), key=lambda a: a.get('name') or a.get('lastname'))
# print(new_list)
# print(id(new_list))

example_dict = {4: 14, 1: 11, 2: 5, 3: 13}


# print(sorted(example_dict.items(), key=lambda item: example_dict[item[0]]))

# ЗАМЫКАНИЯ

def calc(value1, operation, value2):
    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return None

    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div,
    }

    return operations[operation](value1, value2)


# print(calc(1, '+', 2))


# Регулярки

import re

re_obj = re.search(r'\d', 'kjsndcjnsdkjncns222kk2k2')


# print(re.findall(r'\w', 'kjsndcjnsdk:jncns222kk2k2'))


def gen(iterable):
    for item in iterable:
        print('start')
        yield item
        print('Nex value start processing')
        print(item)


new = gen(range(11))

print(new)

while True:
    time.sleep(0.5)
    try:
        next(new)
    except StopIteration:
        print('Gen is empty')
        break
