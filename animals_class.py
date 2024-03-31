import datetime
from abc import ABC, abstractmethod

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

class AnimalsList:
    def __init__(self):
        self.animals_list = []
        
    def add_animal(self, pet) -> bool:
        if pet.name not in self.animals_list:
            self.animals_list.append(pet)
            return True
        
        print(f'Животное с именем уже {pet.name} существует')
        return  False

    def add_animals(self, list_animals: list):
        for i in list_animals:
            self.add_animal(i)

    def show_animals(self):
        print('Список всех животных:')
        for i, animal in enumerate(self.animals_list):
            print(f'{i}) {animal}')



    