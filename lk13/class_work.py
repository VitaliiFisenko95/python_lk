# + 1 странная штука в python
from random import random, randint, choice
from typing import NamedTuple

_A__a = 4


class A:
    def get_attr(self):
        return __a

    @classmethod
    def get_class_attr(cls):
        return __a


# print(A.get_class_attr())
# a = A()
# print(a.get_attr())
# что же такое type (больше разсмотрим на 14м занятии)

ABC = type('ABC', (), {'a': lambda x: x + 2, 'b': 4, 'c': 3})
# print(ABC.a(5))
# print(ABC.b)
# print(ABC.c)
# print(ABC.mro())


"""
Реализовать класс Банкомат, у которого есть баланс. Банкомат может выдавать деньги и принимать платежи.
Банкомат не может уйти в минус и не может обрабатывать отрицательные сумму.
"""

"""
Создать класс воина, создать 2 или больше объектов воина с соответствующими воину атрибутами. Реализовать методы,
которые позволять добавить силы воину, улучшить оружие. Реализовать возможность драки 2х воинов с потерей здоровья,
приобретения опыта.
"""

"""
Написать свой контекст менеджер, которы будет отлавливать и логировать ошибки
"""


class logger:
    def __init__(self, description: str):
        self.description = description

    def __enter__(self):
        try:
            print(f'{self.description} logger start')
        except ValueError:
            print('ValueError')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            with open('errors.txt', 'w') as file:
                file.write(f'{exc_type.__name__} text1 - {exc_val} place {exc_tb.tb_frame}')


def type_transformation(some_value, type_to_convert):
    with logger(f'Trying to convert {some_value} to {type_to_convert.__name__}'):
        # try:
        res = type_to_convert(some_value)
        # except ValueError:
        #     print('errr')
        # print(res)


# type_transformation('1', int)
# type_transformation('ghjkjh', int)

"""
Реализовать класс Банкомат, у которого есть баланс. Банкомат может выдавать деньги и принимать платежи.
Банкомат не может уйти в минус и не может обрабатывать отрицательные сумму.
"""


class ATM:
    def __init__(self, initial_value: int = None, max_money: int = None,
                 withdraw_limit: int = None):
        # assert max_money is not None
        # assert initial_value is not None
        # assert withdraw_limit is not None
        self.initial_value = initial_value or 0
        self.max_money = max_money or 1_000_000
        self.withdraw_limit = withdraw_limit or 20_000
        self.current_value = initial_value

    def withdraw(self, value):
        if value > self.withdraw_limit:
            raise ValueError('withdraw error')
        prediction = self.current_value - value
        if prediction < 0:
            raise ValueError('withdraw error current_value less than value')
        self.current_value -= value
        return value

    def payment(self, value):
        prediction = self.current_value + value
        if self.max_money < prediction:
            raise ValueError('payment error current_value + value more than max_money')
        self.current_value += value
        return 'ok'


def atm_check():
    mono = ATM(initial_value=10_000, max_money=9_999_999, withdraw_limit=5_000)
    print(mono.withdraw(5000))
    print(mono.current_value)
    print(mono.payment(5000))
    print(mono.current_value)


# atm_check()
"""
Создать класс воина, создать 2 или больше объектов воина с соответствующими воину атрибутами. Реализовать методы,
которые позволять добавить здоровья, улучшить оружие. Реализовать возможность драки 2х воинов с потерей здоровья,
приобретения опыта.
"""


class Weapon(NamedTuple):
    name: str
    power: int


class Warrior:
    def __init__(self, weapon: Weapon, name: str, health: int):
        self.weapon = weapon
        self.name = name
        self.health = health
        self.armor = 0
        self.status = 'alive'

    def add_health(self, value):
        if value < 0:
            print('Слишком мало')
            return
        self.health += value

    def change_weapon(self, weapon):
        self.weapon = weapon

    def add_armor(self, armor):
        if armor < 0:
            print('Слишком мало')
            return
        self.armor += armor

    def heat_other(self, other_warrior):
        if other_warrior.status == 'die':
            print('')
            return
        if other_warrior.armor:
            other_warrior.armor -= self.weapon.power
            # нужно учесть что броня не может уйти в минус
        other_warrior.health -= self.weapon.power
        # нужно учесть что здоровье не может уйти в минус


def random_choose_weapon():
    weapon_list = []
    for i in range(50):
        weapon_list.append(Weapon(
            name=str(i),
            power=randint(1, 101)
        ))
    return choice(weapon_list)


def main_fighting_area():
    warrior1 = Warrior(name='Oleg', health=100, weapon=random_choose_weapon())
