import gc
import sys
import weakref


# class A:
#     pass
#
#
# a = A()
#
# print(sys.getrefcount(a))
#
# # print(gc.get_threshold())
#
#
# d = {'a': a}
# print(sys.getrefcount(a))
# l = [a]
# print(sys.getrefcount(a))
# s = {a}
#
# print(sys.getrefcount(a))


# class B:
#     def __init__(self):
#         self.b = 'bb'
#
#
# # a = B()
# #
# # print(sys.getrefcount(a))
#
#
# b = B()
# print(sys.getrefcount(b))
# d1 = {'b': weakref.ref(b)}
#
# print(sys.getrefcount(b))
# print(d1)
# # del b
# print(d1)
# print(d1['b'])
# print(dir(d1['b']))

class C:
    def __init__(self):
        self.name = self.__class__.__name__


c = C()
print(sys.getrefcount(c))
d2 = {'c': weakref.proxy(c)}
print(sys.getrefcount(c))
# del c
print(d2['c'].name)
print(sys.getrefcount(c))
