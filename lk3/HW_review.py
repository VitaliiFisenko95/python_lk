"""
1. Разминочная задача на ввод/вывод.
    Написать программу, которая запросит у
    пользователя что-то, а потом выведет
    результат в консоль.
"""
import sys

value = input()
print(f'Hello, {value}')
"""
2. Валидатор паролей. На занятии делали валидацию емейла, тут 
    нужно сделать валидацию пароля по такому же принципу.
    Придумать критаерии надежного пароля, описать их в условиях.
"""
password: str = input('Enter password: ')

if len(password) < 8 or len(password) > 128:
    print('Password is too short or long')
elif password.isalpha():
    print('Password should contains digits')
elif password.isdigit():
    print('Password should contains letters')
elif password.islower():
    print('Password should contains uppercase letters')
elif password.isupper():
    print('Password should contains lowercase letters')
else:
    print(f'Password is OK {password}')

"""
3. Дописать калькулятор, добавив операции умножения, деления, целочисленного деления и возведения в квадрат. 
    Обязательно программа должна обрабатывать тонкие места и не падать
"""


first_value: str = input('Input first value: ')
operation: str = input('Input math operation: ')
second_value: str = input('Input second value: ')

for value in {first_value, second_value}:
    if not value.isdigit():
        print(f'Value of type {type(value)} {value} is not a digit')
        sys.exit(0)
    first_value: int = int(first_value)
    second_value: int = int(second_value)

if operation == '+':
    print(first_value + second_value)
elif operation == '-':
    print(first_value - second_value)
elif operation == '/' and second_value:
    print(first_value / second_value)
elif operation == '//' and second_value:
    print(first_value // second_value)
elif operation == '**':
    print(first_value ** first_value)
else:
    print(f'Invalid operation {operation}')
