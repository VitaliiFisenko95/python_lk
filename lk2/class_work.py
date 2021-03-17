"""
Базовые типы
str
int
float
list
tuple
set
dict
None
bool
"""
import sys

# I/O operations

# value: str = input('Tell me your age: ')

# if value.isdigit():
#     value: int = int(value)
#     print(type(value))
#     sys.exit(0)
# print('Not a digit')


#  __________ONLY IF STATEMENT___________


# value: str = input('Tell me your age: ')
# role: str = input('Tell me your role: ')
#
# if all([value.isdigit(), int(value) < 18, role != 'admin']):
#     print(f'Not allowed!!!! You should be older 18 but you are {value}')
#     sys.exit(0)
# print('You are welcome!')


"""
if пропускает 
все что тру или не пустое
[1,2,4]
'1222'
True

if  НЕ ПРОПУСКАЕТ
False
[]
''
None
"""

# ____IF ELSE STATEMENT _____


# value: str = input('Tell me your age: ')
# role: str = input('Tell me your role: ')
#
# if all([value.isdigit(), int(value) < 18, role != 'admin']):
#     print(f'Not allowed!!!! You should be older 18 but you are {value}')
# else:
#     print('You are welcome!')


# __ IF ELIF ELSE STATEMENT ___


# value: str = input('Tell me your age: ')
# role: str = input('Tell me your role: ')
#
# if all([value.isdigit(), int(value) < 18, role != 'admin']):
#     print(f'Not allowed!!!! You should be older 18 but you are {value}')
# elif value.isdigit() and int(value) >= 18 and role != 'admin':
#     print('You are adult but not admin')
# elif value.isdigit() and int(value) == 19 and role != 'admin':
#     print('You are adult but not admin')
# else:
#     print('You are welcome!')


# ___ WHILE LOOP ___

# stop_value = ''
# while stop_value != 'stop':
#     stop_value = input('Enter thmth to stop')
#     print('loop passed')


# ___ WHILE LOOP WITH STOP ___


# while True:
#     stop_value = input('Enter thmth to stop')
#     if stop_value == 'c':
#         continue
#     elif stop_value == 'stop':
#         break
#     print('loop passed')


# for item in [1, 2, 34, 'kjnsdkc']:
#     if isinstance(item, str):  # тоже самое type(item) == str
#         print(item + 'hello')
#         continue
#     print(item + 1)


"""
ИТЕРАБЕЛЬНЫЕ ОБЪЕКТЫ
str
list
set
tuple
dict
"""

# for item in (1, 2, 34, 'kjnsdkc'):
#     print(item)
#

# for item in {1, 2, 34, 'kjnsdkc'}:
#     print(item)


# for item in 'мама мыла раму':
#     print(item)


# example_dict = {1: 1, 2: 2, 3: 3, 4: 4, 'dict': {2: '2', '1': 1}}
#
# for key, value in example_dict.items():
#     if key == 'dict':
#         value[2] = 3


# for item in range(1, 12, 2):
#     print(item)


# ____________________________

# EMAIL VALIDATOR
#
# email: str = input('Input email')
#
# if '@' not in email:
#     print('Invalid')
#     sys.exit(0)
# elif '.' not in email:
#     print('Invalid')
#     sys.exit(0)
# at_sign_index = email.index('@')
# for sign in {'.', '@'}:
#     if email[at_sign_index + 1] == sign or email[at_sign_index - 1] == sign:
#         print('Invalid')
#         sys.exit(0)
#     elif email[-1] == sign or email[0] == sign:
#         print('Invalid')
#         sys.exit(0)


# CALCULATOR

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
else:
    print(f'Invalid operation {operation}')
