from pprint import pprint


def validate_email(email):
    if '@' not in email:
        return f'Invalid @ not find in {email}'
    if '.' not in email:
        return f'Invalid . not find in {email}'
    at_sign_index = email.index('@')
    for sign in {'.', '@'}:
        if email[at_sign_index + 1] == sign or email[at_sign_index - 1] == sign:
            return 'Invalid 1'
        elif email[-1] == sign or email[0] == sign:
            return 'Invalid 2'


# print(validate_email(input('Input email')))

#  Positional args


def process_integers(*args):
    first, second, third = args
    print(args[0])
    print(args[1])
    print(args[2])
    print(first, second, third)


# process_integers(2, 1, 3)


# Key-word arguments

def sum_of_class_age(**kwargs):
    print(type(kwargs))
    print(kwargs)
    # print(kwargs)
    # print(kwargs)


people = {
    'Nick': 5,
    'Kate': 6,
    'Mike': 5,
}


# sum_of_class_age(Nick=5, Kate=6, Mike=5)
# sum_of_class_age(**people)


# LOCAL


def validate_password(password):
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

    return password


# password = validate_password(input('Input password :  '))
#
# print(password)


# GLOBAL
import json

FILE_CONTENT = {}


def read_file(file_path):
    global FILE_CONTENT
    with open(file_path) as file:
        FILE_CONTENT = json.load(file)


# read_file('test.json')


# pprint(FILE_CONTENT, indent=4)

def change_json():
    global FILE_CONTENT
    FILE_CONTENT['widget']['debug'] = 'on'


# change_json()
# pprint(FILE_CONTENT, indent=4)


def save_data(file_path):
    global FILE_CONTENT
    with open(file_path, 'w') as file:
        json.dump(FILE_CONTENT, file, indent=4)


# save_data('test.json')


# determined functions

def some_function():
    return 5


def return_None():
    return None


def main():
    file_path = input('Input file path  ')
    read_file(file_path)
    print('read_file')
    change_json()
    print('change_json')
    save_data(file_path)
    print('save_data')


# if __name__ == '__main__':
#     print(__name__)
#     main()

# print(some_function())

"""
1
Напишите программу, которая заполняет список пятью словами,
введенными с клавиатуры, измеряет длину каждого слова
и добавляет полученное значение в другой список.

Например, список слов – ['yes', 'no', 'maybe', 'ok', 'what'],
список длин – [3, 2, 5, 2, 4].
Оба, списка, должны, выводиться, на, экран.
"""

SEP = ', '


def get_words_len_list(line):
    len_list = []
    words = line.split(SEP)
    for word in words:
        len_list.append(len(word))

    return words, len_list


# if __name__ == '__main__':
#     words, len_list = get_words_len_list(input(f"Input some world separated by {SEP}: "))
#     print(words)
#     print(len_list)

"""
2
Четные числа в начало списка, нечетные - в конец
"""


def sort_digits(digits):
    result = []
    for item in digits:
        if item % 2 == 0:
            result.insert(0, item)
        else:
            result.append(item)

    return result


numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
]


# print(sort_digits(numbers))

def test(number, storage=[]):
    storage.append(number)
    print(storage)


test(5)
test(5)
test(5, [])
test(5)
test(5)
