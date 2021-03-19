'''
Тернарный оператор
'''

# value = input()
# if value == '2':
#     print(value)
# else:
#     print('Not 2')
#


# print(value) if value == '2' else print('No2')


"""
try
except
finaly
else
raise
"""

# some_int = input('Enter some digit: ')
# some_int_second = input('Enter some digit: ')
# try:
#     some_int = int(some_int)
#     some_int_second = int(some_int_second)
#     result = some_int / some_int_second
# except ValueError:
#     print('ERROR')
# except ZeroDivisionError:
#     print('0!!!!')
# else:
#     print('OK')
# finally:
#     print('CLOSE!')


#  через иф , вместо трай

# some_int = input('Enter some digit: ')
# some_int_second = input('Enter some digit: ')
# if some_int.isdigit() and some_int_second.isdigit() and some_int_second != 0:
#     some_int = int(some_int)
#     some_int_second = int(some_int_second)
#     result = some_int / some_int_second
# else:
#     print('ERROR')


# ------________________


# some_int = input('Enter some digit: ')
# some_int_second = input('Enter some digit: ')
# try:
#     some_int = int(some_int)
#     some_int_second = int(some_int_second)
#     result = some_int / some_int_second
# except (ZeroDivisionError, ValueError):
#     print('ERROR')
# else:
#     print('OK')
# finally:
#     print('CLOSE!')


# try:
#     1/0
# except Exception as ex:
#     print('jkdjdjjdjddj')


#  ______________________________________________________

### Anti vitalik


# name = input('Input your name: ')
#
# if name == 'Vitalii':
#     raise NameError(f'Name {name} is not supported')
# print(name)

# print(dir(__builtins__))  для просмотра встроеных ошибок, ключевых слов, функций и тп


# срезы


# my_str = 'mama myla ramu'
#
# print(my_str[::2])
#
# print(my_str.index('m'), 'm_index')
#
# my_list = my_str.split(' ')

# print(my_list[9])

# mama_index = my_list.index('mama')
# ramu_index = my_list.index('ramu')
#
# print(my_list[mama_index: ramu_index])
#
#
# print(mama_index, 'mama_index')
#
# my_set = {1, 2, 3,  65, 4}
# print(list(my_set).sort())


# List comprehension


# new_list = []
#
# for i in [1, 2, 3, 4, 5, 6, 7]:
#     if i > 2:
#         new_list.append(i ** 3)
#
# print(new_list)
#
# new_list = [i**3 for i in [1, 2, 3, 4, 5, 6, 7] if i > 2]
# print(new_list, 'comprehension')


new_dict = {}

for i in [1, 2, 3, 4, 5, 6, 7]:
    if i > 2:
        new_dict[i] = i ** 3

print(new_dict)

new_dict = {i: i ** 3 for i in [1, 2, 3, 4, 5, 6, 7] if i > 2}

print(new_dict, 'comprehension')
