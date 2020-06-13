"""
Les commandes et macro de lancer de dés.
"""

from random import randint

def roll(nb_des, valeur_des, bonus):
    resultats = [0] * nb_des
    total = 0
    text = "\n" + str(nb_des) + " dé(s) " + str(valeur_des) + " :\n "

    for de in range(nb_des):
        resultats[de] = randint(1, valeur_des)
    for index in range(nb_des):
        text +=  str(resultats[index])
        total += resultats[index]
        if index != nb_des - 1 :
            text += " + "
    text = text + "\n (" + str(total) + ")" 
    if bonus != 0:
        text += " + " + str(bonus)
    text = text + " = " + "**" + str(total+bonus) + "**"
    return text

