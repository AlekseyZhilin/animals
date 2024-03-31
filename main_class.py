from animals_class import make_dog, make_cat, make_hamster, make_horse, make_camel, make_donkey
from animals_class import AnimalsList

commands_array = ('сидеть', 'лежать', 'голос', 'вперед', 'назад')

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

    animals_list = AnimalsList()
    animals_list.add_animals([dog1, dog2])
    animals_list.add_animal(cat)
    animals_list.add_animal(hamster)
    animals_list.add_animals([horse, camel, donkey])
    anm = animals_list.find_animal('бяша')
    anm.add_commands([commands_array[3], commands_array[4]])

    animals_list.show_animals()
    animals_list.show_count_animals()
    animals_list.sort_by_birth_date()

main()
