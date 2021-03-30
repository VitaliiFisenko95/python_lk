"""
1. Напишите программу, которая принимает имя файла и выводит его расширение.
    Если расширение у файла определить невозможно, выбросите исключение.
"""
# file_name = input('Enter file name')
#
# if '.' not in file_name:
#     raise ValueError('File type does not exist')
# if file_name[-1] == '.':
#     raise ValueError('Cannot end with dot')
# print(file_name.split('.')[-1])


"""
2. Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.
"""

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
]
odd_number = []

# for number in numbers:
#     if number == 237:
#         break
#     if number % 2 == 0:
#         odd_number.append(number)
#
# print(odd_number)

"""
3. Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
"""
# from collections import Counter
# word = input('Input some word')
#
#
# counter = Counter(word.split(' '))
#
# print(counter.most_common(n=2))
#
# longest = None
#
# for i in counter.most_common():
#     if not longest:
#         longest = i[0]
#
#     if len(i[0]) > len(longest):
#         longest = i[0]
# print(longest)
