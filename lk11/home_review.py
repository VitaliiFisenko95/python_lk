"""
Описать сказку про Колобка (не обязательно про колобка) классами.
Ссылка на текст сказки  - https://nukadeti.ru/skazki/kolobok
Нужно создать классы деда, бабки, колобка, лисы (по желанию можно добавить героев) с методами, которые будут имитировать
реплики героев в сказке. Описывать реплики можно не полностью, вызывать методы нужно в очередности сченария,
как использовать - дело фонтазии))
к примеру:
class Fox(ParentClass):
    def eat_kolobok(self, kolobok):
        print('MMMM yammy') реплика лисы
        kolobok.die() метод, который описывает смерть колобка

fox = Fox()
fox.eat_kolobok(kolobok)

Тут описан пример как можно вызвать метод колобка в методе лисы, т.е. действие обязательно вызовет измение другого
объекта. Не стоит забывать что в питоне все типы подобны и мы можем передавать параметрами в метод/функцию любой
питоновский объект
"""


# Очень упрощеннная версия

class Hero:
    def __init__(self, name):
        self.name = name


class Ded(Hero):
    def ask_babka_to_bake_kolobok(self, babka):
        print('_______')
        babka.bake_kolobok()


class Babka(Hero):

    def bake_kolobok(self):
        print(')))))')


class Kolobok(Hero):
    def escape(self):
        print('escape')

    def die(self):
        print('((((((')


class Fox(Hero):

    def eat_kolobok(self, kolobok):
        print('eat')
        kolobok.die()


def tale():

    ded = Ded('ded')
    babka = Babka('babka')
    kolobok = Kolobok('kolobok')
    fox = Fox('fox')

    ded.ask_babka_to_bake_kolobok(babka)
    babka.bake_kolobok()
    kolobok.escape()
    fox.eat_kolobok(kolobok)


tale()
