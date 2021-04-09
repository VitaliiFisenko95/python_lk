"""
1. У вас есть массив чисел, составьте из них максимальное число. Например:
 [61, 228, 9] -> 961228
"""
import json
from datetime import datetime
from functools import reduce
import random

arr = [61, 228, 9]
max_int = reduce(lambda x, y: x + y, map(str, sorted(arr, key=str, reverse=True)))


# print(max_int)


# Этот вариант с собеседования в MYUALLC

def get_max_num(array):
    int_list = []
    arr = ''.join(map(str, array))
    for i in arr:
        int_list.append(i)
    int_list = sorted(list(map(int, int_list)), reverse=True)

    return int(''.join(map(str, int_list)))


# print(get_max_num([61, 228, 9]))

"""
3. Реализовать функцию, которая принимает строку и расделитель и возвращает словарь {слово: количество повторений} 
(частотный словарь)
"""


def converter(string, delimiter):
    res = {}
    words_list = string.split(delimiter)
    for i in set(words_list):
        res.setdefault(i, words_list.count(i))
        # res.update({i: words_list.count(i)})
    return res


string = """a a a b b c a"""

print(converter(string, ' '))

"""
2. Взять код, который писали для игры кубики на лекции 7 https://github.com/VitaliiFisenko95/python_lk/blob/master/lk7/class_work.py#L150 ,
проанализировать его (по возможности улучшить). Результат игры в кубики нужно записать в файл (json, yaml, csv, xlsx) по раундам. 
В данных раунда должно быть:
 - время хода каждого из игроков
 - количество очков за раунд
 - номер игрока (или имя)
"""


def first_player():
    input('Игрок 1, ваш ход')
    return random.randint(1, 6), datetime.now().strftime('%H:%M:%s')


def second_player():
    input('Игрок 2, ваш ход')
    return random.randint(1, 6), datetime.now().strftime('%H:%M:%s')


def main():
    start = input('Start game yes|no')
    player_1_sum = 0
    player_2_sum = 0
    if start == 'yes':
        data = {}
        counter = 10
        while counter:
            player_1_value, time_1 = first_player()
            player_2_value, time_2 = second_player()
            if player_1_value == player_2_value:
                continue
            player_1_sum += player_1_value
            player_2_sum += player_2_value

            print(player_1_value)
            print(player_2_value)

            counter -= 1
            data[f'Round_{10 - counter}'] = {
                'player_1': {
                    'name': 'player_1',
                    'round_sum': player_1_value,
                    'time': time_1
                },
                'player_2': {
                    'name': 'player_2',
                    'round_sum': player_2_value,
                    'time': time_2
                }
            }

        with open('res.json', 'w') as file:
            json.dump(data, file)

        # with open('res.csv', )

        # НАПИСАТЬ В CSV XLSX

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


main()
