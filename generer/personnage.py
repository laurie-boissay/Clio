from collection_info.save_game import *

from collection_de_mots.equipement import *

"""
Les méchanismes pour accéder et modifier le personnage.

#nom_joueur_id : ["nom_perso",F,Co,D,I,S,Ch,def,PV_max,PV,PA,xp,classe,genre,don,[sac],[équipé]],
"""


def nom_perso(message):
    """
    Renvoie le nom du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_nom"]

def prenom_perso(message):
    """
    Renvoie le prénom du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_prénom"]

def pronom_perso(message):
    """
    Renvoie le pronom du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_pronom"]

def race_perso(message):
    """
    Renvoie la race du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_race"]

def age_perso(message):
    """
    Renvoie l'age du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_age"]

def perso_classe(message):
    """
    Renvoie la classe du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_classe"]

def genre(message):
    """
    Renvoie le genre du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_genre"]

def don(message):
    """
    Renvoie le genre du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_don"]

def force(message):
    """
    Renvoie (int) la force du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_force"]

def constitution(message):
    """
    Renvoie (int) la constitution du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_constitution"]

def dexterite(message): # initiative = dex
    """
    Renvoie (int) la dextérité du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_dextérité"]

def modifier_dexterite(message, valeur):
    """
    Modifie la valeur de dextérité.
    """
    team = num_team(message)
    info_de_partie[team][message.author]["p_dextérité"] += valeur

def intelligence(message):
    """
    Renvoie (int) l'intelligence du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_intelligence"]

def sagesse(message):
    """
    Renvoie (int) la sagesse du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_sagesse"]

def charisme(message):
    """
    Renvoie (int) le charisme du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_charisme"]

def defense(message):
    """
    Renvoie (int) le charisme du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_défense"]

def modifier_defense(message, valeur): # initiative = dex
    """
    Modifie la valeur de défense.
    """
    team = num_team(message)
    info_de_partie[team][message.author]["p_défense"] += valeur

def vie_max(message):
    """
    Renvoie (int) le maximum de points de vie du personnage 
    associé au joueur/à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_PV max"]

def pv(message):
    """
    Renvoie (int) les points de vie actuels du personnage 
    associé au joueur/à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_PV"]

def argent(message):
    """
    Renvoie (int) l'argent du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_PA"]

def modifier_argent(message, montant):
    """
    Modifie la valeur de "Argent".
    """
    team = num_team(message)
    info_de_partie[team][message.author]["p_PA"] += montant

def xp(message):
    """
    Renvoie (int) l'expérience du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_XP"]

def niveau(message):
    """
    Renvoie (int) le niveau du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_niveau"]

def sac(message):
    """
    Renvoie le contenu du sac du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_sac"]

def equipement(message):
    """
    Renvoie l'équipement du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
    return info_de_partie[team][message.author]["p_équipement"]

def num_team(message):
    """
    Renvoie le numéro de team associé au joueur/
    à la joueuse.
    """
    for k, v in team_des_joueurs.items():
        if k == message.author:
            team = v            

    return team


def texte_possessions(message, indice):
    """
    Renvoie un texte : le contenu du sac ou l'armure équipée
    selon ce qui est précisé en paramètre.
    """
    if indice == "sac" :
        objet = sac(message)
    elif indice == "equipement":
        objet = equipement(message)

    if objet == []:
        texte = "rien "
    else:
        texte = ""
        for i in range(len(objet)):
            texte += "\n"
            if indice == "equipement":
                texte += str(i+1) + "/3 pièce.s : "
            texte += objet[i]
        texte += "\n"

    return texte


def appliquer_stat_armure(message, objet, operateur):
    """
    Cette fonction est appelée pour modifier les stat
    d'un personnage lorsqu'il porte ou enlève une pièce d'armure.

    Prend la valeur de défense de l'objet dans la liste armes_armures
    la soustrait ou l'additionne aux stats du personnage.

    Si l'armure à un malus de dextérité, procède de la même manière
    que pour la défense.
    """ 
    valeur_def = armes_armures[2][objet][0][0]
    valeur_dex = armes_armures[2][objet][1][0]

    if operateur == "+":
        modifier_defense(message, valeur_def)
        if len(armes_armures[2][objet]) > 4:
            modifier_dexterite(message, valeur_dex)

    else:
        modifier_defense(message, -valeur_def)
        if len(armes_armures[2][objet]) > 4:
            modifier_dexterite(message, -valeur_dex)