"""
Les méchanismes pour accéder et modifier le personnage.

#nom_joueur_id : ["nom_perso",F,Co,D,I,S,Ch,def,PV_max,PV,PA,xp,classe,genre,don,[sac],[équipé]],
"""



from collection_info.save_game import *

from collection_de_mots.equipement import *



def nom_perso(message):
    """
    Renvoie le nom du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][0]

def force(message):
    """
    Renvoie (int) la force du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][1]

def constitution(message):
    """
    Renvoie (int) la constitution du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][2]

def dexterite(message): # initiative = dex
    """
    Renvoie (int) la dextérité du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][3]

def modifier_dexterite(message, valeur):
    """
    Modifie la valeur de dextérité.
    """
    info_de_partie[num_team(message)][message.author][3] += valeur

def intelligence(message):
    """
    Renvoie (int) l'intelligence du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][4]

def sagesse(message):
    """
    Renvoie (int) la sagesse du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][5]

def charisme(message):
    """
    Renvoie (int) le charisme du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][6]

def defense(message):
    """
    Renvoie (int) le charisme du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][7]

def modifier_defense(message, valeur): # initiative = dex
    """
    Modifie la valeur de défense.
    """
    info_de_partie[num_team(message)][message.author][7] += valeur

def vie_max(message):
    """
    Renvoie (int) le maximum de points de vie du personnage 
    associé au joueur/à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][8]

def pv(message):
    """
    Renvoie (int) les points de vie actuels du personnage 
    associé au joueur/à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][9]

def argent(message):
    """
    Renvoie (int) l'argent du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][10]

def modifier_argent(message, montant):
    """
    Modifie la valeur de "Argent".
    """
    info_de_partie[num_team(message)][message.author][10] += montant

def xp(message):
    """
    Renvoie (int) l'expérience du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][11]

def perso_classe(message):
    """
    Renvoie la classe du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][12]

def genre(message):
    """
    Renvoie le genre du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][13]

def don(message):
    """
    Renvoie le genre du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][14]

def sac(message):
    """
    Renvoie le contenu du sac du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][15]

def equipement(message):
    """
    Renvoie l'équipement du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][16]

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
                texte += str(i+1) + "/3 pièce.s d'"
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