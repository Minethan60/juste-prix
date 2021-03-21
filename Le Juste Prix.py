# Created by Minethan - 21.03.2021 #
from random import randint
choix1 = int(input("Entrez un nombre minimum : "))
choix2 = int(input("Entrez un nombre maximum : "))
nbr = randint(choix1, choix2)
while True :
    text = int(input("Entrez un nombre entre " + str(choix1) + " & " + str(choix2) +  ": "))
    if text == nbr:
        print("Bravo ! Vous avez trouver le bon nombre qui était : " + str(nbr) + " !")
        break
    elif text < nbr:
        print("C'est plus !")
    elif text > nbr:
        print("C'est moins !")
# Created by Minethan - 21.03.2021 #