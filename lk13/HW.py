"""
Создать класс воина, создать 2 или больше объектов воина с соответствующими воину атрибутами. Реализовать методы,
которые позволять добавить здоровья, сменить оружие. Реализовать возможность драки 2х воинов с потерей здоровья,
приобретения опыта.
Следует учесть:
 - у воина может быть броня
 - здоровье не может быть меньше 0
 - броня не может быть меньше 0
 - здоровье не тратится пока броня не 0
Было бы неплохо добавить возможность воину носить несколько видов оружия и при сломаном текущем заменить его (опционально)
"""
from random import randint, choice
from typing import NamedTuple


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