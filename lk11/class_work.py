import json
import random
from datetime import datetime


class Person:
    lags_count = 2

    def __init__(self, eyes_count):
        self.__eyes_count = eyes_count
        self.count_of_tooth = self._get_tooth_count()

    @property
    def eyes_count(self):
        return self.__eyes_count

    @eyes_count.setter
    def eyes_count(self, value):
        if not isinstance(value, int):
            raise TypeError

        self.__eyes_count = value

    @eyes_count.deleter
    def eyes_count(self):
        print(self.some_static_method())
        raise Exception('Not allowed')

    def _get_tooth_count(self):
        return random.randint(0, 32)

    @classmethod
    def some_class_method(cls, value):
        print('kjfkfkkf')
        print(cls)
        return cls(value)

    @classmethod
    def change_lags_count(cls, value):
        cls.lags_count = value
        print(cls.some_static_method())

    @staticmethod
    def some_static_method():
        return 1 + 1


person = Person.some_class_method(2)
# print(person._Person__eyes_count) # нужно запомнить, но в продакш коде так не писать
print(person.eyes_count)
person.eyes_count = 4
print(person.eyes_count)
# del person.eyes_count
# person._eat()
print(person.count_of_tooth)

print(Person.lags_count)
Person.change_lags_count(6)
print(Person.lags_count)
print(person.lags_count)
Person.some_static_method()
person.some_static_method()
# person.some_class_method(3)
# del Person.lags_count
# print(person.lags_count)


"""
Написать класс - Список дел. Написать класс, который опишет каждый отдельный пункт списка
Написать функцию, которая позволит:
    1. Добавить пункт в список
    2. Отметить пункт как сделаный
    3. Покажет не сделаные дела
    4. Покажет сделаные дела
    5. При выходе из нашего интерфейса сохранит все в файл (формат файла на выбор)
"""


class Item:
    def __init__(self, is_done: bool, info: str, is_created_now: bool,
                 created: datetime) -> None:
        self.is_done = is_done
        self.info = info
        self.last_updated = None
        self.created = datetime.now() if is_created_now else created

    def as_dict(self) -> dict:
        return {
            'is_done': self.is_done,
            'info': self.info,
            'last_updated': str(self.last_updated),
            'created': str(self.created),
        }


class TodoList:
    def __init__(self, name: str, owner: str, dead_line: datetime):
        self.name = name
        self.owner = owner
        self.dead_line = dead_line
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        try:
            with open(f'{self.name}.json') as file:
                data = json.load(file)
                tasks = []
                for item in data:
                    tasks.append(
                        Item(is_done=item['is_done'], info=item['info'], created=item['created'], is_created_now=False))
                return tasks
        except FileNotFoundError:
            return []

    def add_task(self, task: Item):
        self.tasks.append(task)

    def done_task(self, index):
        task = self.tasks[index]
        task.is_done = True
        task.last_updated = datetime.now()

    def undone_task(self, index):
        task = self.tasks[index]
        task.is_done = False
        task.last_updated = datetime.now()

    @property
    def done_tasks(self):
        tasks = ''
        for item in self.tasks:
            if item.is_done:
                tasks += f'\n {item.is_done}\t {item.info} \t {item.created}'
        return tasks

    @property
    def undone_tasks(self):
        tasks = ''
        for item in self.tasks:
            if not item.is_done:
                tasks += f'\n {item.is_done}\t {item.info} \t {item.created}'
        return tasks

    def to_json(self):
        with open(f'{self.name}.json', 'w', encoding='utf-8') as file:
            tasks = []
            for item in self.tasks:
                tasks.append(item.as_dict())
            json.dump(tasks, file, indent=4, ensure_ascii=False)

    @property
    def tasks_list(self):
        tasks = ''
        for index, item in enumerate(self.tasks):
            tasks += f'\n {index}\t {item.is_done}\t {item.info}\t {item.created}'
        return tasks


def init_todo_list():
    name = input('List name')
    owner = input('List owner')
    return TodoList(name=name, owner=owner, dead_line=datetime.now())


def main():
    todo_list = init_todo_list()
    try:
        while True:
            action = input('input action')

            if action == 'add':
                is_done = input('1 or 0')
                if is_done not in {'1', '0'}:
                    continue
                is_done = bool(int(is_done))
                info = input('Input some info')
                todo_list.add_task(Item(is_done, info, is_created_now=True, created=datetime.now()))
            elif action == 'tasks':
                print(todo_list.tasks_list)
            elif action == 'undone_tasks':
                print(todo_list.undone_tasks)
            elif action == 'done_tasks':
                print(todo_list.done_tasks)
            elif action == 'done_task':
                index = input('Task index')
                todo_list.done_task(int(index))
            elif action == 'undone_task':
                index = input('Task index')
                todo_list.undone_task(int(index))
            elif action == 'exit':
                todo_list.to_json()
                return
    except Exception:
        todo_list.to_json()


if __name__ == '__main__':
    main()
