import datetime

type_animals = ('собака', 'кошка', 'хомяк', 'лошадь', 'верблюд', 'осел')
vid_animals = ('домашнее животное', 'вьючное животное')

class InterfaceAnimals:
    def __init__(self, name: str, birth_date: datetime.date):
        self.name = name
        self.birth_date = birth_date
        self.commands_list = []

    def add_command(self, command: str):
        self.commands_list.append(command)

    def add_commands(self, commands_lisr: list):
        for i in commands_lisr:
            self.commands_list.append(i)

    def get_commands_str(self) -> str:
        commands = ' ('
        for i in self.commands_list:
            commands += ' ' + i
        commands += ' )'
        return commands

    def show_commands(self):
        print(f'Команды выполняемые {self.name}:')
        for i, cmd in enumerate(self.commands_list):
            print(f'{i}) {cmd}')

    def __gt__(self, other):
        return self.birth_date > other.birth_date

class Dog(InterfaceAnimals):
    count = 0
    def __init__(self, name: str, birth_date: datetime.date):
        super().__init__(name, birth_date)
        self.type = type_animals[0]
        self.vid = vid_animals[0]
        type(self).count += 1

    def __str__(self):
        return f'{self.name: <10s} {self.birth_date}, {self.type}, {self.vid} {self.get_commands_str()}'

class Cat(InterfaceAnimals):
    count = 0
    def __init__(self, name: str, birth_date: datetime.date):
        super().__init__(name, birth_date)
        self.type = type_animals[1]
        self.vid = vid_animals[0]
        type(self).count += 1

    def __str__(self):
        return f'{self.name: <10s} {self.birth_date}, {self.type}, {self.vid} {self.get_commands_str()}'


class Hamster(InterfaceAnimals):
    count = 0

    def __init__(self, name: str, birth_date: datetime.date):
        super().__init__(name, birth_date)
        self.type = type_animals[2]
        self.vid = vid_animals[0]
        type(self).count += 1

    def __str__(self):
        return f'{self.name: <10s} {self.birth_date}, {self.type}, {self.vid} {self.get_commands_str()}'

class Horse(InterfaceAnimals):
    count = 0

    def __init__(self, name: str, birth_date: datetime.date):
        super().__init__(name, birth_date)
        self.type = type_animals[3]
        self.vid = vid_animals[1]
        type(self).count += 1

    def __str__(self):
        return f'{self.name: <10s} {self.birth_date}, {self.type}, {self.vid} {self.get_commands_str()}'

class Camel(InterfaceAnimals):
    count = 0

    def __init__(self, name: str, birth_date: datetime.date):
        super().__init__(name, birth_date)
        self.type = type_animals[4]
        self.vid = vid_animals[1]
        type(self).count += 1

    def __str__(self):
        return f'{self.name: <10s} {self.birth_date}, {self.type}, {self.vid} {self.get_commands_str()}'

class Donkey(InterfaceAnimals):
    count = 0

    def __init__(self, name: str, birth_date: datetime.date):
        super().__init__(name, birth_date)
        self.type = type_animals[5]
        self.vid = vid_animals[1]
        type(self).count += 1

    def __str__(self):
        return f'{self.name: <10s} {self.birth_date}, {self.type}, {self.vid} {self.get_commands_str()}'

def make_dog(name, birth_date):
    return Dog(name, birth_date)

def make_cat(name, birth_date):
    return Cat(name, birth_date)

def make_hamster(name, birth_date):
    return Hamster(name, birth_date)

def make_horse(name, birth_date):
    return Horse(name, birth_date)

def make_camel(name, birth_date):
    return Camel(name, birth_date)

def make_donkey(name, birth_date):
    return Donkey(name, birth_date)

class AnimalsList:
    def __init__(self):
        self.animals_list = []
        
    def add_animal(self, animal: InterfaceAnimals) -> bool:
        if animal.name not in [i.name for i in self.animals_list]:
            self.animals_list.append(animal)
            return True
        
        print(f'Животное с именем уже {animal.name} существует')
        return  False

    def add_animals(self, list_animals: list):
        for i in list_animals:
            self.add_animal(i)

    def find_animal(self, name: str) -> InterfaceAnimals:
        for i in self.animals_list:
            if name == i.name:
                return i
        return None

    def show_animals(self):
        print('Список всех животных:')
        for i, animal in enumerate(self.animals_list):
            print(f'{i + 1}) {animal}')

    def show_count_animals(self):
        list_typs = []
        print('Количество животных:')
        for i, type_animal, count in [(i, animal.type, type(animal).count)
                                      for i, animal in enumerate(self.animals_list)]:
            if type_animal not in list_typs:
                list_typs.append(type_animal)
                print(f'{i + 1}) {type_animal: <10s} {count}')

    def sort_by_birth_date(self):
        print('Список всех животных, отсортированных по возрасту:')
        for i, animal in enumerate(sorted(self.animals_list)):
            print(f'{i + 1}) {animal}')

    