"""
1. Создать файл, в нем написать текст.
 - Считать данные с файла и вывести в консоль
 - Считать данные с этого же файла и записать в новый файл
 - Считать данные с этого же файла, преобразовать (любые операции) и записать в этот же файл с разделителем
   (пробел, точка, запятая и тп)
"""

# with open('test.txt') as file:
#     print(file.read())


# with open('test.txt') as file_read, open('new_file.txt', 'w') as file_write:
#     file_write.write(file_read.read())


# with open('test.txt', 'r+') as file:
#     data = file.read()
#     file.write('|'.join(data.split(',')))


# with open('test.txt') as file_read, open('test.txt', 'w') as file_write:
#     file_write.write(file_read.read())
# from datetime import datetime

"""
2. Преобразовать дату. Нужно написать код, который из Feb 12 2019 2:41PM сделает 2019-02-12 14:41:00
"""
# date = 'Feb 12 2019 2:41PM'
#
# converted_date = datetime.strptime(date, '%b %d %Y %I:%M%p')
# print(converted_date.isoformat(sep=' '))
# print(converted_date.strftime('%Y-%m-%d %H:%m:%S'))
#
# print(converted_date.strftime('%b %d %Y %I:%M'))
#
# print()
"""
3. Напишите программу, которая принимает год, и возвращает список дат всех понедельников в данном году.
   Работа с датами (можно использовать любые модули и гуглить)
"""

# import pandas
# import pprint
#
# pprint.pprint(pandas.date_range('2021', end='2022', freq='W-MON').strftime('%Y-%m-%d').tolist(), indent=4)
