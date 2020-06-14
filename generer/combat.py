"""
Méchanisme de combat
"""

from generer.personnage import *
from random import randint


def resolution_combat(message):
    """
    """
    #est appelé par attaque arme ou attaque capacité
    #besoin d'un palier de réussite
    #besoin d'une liste d'initiative
    # appelle roll pour lancer les degats
    texte = ""
    return texte
    

def associer_stat(message, stat):
    """
    Quelle fonction correspond à cette stat ?
    Appelle la fonction.
    Renvoie la valeur de la stat correspondant au personnage joueur.
    """
    if stat == "force":
        valeur = force(message)

    elif stat == "dextérité":
        valeur = dexterite(message)

    elif stat == "constitution":
        valeur = constitution(message)

    elif stat == "intelligence":
        valeur = intelligence(message)

    elif stat == "sagesse":
        valeur = sagesse(message)

    else: #"charisme"
        valeur = charisme(message)

    return valeur


def roll(nb_des, valeur_des, bonus):
    resultats = [0] * nb_des
    total = 0
    
    texte = "\n" + str(nb_des) + " dé(s) " + str(valeur_des) + " :\n "

    for de in range(nb_des):
        resultats[de] = randint(1, valeur_des)
    
    for index in range(nb_des):
        texte +=  str(resultats[index])
        total += resultats[index]
        
        if index != nb_des - 1 :
            texte += " + "
    
    texte = texte + "\n (" + str(total) + ")" 
    
    if bonus != 0:
        texte += " + " + str(bonus)
    
    texte = texte + " = " + "**" + str(total+bonus) + "**"

    #return resultat, texte
    return texte