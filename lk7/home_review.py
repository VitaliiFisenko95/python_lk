"""
1. Написать любую детерменированную функцию (Детерменированная функция = функция, которая возвращает одно и тоже вне
зависимости от парамеметров)
"""
import json

"""
2. Написать функцию, которая вернет True если число четное и False если не четное
"""


def is_even(number):
    return not bool(number % 2)


def is_odd(number):
    return bool(number % 2)


"""
3. Напишите функция is_prime, которая принимает 1 аргумент (число) и возвращает True, если число простое, иначе False
Простое число - это число, которое делится без остатка только на себя и на 1
"""


def is_prime(value):
    if value == 1:
        return False
    d = 2
    while d * d <= value and value % d != 0:
        d += 1
    return d * d > value


# print(is_prime(1))
# print(is_prime(2))
# print(is_prime(3))
# print(is_prime(4))
# print(is_prime(5))
# print(is_prime(6))
# print(is_prime(7))
# print(is_prime(8))
# print(is_prime(9))

"""
4. Напишите функцию, которая принимает 1 аргумент (строка) и выполняет следующие действия на каждую из букв строки:
i - инкремент (+1)
d - дикремент (-1)
s - возведение в квадрат
o - добавить число в результативный список
остальные буквы игнорируются
Исходное число = 0
Результативный список = []
Вернуть результативный список
parse("iiisdoso")  ==>  [8, 64] <- это как пример
"""


def parse(operations):
    initial = 0
    res = []
    for op in operations:
        if op == 'i':
            initial += 1
        elif op == 'o':
            res.append(initial)
        elif op == 'd':
            initial -= 1
        elif op == 's':
            initial **= 2
    return res


# assert parse("iiisdoso") == [8, 64]

"""
5. Написать программу, которая откроет файл (questions.json) и после ответов на вопросы, запишет их назад 
в этот же файл.
"""


def answer_questions(file_path):
    with open(file_path) as file:
        data = json.load(file)

    for idx, q in enumerate(data.get('questions', [])):
        data['questions'][idx]['answer'] = input(q['q'])

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


answer_questions('questions.json')
