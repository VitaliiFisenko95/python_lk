"""
1. Написать программу, которая будет делать траслитерацию
"""

symbols = (
    "абвгдеёзиійклмнопрстуфхыиэАБВГДЕЁЗИІЙКЛМНОПРСТУФХЫИЭЬЪьъґҐЄє",
    "abvgdeeziijklmnoprstufhyyeABVGDEEZIIJKLMNOPRSTUFHYYE____gGEe",
)
transl_map = {ord(i): ord(j) for i, j in zip(*symbols)}

print('коллетивизацыя'.translate(transl_map))

"""
2. Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


print(list(set(a).intersection(set(b))))
print(list(set(a) & set(b)))
"""
3. Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
"""

"""
4. Нужно проверить, все ли числа в последовательности уникальны.
"""

data_list = [1, 2, 3, 4, 1, 2, 3, 4, 56, 6]

print(len(data_list) == len(set(data_list)))

print(set(data_list))
print(data_list)

"""
5. Поменяйте значения переменных местами.
"""
x = 5
y = 10

y, x = x, y

"""
6. Посчитайте, сколько раз символ встречается в строке.
"""
string = 'Посчитайте, сколько раз символ встречается в строке.'

print(string.count(' '))

"""
7. Сложите цифры целого числа. чило - 892349832
"""

number = 56

number_list = sum([int(i) for i in str(number)])
print(number_list)

"""
8. Выведите список файлов в указанной директории.
"""
import os

print('kjdsjkcnckjsd')
print([file for file in os.listdir('home') if os.path.isdir(os.path.join('home', file))])
"""
9. Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.
"""

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
]

"""
10. Напишите программу, которая принимает имя файла и выводит его расширение. 
    Если расширение у файла определить невозможно, выбросите исключение.
"""
