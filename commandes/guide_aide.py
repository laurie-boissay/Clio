"""
Les commandes qui affichent surtout du texte pour guider le joueur/la joueuse.
"""
from generer.classe_personnage import Personnage
from generer.personnage import *
from generer.guide_aide import *

from collection_info.save_game import *
from collection_de_mots.personnage import *
from collection_de_mots.equipement import *


def texte_aide():
    """
    Renvoie un texte d'aide/mode d'emploi.
    """
    texte = [
    "Je suis Clio, la muse de l'histoire et j'adore le JDR."
    "\nTu peux me parler en toute confidentialité en message privé."
    "\nJe suis là pour faire vivre des histoire épiques à mes joueurs."
    "\nPour que cela soit possible, il y a plusieurs étapes."
    "\nLa première est de créer une nouvelle partie. Ensuite, tu seras guidé.e."

    "\n\n```!initialiser```"
    "Créer une nouvelle partie."
    "\nTu dois écrire cette commande dans le canal ou va se dérouler la partie."
    "\nTu vas recevoir en message privé une commande."
    "\n Il faudra l'envoyer en en message privé aux autres joueurs et "
    "\nla copier-coller aussi en message privé mais dans mon canal."

    "\n\n```!quête```"
    "Quand vous êtes prêt.e.s à partir à l'aventure, génère une quête."

    "\n\n```!qui```"
    'Permet de vérifer que ton perso est bien "enregistré".'
    "\nDans cet exemple 0 est le numéro de team."
    ]
    return texte[0]


def texte_initialiser(message):
    """
    Nombre = combien de partie son enregistrées dans info_de_partie.
    Pour une nouvelle parie, le team_number correspondra à ce nombre.

    Indique que la partie est bien créée, le numéro de team assigné,
    un texte d'aide.

    Ajoute un dictionnaire dans la liste info_de_partie àl'indice team_number.
    Ajoute dans ce dictionnaire 3 entrées : 
        - "allowed_channel" : le canal dans le quel la partie se jouera ;
        - "achats_autorisés" : (liste de joueurs autorisés) ;
        - "combat_autorisés" : (liste de joueurs autorisés).

    Si la commande !initialiser est tapée en message privé, le texte devient un message d'erreur.
    
    renvoie le texte.
    """
    try:
        team_number = len(info_de_partie)
        texte = "La partie à bien été créée."
        texte += "\n\nCommunique cette commande en message privé aux joueurs que tu invites dans ta partie :"
        texte += "```!rejoindre:" + str(team_number) + "```"
        texte += "\nChaque joueur doit rejoindre ta partie y compris toi."
        texte += "\nPour garder ce code secret, tapez tous la commande ci-dessus en message privé."
        
        info_de_partie.append({})
        info_de_partie[team_number]["allowed_channel"] = message.channel.name
        info_de_partie[team_number]["achats_autorisés"] = []
        info_de_partie[team_number]["combat_autorisés"] = []
    
    except AttributeError:
        texte = "La commande :```!initialiser```doit être tapée dans le canal ou va se jouer la partie.\n"

    return texte


def texte_rejoindre(message):
    """
    Le message.author du joueur est associé à la team indiquée dans la liste team_des_joueurs.
    Texte de confirmation, aide.
    
    Si le numéro de team n'est pas indiqué le texte devient un message d'erreur.
    Si le numéro de team n'est pas bon le texte devient un message d'erreur.
    Si le dictionnaire team de la liste info_de_partie n'a pas d'entrée "allowed_channel":
        le texte devient un mesage d'erreur.

    Renvoie le texte.
    """
    cmd = message.content.split(":")

    pseudo_player = message.author

    try:     
        team = int(cmd[1])
        team_des_joueurs[message.author] = team
        texte = message.author.name + " tu as bien rejoins la team n°" + str(team_des_joueurs[message.author])
        texte += ".\nLe canal écrit discord autorisé pour cette partie est : "
        texte += str(info_de_partie[team]["allowed_channel"])

        texte += "\n\nJe t'invite à t'y rendre pour générer ton personnage :"
        texte += "```!pj```"

    except ValueError:
        texte = "Il me faut un numéro de team."
    except IndexError:
        texte = "Ce numéro de team n'est pas bon."
    except KeyError:
        texte = "Il faut d'abord créer une partie."

    return texte
    

