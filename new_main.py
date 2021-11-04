# coding: utf-8

import rich_console as r_c
import gestion_parc as g_p
from animal import animal

command_possible = f"{r_c.text_soulign}\nQue souhaite-tu faire?{r_c.reset_text_soulign}\n\n  1 - {r_c.text_soulign}Afficher{r_c.reset_text_soulign} la liste des animaux\n  2 - Faire {r_c.text_soulign}naître{r_c.reset_text_soulign} un animal dans le parc\n  3 - {r_c.text_soulign}Ajouter{r_c.reset_text_soulign} un animal à la liste\n  4 - {r_c.text_soulign}Modifier{r_c.reset_text_soulign} un animal de la liste\n  5 - {r_c.text_soulign}Supprimer{r_c.reset_text_soulign} un animal de la liste\n  6 - {r_c.text_soulign}Quitter{r_c.reset_text_soulign} le programme\n"

def Main():
    """
    """
    logistic_continue = True
    # tant qu'on veut faire quelque chose 
    # on boucle
    while logistic_continue == True:
        print(command_possible)
        action_user = int(input("- "))

        # 1 - Afficher la liste des animaux
        if action_user == 1:
            animal.print_list_animal()
            # print()

        # 2 - Faire naître un animal dans le parc
        if action_user == 2:
            g_p.rise_animal()

        # 3 - Ajouter un animal à la liste
        # Et modifie les propriétés d'instance en conséquence
        if action_user == 3:
            g_p.add_parc()
            g_p.numero_animal+=1

        # 4 - Modifier un animal de liste
        if action_user == 4:
            print()
            g_p.modified_parc(animal.list_animals[0], color="jaune")



        # 5 - Supprimer un animal de la liste
        if action_user == 5:
            g_p.pull_of_parc()

        # 6 - Quitter le programme
        if action_user == 6:
            print(f"\n{r_c.text_soulign}Dans ce cas à la prochaine{r_c.reset_text_soulign}.")
            logistic_continue = False


# Code starts here
if __name__ == "__main__":
    r_c.clear_console()
    Main()
    print()
    animal.print_list_animal()