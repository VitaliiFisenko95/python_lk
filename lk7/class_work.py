# ______ Рекурсия ____

"""
Факториал
"""
import random
from datetime import datetime


def factorial(number):
    if number in {0, 1}:
        return 1
    print(f'Recursion  {number}')
    return number * factorial(number - 1)


# factorial(1000)

"""
Числа Фиббоначи

Числа Фибоначчи – это ряд чисел, в котором каждое следующее число равно сумме двух предыдущих.

1, 1, 2, 3, 5, 8, 13, ...
"""


def fibon(pos):
    if pos in {1, 2}:
        return 1
    return fibon(pos - 1) + fibon(pos - 2)


assert fibon(7) == 13
assert fibon(8) == 21

# fibon(70)


"""
Программа должна запрашивать у пользователя сумму в гривнах (uah), и тип валюты (usd/euro) для обмена.
Если валюта не из списка, печатаем ошибку.
Если все ок, печатаем сумму в запрашиваемой валюте по курсу.
"""

CURRENCY_MAP = {
    'uah': 1,
    'usd': 28,
    'euro': 33,
}


def converter(uah, type_):
    if type_ not in CURRENCY_MAP.keys():
        print(f'Invalid currency {type_}')
        return
    return uah / CURRENCY_MAP[type_]


# print(converter(30, 'euro'))
# print(converter(100, 'usd'))


"""
Написать функцию, которая принимает 1 параметр (строка) — день-месяц-год час:минуты:секунды ("10-10-2019 00:24:12").
Вернуть True, если время и дата валидные, иначе False.
Валидная дата - это дата, которая реально может быть.
"""


def validate_date(date):
    try:
        datetime.strptime(date, '%d-%m-%Y %H:%M:%S')
        return True
    except Exception:
        return False


# print(validate_date("10-10-2019 00:24:12"))

"""
Написать функцию, которая на вход принимает число и возвращает сумму всех его цифр. Операцию повторять до тех пор, 
пока не останется одна цифра.
Например:
дано: 5349
5 + 3 + 4 + 9 = 21 2 + 1= 3
вывод: 3
"""


# def sum_of_digits(number):
#     res = number
#     while len(str(number)) > 1:
#         res = 0
#         for i in str(number):
#             res += int(i)
#         number = str(res)
#     return res


# print(sum_of_digits(5349))

# НУжен другой вариант !!!!!!


# Вроде лучше малость)))

def sum_of_digits(num):
    while len(str(num)) != 1:
        num = str(num)
        num = int(num[:-1]) + int(num[-1])
    return num

print(sum_of_digits('5349'))


"""
Угадай число
"""


def validate_user_input():
    user_value = input('Input your value')
    if not user_value.isdigit():
        raise ValueError(f'Invalid value {user_value}')
    return int(user_value)


def guess_number():
    program_number = random.randint(1, 100)
    counter = 1
    while counter < 4:
        print(program_number)
        print('program_number')
        user_int = validate_user_input()
        if user_int > program_number:
            print('Меньше')
        elif user_int < program_number:
            print('Больше')
        elif user_int == program_number:
            print(f'Молодец !!! Угадал за {counter} попытки')
            return
        counter += 1


# guess_number()


"""
Написать игру. 2 игрока бросают игровые кубики по 10 раз,
нужно определить кто выиграл и вывести результаты обоих игроков (суммы бросков).
Если у двух игроков за 1 ход выпало на кубиках одинаковое число, то игроки перебрасывают кубики.
"""


def first_player():
    input('Игрок 1, ваш ход')
    return random.randint(1, 6)


def second_player():
    input('Игрок 2, ваш ход')
    return random.randint(1, 6)


def main():
    start = input('Start game yes|no')
    player_1_sum = 0
    player_2_sum = 0
    if start == 'yes':
        counter = 10
        while counter:
            player_1_value = first_player()
            player_2_value = second_player()
            if player_1_value == player_2_value:
                continue
            player_1_sum += player_1_value
            player_2_sum += player_2_value

            print(player_1_value)
            print(player_2_value)

            counter -= 1

        if player_1_sum > player_2_sum:
            print(' First player win')
            print(player_1_sum)
            print(player_2_sum)
            return

        if player_1_sum == player_2_sum:
            print('Победила дружба')
            print(player_1_sum)
            print(player_2_sum)
            return

        print(' Second player win')
        print(player_1_sum)
        print(player_2_sum)

# main()
