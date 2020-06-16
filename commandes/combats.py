"""
Les fonctions qui permettent de résoudre un combat.
"""

from generer.combat import *

from collection_de_mots.equipement import *

from collection_info.save_game import *


def attaque_arme(message, categorie):
    """
    Vérifie si le personnage possède l'arme.
        si non, renvoie un texte.

        Si oui, de quelle catégorie est-elle ?
        Puis sur quelle caractéristique elle touche ?
        appelle la fonction roll.

        A VENIR :
        est-ce touché ? (ajouter un paramètre)
            si oui : lancer les dégâts selon la catégorie.
            si non : texte, conséquences ?
    """
    if message.author not in info_de_partie[num_team(message)]["combat_autorisé"]:
        return "Vous ne pouvez pas combatre ici."

    cmd = message.content.strip("!")
    arme = cmd.strip(" ").lower()
    
    if arme in sac(message):
        
        if categorie == "une main":
            index = 0
        
        elif categorie == "deux mains":
            index = 1
        
        for k, v in armes_armures[index].items():
            if arme == k :
                stat = v[0][2]
        
        bonus = associer_stat(message,stat)
        texte = nom_perso(message) + " utilise 1 " + arme + " :\n"
        texte += roll(1, 20, bonus)

        #resultat, texte += roll(1, 20, bonus)
        #resolution_combat(message)

    else:
        texte = "Tu ne possède pas cette arme : " + arme + "."

    return texte


