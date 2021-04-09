#  Декораторы
import datetime
import time


def time_log(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(start)
        res = func(*args, **kwargs)
        stop = time.time()
        print(res)
        print(stop - start)
        return res

    return wrapper


@time_log
def some_func():
    val = input('Input some value')
    return val


# time_log(some_func)()
"""
Написать декоратор, который позволит обрабатывать ошибки
"""


def expects(error):
    def handler(func):
        def wrapper(*args, **kwargs):
            try:
                print('2')
                return func(*args, **kwargs)
            except error:
                print('Error')

        return wrapper

    return handler


@expects(ValueError)
def raise_error():
    raise ValueError


# raise_error()

"""
Написать декоратор, который позволит логировать (писать в файл) имя функции, параметры, время вызова, время выполнения
"""


def log(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(1)
        res = func(*args, **kwargs)
        run_time = time.time() - start
        with open('log.txt', 'a') as file:
            file.write(f'{func.__name__} {args, kwargs} {datetime.datetime.now()} {run_time}')
            file.write('\n')
        return res

    return wrapper


@log
@expects(ValueError)
def some_func_2():
    val = input('Input some value')
    return val


# print(some_func_2())

# ______ ЗАДАЧИ _______
"""
Проверить введенное слово полиндром или нет
"""


def polyndrom_check(word):
    return word == word[::-1]


# print(polyndrom_check('поп'))

"""
Написать аналог with open() с помощью context lib
"""
import contextlib


@contextlib.contextmanager
def custom_open(path):
    file = None
    try:
        file = open(path)
        yield file
    finally:
        if file:
            file.close()


# with custom_open('log.txt') as file:
#     print(file.read())

# Задачи с собесов))

"""
Что будет если выполнить код ?
"""

a = [[1]] * 3
b = [[], [4], []]
a[1].append(42)
b[1].append(42)
# print(a)
# print(b)

"""
Что произойдет в этих двух фрагментах и почему?
"""

a = [1, 2, 3, 4, 5]
for x in a:
    del x
# print(a)
import re

"""
Подсчитать количество слов test в строке.

Текс - This is a simple test message for test
"""

print(len(re.findall('test', 'This is a simple test message for test')))
"""
Дано текст: ruby python 456 java 789 j2not clash2win
Задача: Найти все упоминания языков программирования в строке.
"""
pattern = 'ruby|python|java'
print(re.findall(pattern, 'ruby python 456 java 789 j2not clash2win'))

"""
Если будет времячко, то найти подвохи тут))
"""

# import os
# def read_file_id(mode, names=[]):
#     _ = ''
#     id = -1
#     for n in names:
#         with open(n, 'w') as f:
#             _ += f.read()
#         f.close() не нужно
#     print('default: ' + str(id) + ', actual: ' + _)
#     return id if _ else id +
