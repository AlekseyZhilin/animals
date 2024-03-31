from animals_class import make_dog, make_cat, make_hamster, make_horse, make_camel, make_donkey
from animals_class import AnimalsList

def main():
    dog1 = make_dog('шарик', '2020-01-01')
    dog2 = make_dog('рэй', '2022-01-01')

    animals_list = AnimalsList()
    animals_list.add_animal(dog1)
    animals_list.add_animal(dog2)
    animals_list.show_animals()

main()
