"""
1.Реализовать класс фигуры. На основе фигуры реализовать класс треугольника, квадрата и прямоугольника с
методами подсчета площади и периметра. Методы должны возвращать (return) значение, а не принтить (это важно)
"""
import uuid


class Figure:

    def cal_perimetr(self):
        raise NotImplementedError

    def cal_square(self):
        raise NotImplementedError


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        assert isinstance(side_a, int), 'Переменная должна быть типа int'
        assert isinstance(side_b, int), 'Переменная должна быть типа int'
        assert isinstance(side_c, int), 'Переменная должна быть типа int'
        self._validate_trinangle(side_a, side_b, side_c)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def _validate_trinangle(self, side_a, side_b, side_c):
        # add some validation
        # raise some error if not valid
        pass

    def cal_perimetr(self):
        return self.side_a + self.side_b + self.side_c

    def cal_square(self):
        per = self.cal_perimetr() / 2
        return (per * (per - self.side_a) * (per - self.side_b) * (per - self.side_c)) ** 0.5


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        assert isinstance(side_a, int), 'Переменная должна быть типа int'
        assert isinstance(side_b, int), 'Переменная должна быть типа int'
        self._validate_rectangle(side_a, side_b)
        self.side_a = side_a
        self.side_b = side_b

    def _validate_rectangle(self, side_a, side_b):
        # add some validation
        # raise some error if not valid
        pass

    def cal_perimetr(self):
        return (self.side_a + self.side_b) * 2

    def cal_square(self):
        return self.side_a * self.side_b


class Square(Figure):
    def __init__(self, side_a):
        assert isinstance(side_a, int), 'Переменная должна быть типа int'
        self.side_a = side_a

    def cal_square(self):
        return self.side_a ** 2

    def cal_perimetr(self):
        return self.side_a * 4


"""
2.Реализовать класс Person, у которого должно быть два атрибута: age и name. 

Также у него должен быть следующий набор методов:

    1.def know(self, another_person_object)
    который позволяет добавить другого человека в список знакомых (лист __friends (обязательно приватный атрибут)).

    2.def is_known(self, another_person_object)
    который возвращает знакомы ли два человека (True/False)

"""


class Person:
    def __init__(self, age, name, _id):
        self.name = name
        self.age = age
        self._id = _id
        self.__friends = {}

    def know(self, other):
        self.__friends.setdefault(other._id, other)

    def is_known(self, other):
        return other._id in self.__friends

    @property
    def friends(self):
        return list(self.__friends.values())


person1 = Person(18, 'Oleg', _id=uuid.uuid4())
person2 = Person(20, 'Ivan', _id=uuid.uuid4())
person3 = Person(20, 'Ivan', _id=uuid.uuid4())

print(person1.is_known(person2))

person1.know(person2)
person1.know(person2)
person1.know(person2)
person1.know(person2)
person1.know(person2)
person1.know(person3)
print(person1.is_known(person2))
print(person1.friends)