def boutique_d_armes(message):
    """
    Vérifie si les achats sont autorisés pour ce personnage.
        si non, retourne un texte.
        si oui, vérifie si la demande d'achat précise un objet.
            si non, demande de préciser avec un texte d'aide.
            si oui, appelle la fonction liste_d_armes.
    """
    if message.author not in info_de_partie[num_team(message)]["achats_autorisés"]:
        return "Les achats sont autorisés en ville uniquement."

    else:
        mot_cle = message.content.split(":")
        
        if len(mot_cle) == 1:
            texte = '"Bienvenue dans mon échoppe. Alors si je comprend bien vous cherchez des armes.'
            texte += "\nJ'ai beaucoup de choses en stock. Soyez plus "
            
            if genre(message) == "masculin":
                texte += "précis"
            elif genre(message) == "féminin":
                texte += "précise"
            else:
                texte += "précis.e"

            texte += ' s\'il vous plaît."\nIl gesticule dans tous les sens :\n\n'
            texte += '"Vous voulez une arme à distance\n'
            texte += '> !armes:distance\n\nou peut être une arme lourde ?"\n'
            texte += '> !armes:deux mains\n\n"A moins que vous ne soyez très habile de vos mains ?"\n'
            texte += '> !armes:dextérité\n\n"Remarquez, une bonne une dague, c\'est toujours utile !"\n'
            texte += "> !armes:dague\n\n"
            return texte
        
        else:
            mot_cle = mot_cle[1].strip(" ").lower()
        
            return liste_d_armes(mot_cle)


def texte_classes():
    """
    Renvoie un texte : la liste des classes implémentées.
    """
    texte = "Les classes implémentées :\n\n"
    
    for k, v in classes_et_carac_associee.items():
        texte += k + " : " + v + "\n"
    
    return texte


def texte_dons(message):
    """
    Si une classe n'est pas précisée dans le message :
        renvoie un texte d'aide.

    Si, une classe est précisée :
        parcours toutes les listes de classes pour trouver une occurence
        Renvoie un texte avec les dons de la classe.

    Si une classe est précisée mais qu'elle ne correspond à rien:
        renvoie un texte d'erreur/aide. 
    """
    cmd = message.content.split(":")
    texte = ""
    index = ""

    try:
        dons = cmd[1].strip(" ").lower()
    except IndexError:
        texte += "Quelle classe t'intéresse ?\n"
        texte += "> !dons:nécromancien.ne"
        return texte

    for i in range(len(toutes_classes)):
        for j in range(len(toutes_classes[i])):
            if dons == toutes_classes[i][j]:
                for k, v in dons_par_classes[j].items():
                    texte += "__" + k.capitalize() + "__" + " : " + v + "\n\n"

                return texte

    return "je ne connais pas cette classe.\n> !classes"


def texte_info():
    """
    Renvoie un texte : ambiance + l'adresse du dossier Clio sur Github.
    """
    texte = [
    "Vous pensez que les gnomes ont le monopole de la technologie ?"
    "\nVous pouvez participer à mon amélioration :" 
    "\nhttps://github.com/laurie-boissay/clio"
    ]
    return texte[0]

def texte_genres(message):
	"""
	Return un texte avec la liste des genres implémentés.
	"""
	texte = ""
	for i in range(len(genre_pers)):
		texte += genre_pers[i] + ", "

	return texte

def texte_pj(message):
    """
    Génère un personnage joueur.
    Renvoie un texte : une commande.
    """
    pj = Personnage()
    pj.set_cmd_texte(message)
    pj.set_param_identite()
    pj.set_particularites()
    pj.set_don()
    pj.stat_prioritaire_de_classe()
    pj.set_points_de_vie_maximum()
    
    return pj.afficher_personnage()

