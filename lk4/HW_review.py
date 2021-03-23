"""
1. Реализовать калькулятор, как делали на прошлом дз, но уже с обработкой ошибок (try, except)
"""
# import sys
#
# first_value: str = input('Input first value: ')
# operation: str = input('Input math operation: ')
# second_value: str = input('Input second value ')
#
# try:
#     first_value: int = int(first_value)
#     second_value: int = int(second_value)
# except ValueError as error:
#     print(f'Error {type(error)}')
#     sys.exit(0)
#
# if operation == '+':
#     print(first_value + second_value)
# elif operation == '-':
#     print(first_value - second_value)
# elif operation == '*':
#     print(first_value * second_value)
# elif operation == '/':
#     try:
#         print(first_value / second_value)
#     except ZeroDivisionError:
#         print('ZeroDivisionError')
# elif operation == '//':
#     try:
#         print(first_value // second_value)
#     except ZeroDivisionError:
#         print('ZeroDivisionError')
# else:
#     print(f'Invalid operation {operation}')

"""
2. Нужно сделать что бы код не падал, а был обработан каждый случай в отдельном except.
 На код стоит посмотреть внимательно, может что-то в нем не так)
"""
# import random
#
# try:
#     raise random.choice([ZeroDivisionError, ImportError, KeyError, UnicodeError, StopIteration])
# except ZeroDivisionError:
#     print('ZeroDivisionError')
# except ImportError:
#     print('ImportError')
# except KeyError:
#     print('KeyError')
# except UnicodeError:
#     print('UnicodeError')
# except StopIteration:
#     print('StopIteration')
#
#
# try:
#     raise random.choice([ZeroDivisionError, ImportError, KeyError, UnicodeError, StopIteration])
# except Exception as error:
#     print(type(error))

"""
3. Совместить валидацию email и валидацию пароля и вместо принтов райзить ошибки если пароль или 
email не подходит по критериям (критерии надежности пароля можно брать с прошлого ДЗ или придумать новые). 
Ошибки брать на выбор 
"""

# password: str = input('Enter password: ')
#
# if len(password) < 8 or len(password) > 128:
#     raise ValueError('Password is too short or long')
# elif password.isalpha():
#     raise NameError('Password should contains digits')
# elif password.isdigit():
#     raise NameError('Password should contains letters')
# elif password.islower():
#     raise NameError('Password should contains uppercase letters')
# elif password.isupper():
#     raise NameError('Password should contains lowercase letters')
# else:
#     raise NameError(f'Password is OK {password}')

"""
4. Создать список, где все элементы будут кратные 5ти (упражнение на функцию range)
"""

odd_to_five = []
for item in range(40):
    if item and not item % 5:
        odd_to_five.append(item)

"""
5. Вывести в консоль (функция print) максимальное и минимальное значение из списка в задании 4 и сумму всех елементов 
этого списка
"""

# print(sum(odd_to_five), min(odd_to_five), max(odd_to_five))
