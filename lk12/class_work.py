import uuid

# Магические
from dataclasses import dataclass


class CustomInt(int):

    def __add__(self, other):
        if isinstance(other, str):
            other = len(other)
        return super().__add__(other)


# new_int = CustomInt(1)
# print(new_int + '3333')


class Person:
    def __init__(self, age, name, _id):
        self.name = name
        self.age = age
        self._id = _id
        self.__friends = {}

    def __str__(self):
        return f'{self.name} {self.age}'

    def __repr__(self):
        return f'{self.name} {self.age} with _id {self._id} of class {self.__class__.__name__} in module {__file__}'

    def know(self, other):
        self.__friends.setdefault(other._id, other)

    def is_known(self, other):
        return other._id in self.__friends

    @property
    def friends(self):
        return list(self.__friends.values())


# person1 = Person(18, 'Oleg', _id=uuid.uuid4())
# person2 = Person(20, 'Ivan', _id=uuid.uuid4())
# person3 = Person(20, 'Ivan', _id=uuid.uuid4())
#
# print(person1.is_known(person2))
#
# person1.know(person2)
# person1.know(person2)
# person1.know(person2)
# person1.know(person2)
# person1.know(person2)
# person1.know(person3)
#
# print(person1)
# print(person1.is_known(person2))
# print(person1.friends)

class ListObjectDict(dict):
    def __iter__(self):
        return self.values().__iter__()

    def __getitem__(self, key):
        if isinstance(key, int):
            return list(self.values())[key]
        return super().__getitem__(key)

    def get(self, key, default=None):
        return super().get(key, default)

    def append(self, obj):
        self[str(id(obj))] = obj


# new_dict = ListObjectDict()
#
# a = 'knmkdnkcdnkc'
# b = 1

# print(new_dict)
# new_dict.append(b)
# new_dict.append(a)
# print(new_dict)
# print(new_dict[str(id(a))])
# print(new_dict[-1])
# print(new_dict[0])
# print(type(new_dict))

from collections import namedtuple

PersonFromTuple = namedtuple('PersonFromTuple', ['age', 'name'])


# print(PersonFromTuple)
# print(type(PersonFromTuple))
# print(dir(PersonFromTuple))
# person = PersonFromTuple(age=19, name='Oleg')
# print(person.age)
# person.age = 56
# del person.age

@dataclass
class Point:
    x: float
    y: float
    z: float

    def sum(self):
        return self.x + self.y + self.z


# p = Point(x=1, y=2.12, z='kdm')
# print(p)
# print(p.sum())
#
# p.z = 11.2
# print(p)

import typing


# val: typing.List[str, typing.Dict] = []


class ImmutablePerson(typing.NamedTuple):
    age: int
    name: str
    inn: typing.Union[str, int, None] = None


person = ImmutablePerson(age=18, name='Oleg', inn='34567898765')


def get_person_info(per: ImmutablePerson) -> str:
    print(per.inn + 'kdkkd')
    print(per.inn)
    return f'{per.age} {per.name} {per.inn} {per.inn}'


print(get_person_info(per=person))
"""
Реализовать класс Банкомат, у которого есть баланс. Банкомат может выдавать деньги и принимать платежи.
Банкомат не может уйти в минус и не может обрабатывать отрицательные сумму.
"""
