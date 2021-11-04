# coding: utf-8


class animal:
    """
        Modele pour animal
    """
    # propriete de classe
    list_animals = []
    list_rise_animals = []
    # methode d'instance
    # le premier argument doit être self (c'est à dire l'objet courant)
    # argument invisible lors de l'appel

    def __init__(
        self, 
        number = 0,
        espece = "lapin", 
        speed_max = 5, 
        color = "bleu",
        age = 1):
        """
            Constructeur
        """

        # propriétés d'instance
        self.number = number
        self.espece = espece
        self.speed_max = speed_max
        self.color = color
        self.age = age
        self.alive = True

    def old_animal(self):
        """
            Pour faire vieillir un animal
        """
        

    # Méthodes de classe
    # le premier argument doit être cls (c'est à dire la classe)
    # argument invisible lors de l'appel
    @classmethod
    def print_list_animal (cls):
        """
        Affiche la liste des animaux
        \n\tOu
        \n\tLa liste des nouveaux nées
        """
        print("Tu veux :\n  1 - La liste des animaux\n  2 - La liste des nouveaux nées\n")
        what_list = int(input("- "))

        if what_list == 1:

            if len(cls.list_animals) == 0:
                print(f"\nNous n'avons aucun animal dans le parc.")
                
            elif len(cls.list_animals) == 1:
                print(f"\nNous avons 1 animal dans le parc.\n")

            else:
                print(f"\nNous avons {len(cls.list_animals)} animaux dans le parc.\n")

            # pour chaque animal de la list_animals
            for my_animal in cls.list_animals:
                # afficher les infos de l'animal
                print(f"Le numéro {my_animal.number} est un {my_animal.espece} {my_animal.color}, il a {my_animal.age} ans et peut aller à {my_animal.speed_max}km/h.")

        if what_list == 2:
            if len(cls.list_rise_animals) == 0:
                print(f"\nNous n'avons aucun nouveau née dans le parc.")
                
            elif len(cls.list_rise_animals) == 1:
                print(f"\nNous avons 1 nouveau née dans le parc.\n")

            else:
                print(f"\nNous avons {len(cls.list_rise_animals)} nouveaux nées dans le parc.\n")

            # pour chaque nouveau née de la list_rise_animals
            for my_animal in cls.list_rise_animals:
                # afficher les infos du nouveau née
                print(f"Le numéro {my_animal.number} est un {my_animal.espece} {my_animal.color}, il a {my_animal.age} ans et peut aller à {my_animal.speed_max}km/h.")


# if __name__ == "__main__":
#     create_parc()
#     print(animal.list_animals)