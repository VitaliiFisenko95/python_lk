# Абстракция
import functools
from abc import ABC, abstractmethod


class MyAbstractClass(ABC):

    @abstractmethod
    def some_method(self):
        return None

    @abstractmethod
    def some_second_method(self):
        return int


class SomaAClass(MyAbstractClass):

    def some_method(self):
        return None

    def some_second_method(self):
        return int


# a = SomaAClass()

"""
Написать метакласс, который запретит переопредялть __call__
"""

# class MyMeta(type):
#     def __new__(mcs, class_name, parents, attrs):
#         print(class_name)
#         print(parents)
#         print(attrs)
#         # if '__call__' in attrs:
#         #     raise AttributeError('__call__ is depricated')
#         for p in parents:
#             print(p)
#             print(p.__dict__.keys())
#             for attr in p.__dict__.keys():
#                 if attr == '__call__':
#                     raise AttributeError('__call__ is depricated')
#         return super().__new__(mcs, class_name, parents, attrs)
#
#
# class A(metaclass=MyMeta):
#     ...
#
#
# class B(A):
#     b = 4
#
#     def b_method(self):
#         return None
#
#     # def __call__(self):
#     #     pass
#
#
# class C:
#     ...
#
#
# class D(B, C):
#     pass


"""
Написать метакласс, который будет райзить ошибку если в класса-наследниках есть незадикорированные 
публичные методы
"""


def mark_decorated_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    wrapper._decorated = True
    return wrapper


class CheckDecoratedMetaClass(type):
    def __new__(mcs, class_name, parents, attrs):
        for name, value in attrs.items():
            if callable(value):
                if hasattr(value, '_decorated'):
                    print(name, class_name)
        return super().__new__(mcs, class_name, parents, attrs)


class SomeClass(metaclass=CheckDecoratedMetaClass):

    @mark_decorated_decorator
    def mark_decorated(self):
        """
        kjsdncjnskjnckjsd
        :self: SomeClass
        :return:
        """
        return self.__class__.__name__

    @mark_decorated_decorator
    def leave_non_decorated(self):
        return 'fff'


obj = SomeClass()
# print(obj.mark_decorated.__doc__)

"""
Написать декоратор класса, который позволит создать синглтон
"""


def class_decorator(cls):
    def wrapper(*args, **kwargs):
        return cls(*args, **kwargs)

    return wrapper


new_int = 5
new_int += 1

for i in range(0, 101):  # O(100) -> O(n)
    for j in range(0, 101):  # O(n**2)
        if i < j:
            print(i, j)
        if i < 10:
            print(i)
        print(i)

# O(n)
