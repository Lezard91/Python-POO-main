# coding: utf-8

import rich_console as r_c
from animal import animal
import random as rd

numero_animal = 1
list_especes = ["Lapin", "Chat", "Mésange", "Python", "Chien", "Tourterelle", "Coccinelle", "Abeille"]
list_colors = ["Blanc", "Vert", "Bleu", "Rouge", "Jaune", "Noir"]

def add_parc ():
    """
    Ajouter un animal à la liste,
    \nEt modifie les propriétés d'instance en conséquence
    """
    print("\nEntre les caractéristiques de l'animal\n")
    new_espece = input("- Espèce : ")
    new_color = input("- Couleur : ")
    new_speed = input("- Vitesse (km/h): ")
    new_age = input("- Âge : ")
    new_animal = animal(number=numero_animal, espece=new_espece, speed_max=new_speed, color=new_color, age=new_age)
    animal.list_animals.append(new_animal)

def rise_animal ():
    numero_birth = len(animal.list_rise_animals)
    print("Combien de petits vont venirent au monde?")
    nb_birth = int(input("- "))
    for animal_birth in range(nb_birth):
        index_espece = rd.randrange(0,len(list_especes))
        index_color = rd.randrange(0,len(list_colors))
        new_espece = list_especes[index_espece]
        new_color = list_colors[index_color]
        numero_birth = numero_birth + 1
        new_animal = animal(number=numero_birth,espece=new_espece,color=new_color)
        animal.list_rise_animals.append(new_animal)

def modified_parc (
    my_animal,
    number = None,
    color = None,
    speed_max = None,
    alive = None):
    """
        my_animal est un objet de type animal
    """

    # modifie une valeur de propriété d'instance
    # de l'instance my_animal
    if number is not None:
        my_animal.number = number

    if color is not None:
        my_animal.color = color

    if speed_max is not None:
        my_animal.speed_max = speed_max

    if alive is not None:
        my_animal.alive = alive

def pull_of_parc ():
    """
    """
    print(f"\n{r_c.text_soulign}Quel est le numéro de l'animal que vous voulez retirer de la liste?{r_c.reset_text_soulign}\n")
    nb_supp = int(input("- "))
    nb_supp = nb_supp - 1

    # Supprime un animal de la liste list_animal
    animal.list_animals.pop(nb_supp)

if __name__ == "__main__":
    add_parc()
    print(animal.list_animals)