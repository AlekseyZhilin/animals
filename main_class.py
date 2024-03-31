import datetime

from animals_class import make_dog, make_cat, make_hamster, make_horse, make_camel, make_donkey
from animals_class import AnimalsList, type_animals

commands_array = ('сидеть', 'лежать', 'голос', 'вперед', 'назад')

def show_menu():
    print()
    print('-' * 70)
    print('Меню:')
    print('1) Показать список всех животных с коммандами')
    print('2) Показать список всех животных, отсортированных по дате рождения')
    print('3) Показать количество животных каждоко типа')
    print('4) Добавить животное')
    print('5) Добавить комманды, выбранному животному')
    print('6) Выход')
    print('-' * 70)

def check_choice(choice: str, end) -> int:
    bad_choice = 'Вы указали неверное значение'

    try:
        res = int(choice)
        if (res > 0) and (res <= end):
            return res
        else:
            print(bad_choice)
            return -1
    except:
        print(bad_choice)
        return  -1

def main():
    dog1    = make_dog('шарик', '2021-07-01')
    dog1.add_commands([commands_array[0], commands_array[1], commands_array[2]])
    dog2    = make_dog('рэй', '2018-01-01')
    dog2.add_command(commands_array[2])
    cat     = make_cat('мурка', '2020-01-01')
    hamster = make_hamster('хомя','2022-01-01')
    horse   = make_horse('быстрый', '2022-02-01')
    camel   = make_camel('странник', '2019-01-01')
    donkey  = make_donkey('бяша', '2020-01-01')
    donkey.add_command(commands_array[4])

    animals_list = AnimalsList()
    animals_list.add_animals([dog1, dog2])
    animals_list.add_animal(cat)
    animals_list.add_animal(hamster)
    animals_list.add_animals([horse, camel, donkey])

    choice = 0
    while True:
        show_menu()
        choice = input('Выберите пункт: ')
        if check_choice(choice, 6) != -1:
            choice = int(choice)

        if choice == 1:
            animals_list.show_animals()
        if choice == 2:
            animals_list.sort_by_birth_date()
        if choice == 3:
            animals_list.show_count_animals()
        if choice == 4:
            name = input('Введите имя животного: ')
            birth_date = input('Введите дату рождения yyyy-mm-dd: ')
            try:
                datetime.datetime.strptime(birth_date, '%Y-%m-%d')
            except ValueError:
                birth_date = f'{datetime.date.today().year}-{datetime.date.today().month}-{datetime.date.today().day}'
            for i, type_an in enumerate(type_animals):
                print(f'{i + 1}) {type_an}')
            res = input('Выберете тип животного: ')
            if check_choice(res, len(type_animals)) != -1:
                res = int(res)
                if res == 1:
                    anm = make_dog(name, birth_date)
                    animals_list.add_animal(anm)
                elif res == 2:
                    anm = make_cat(name, birth_date)
                    animals_list.add_animal(anm)
                elif res == 3:
                    anm = make_hamster(name, birth_date)
                    animals_list.add_animal(anm)
                elif res == 4:
                    anm = make_horse(name, birth_date)
                    animals_list.add_animal(anm)
                elif res == 5:
                    anm = make_camel(name, birth_date)
                    animals_list.add_animal(anm)
                elif res == 6:
                    anm = make_donkey(name, birth_date)
                    animals_list.add_animal(anm)
                print(f'Животное {name} добавлено')

        if choice == 5:
            name = input('Введите имя животного, для добавления комманды: ')
            anim = animals_list.find_animal(name)
            if anim is not None:
                for i, command_an in enumerate(commands_array):
                    print(f'{i + 1}) {command_an}')
                res = input('Выберете комманду: ')
                if check_choice(res, len(commands_array)) != -1:
                    anim.add_command(commands_array[int(res) - 1])
                    print(f'Комманда {commands_array[int(res) - 1]} добавлена')
            else:
                print(f'Нет животного с именем {name}')

        if choice == 6:
            break

        input('Для продолжения работы, нажмите любую enter ')

main()
