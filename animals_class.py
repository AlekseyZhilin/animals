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

    def show_commands(self):
        print(f'Команды выполняемые {self.name}:')
        for i, cmd in enumerate(self.commands_list):
            print(f'{i}) {cmd}')

class Dog(InterfaceAnimals):
    count = 0
    def __init__(self, name: str, birth_date: datetime.date):
        super().__init__(name, birth_date)
        self.type = type_animals[0]
        self.vid = vid_animals[0]
        Dog.count += 1

    def __str__(self):
        return f'{self.name}, {self.birth_date}, {self.type}, {self.vid}'

class Cat(InterfaceAnimals):
    count = 0
    def __init__(self, name: str, birth_date: datetime.date):
        super().__init__(name, birth_date)
        self.type = type_animals[1]
        self.vid = vid_animals[0]
        Cat.count += 1

    def __str__(self):
        return f'{self.name}, {self.birth_date}, {self.type}, {self.vid}'


class Hamster(InterfaceAnimals):
    count = 0

    def __init__(self, name: str, birth_date: datetime.date):
        super().__init__(name, birth_date)
        self.type = type_animals[2]
        self.vid = vid_animals[0]
        Hamster.count += 1

    def __str__(self):
        return f'{self.name}, {self.birth_date}, {self.type}, {self.vid}'

class Horse(InterfaceAnimals):
    count = 0

    def __init__(self, name: str, birth_date: datetime.date):
        super().__init__(name, birth_date)
        self.type = type_animals[3]
        self.vid = vid_animals[1]
        Horse.count += 1

    def __str__(self):
        return f'{self.name}, {self.birth_date}, {self.type}, {self.vid}'

class Camel(InterfaceAnimals):
    count = 0

    def __init__(self, name: str, birth_date: datetime.date):
        super().__init__(name, birth_date)
        self.type = type_animals[4]
        self.vid = vid_animals[1]
        Camel.count += 1

    def __str__(self):
        return f'{self.name}, {self.birth_date}, {self.type}, {self.vid}'

class Donkey(InterfaceAnimals):
    count = 0

    def __init__(self, name: str, birth_date: datetime.date):
        super().__init__(name, birth_date)
        self.type = type_animals[5]
        self.vid = vid_animals[1]
        Donkey.count += 1

    def __str__(self):
        return f'{self.name}, {self.birth_date}, {self.type}, {self.vid}'

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
        if animal.name not in self.animals_list:
            self.animals_list.append(animal)
            return True
        
        print(f'Животное с именем уже {animal.name} существует')
        return  False

    def add_animals(self, list_animals: list):
        for i in list_animals:
            self.add_animal(i)

    def show_animals(self):
        print('Список всех животных:')
        for i, animal in enumerate(self.animals_list):
            print(f'{i + 1}) {animal}')



    