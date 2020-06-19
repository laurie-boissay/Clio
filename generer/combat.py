from random import randint, randrange


from generer.personnage import *
from generer.classe_personnage import Personnage




"""
Méchanismes de combat.
"""


def find_player_charac_name(message, member):
        for k, v in info_de_partie[num_team(message)].items():
            if member == k :
                return v["p_prénom"]


def find_player_charac_level(message, member):
        for k, v in info_de_partie[num_team(message)].items():
            if member == k :
                return v["p_niveau"]


def players(message):
    # Renvoie la liste des joueurs.
    return info_de_partie[num_team(message)]["quête en cours"]["players"]


def boss(message):
    #dictionnaire contenant : genre, race, classe, don, prénom, pronom, nom, age
    return info_de_partie[num_team(message)]["quête en cours"]["boss"]


def difficulte(message):
    #dictionnaire contenant : niveau, nb salles, récompense, multiplicateur.
    return info_de_partie[num_team(message)]["quête en cours"]["difficulté"]


def combat(message):
    return info_de_partie[num_team(message)]["combat_autorisé"]


def achats(message):
    return info_de_partie[num_team(message)]["achats_autorisés"]


def quete_en_cours(message):
    return info_de_partie[num_team(message)]["quête en cours"]


def ennemis_dans_salle(message):
    return info_de_partie[num_team(message)]["quête en cours"]["ennemis"]


def niveau_des_perso(message):
    return info_de_partie[num_team(message)]["niveau des joueurs"]


def carac_ennemis(message, nb):
    return info_de_partie[num_team(message)]["quête en cours"]["ennemis"][nb]


def resolution_combat(message):
    """
    """
    #est appelé par attaque arme ou attaque capacité
    #besoin d'un palier de réussite
    #besoin d'une liste d'initiative
    # appelle roll pour lancer les degats
    texte = ""
    return texte

def generer_ennemis(message):
    info_de_partie[num_team(message)]["quête en cours"]["ennemis"] = []
    

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


def generer_ennemis(message):    
    if len(ennemis_dans_salle(message)) == 0:
        
        players_level(message)
        
        for i in range(difficulte(message)["multiplicateur"]*len(players(message))):
            ennemi = Personnage()
            niveau_ennemi = niveau_des_perso(message)[randrange(len(niveau_des_perso(message)))]           
            ennemi.set_niveau(niveau_ennemi)
            info_de_partie[num_team(message)]["niveau des joueurs"].remove(niveau_ennemi)
           
            ennemi.set_type_pers("PNJ")
            ennemi.set_particularites()
            ennemi.set_total_points()
            ennemi.set_valeur_max()
            ennemi.stat_prioritaire_de_classe()
            ennemi.set_points_de_vie_maximum()
            ennemi.set_armure(difficulte(message)["multiplicateur"])
            ennemi.set_arme()

            info_de_partie[num_team(message)]["quête en cours"]["ennemis"].append(ennemi.get_ennemi())
   

def players_level(message):
    info_de_partie[num_team(message)]["niveau des joueurs"] = []
    
    for i in range(len(players(message))):
        for j in range(difficulte(message)["multiplicateur"]):
            info_de_partie[num_team(message)]["niveau des joueurs"].append(find_player_charac_level(message, players(message)[i]))


def texte_decrivant_ennemis(message):
    texte = "Vous n'êtes pas seul.e.s :"

    for i in range(difficulte(message)["multiplicateur"]*len(players(message))):
        texte += "\n- " + carac_ennemis(message, i)["classe"]
        texte += " " + carac_ennemis(message, i)["race"]
        texte += " de niveau " + str(carac_ennemis(message, i)["niveau"]) + " : "
        texte += "matricule : **" + str(i+1) + "** "

    return texte


def generer_liste_initiative(message):
    texte = ""
    return texte


def lancer_combat(message):
    texte = ""
    #if players(message)[i] not in combat(message):
            #info_de_partie[num_team(message)]["combat_autorisé"].append(players(message)[i])
    return texte