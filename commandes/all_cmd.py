import discord

from commandes.des import *

from collection_info.save_game import *

from generer.classe_personnage import Personnage

from collection_de_mots.personnage import *
from collection_de_mots.equipement import *


def all_users_cmd(message, client):
    canal = message.channel
    texte = "not a cmd"

    if (message.author != client.user): # User is not Clio.
            
        if 'clio clio clio' in message.content:
            canal = message.author
            texte = ("https://raw.githubusercontent.com/laurie-boissay/Clio/master/clio__muse_of_history_by_cetrece-dcwuzqk.png")

        elif message.content.startswith('!aide'): 
            # Renvoi un message d'aide.
            texte = texte_aide()

        elif message.content.startswith('!nouvelle partie'):
            texte = texte_nouvelle_partie(message)
            canal = message.author

        elif message.content.startswith('!pj'):
            # génère un PJ, renvoi un texte.
            texte = texte_pj(message)
            canal = message.author

        elif message.content.startswith('!info'):
            # Renvoi le lien vers mon Github.
            texte = texte_info()
            canal = message.author

        elif message.content.startswith('!classes'):
            # génère un PJ, renvoi un texte.
            texte = texte_classes()
            canal = message.author

        elif message.content.startswith('!genres'):
                # Renvoi la liste des genres qui influencent la génération d'un prénom.
                texte = ""
                for i in range(len(genre)):
                    texte += genre[i] + ", "
                canal = message.author

        elif message.content.startswith('!armes') and message.author in team_des_joueurs:
            texte = boutique_d_armes(message)

        elif message.content.startswith('!joue'):
            texte = texte_joue(message)

        elif message.content.startswith('!qui'):
            texte = texte_qui(message)

        elif message.content.startswith('!'):
            texte = commande_des(message.content)
            if texte != "not a cmd" :
                if message.author in team_des_joueurs:
                    perso = nom_perso(message)
                else:
                    perso = message.author.name
                texte = str(perso) + " s'empare des dés : " + texte
          
    return canal, texte


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

def dexterite(message):
    """
    Renvoie (int) la dextérité du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][3]

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

def vie_max(message):
    """
    Renvoie (int) le maximum de points de vie du personnage 
    associé au joueur/à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][7]

def argent(message):
    """
    Renvoie (int) l'argent du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][8]


def perso_classe(message):
    """
    Renvoie la classe du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][9]

def genre(message):
    """
    Renvoie le genre du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][10]

def don(message):
    """
    Renvoie le genre du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][11]


def boutique_d_armes(message):
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
        texte += '> !armes:dextérité\n\n"Remarquez, bonne une dague, c\'est toujours utile !"\n'
        texte += "> !armes:dague\n\n"
        return texte
    else:
        mot_cle = mot_cle[1].lower()
        mot_cle = mot_cle.strip(" ")
    
        return liste_d_armes(mot_cle)
 

def liste_d_armes(mot_cle):
    trouvaille = ""
    for i in range(len(armes_armures)):

        for k, v in armes_armures[i].items():
            if mot_cle in k or mot_cle in v[-1] or mot_cle in v[0]:
                trouvaille += k + " : "
                for f in range(len(v)-1):
                    trouvaille += str(v[f][0]) + v[f][1] + v[f][2] + "\n"
                trouvaille += "Utilisable " + v[-1] + ".\n\n"

    if trouvaille == "":
        texte = "Ha non j'ai pas ça. J'espère quand même vous revoir, bonne journée."
    else:
        texte = "J'ai quelque chose qui pourraient bien vous intéresser !\n\n" + trouvaille

    return texte

def num_team(message):
    """
    Renvoie le numéro de team associé au joueur/
    à la joueuse.
    """
    for k, v in team_des_joueurs.items():
        if k == message.author:
            team = v            

    return team


def texte_aide():
    texte = [
    "Je suis Clio, la muse de l'histoire et j'adore le JDR."
    "\nTu peux me parler en toute confidentialité en message privé."
    "\nJe suis là pour faire vivre des histoire épiques à mes joueurs."
    "\nPour que cela soit possible, il y a plusieurs étapes :"

    "\n\n```!nouvelle partie```"
    "Tu dois écrire cette commande dans le canal ou va se dérouler la partie."
    "\nCette commande te renvoie en message privé un numéro de team."
    "\nCommunique ce numéro aux joueurs que tu souhaite inviter dans la partie."

    "\n\n```!pj, prénom=Clio, classe=druide, genre=androgyne, team=0```"
    "Chaque joueur va générer un personnage personnalisé."
    "\nDans cet exemple le numéro de team est 0."
    
    "\n\nTous les joueurs doivent enregistrer leur personnage."
    "\nJe génère moi même la commande de sauvegarde, il suffit de la copier-coller et valider !"

    "\n\n```!qui```"
    'Permet de vérifer que ton perso est bien "enregistré".'
    "\nDans cet exemple 0 est le numéro de team."           
    ]
    return texte[0]


def texte_nouvelle_partie(message):
    team_number = len(info_de_partie)
    info_de_partie.append({})
    allowed_channels.append(message.channel.id)

    texte = "Voici ton code de team : " + str(team_number)
    texte += "\nCommunique cette commande aux joueurs que tu invites dans ta partie."
    texte += "\n\n```!pj, team=0```"
    texte += "Chaque joueur va générer un personnage qu'il peut personnaliser."

    return texte


def texte_pj(message):
    pj = Personnage()
    pj.set_cmd_texte(message)
    pj.set_param_identite()
    pj.set_particularites()
    pj.stat_prioritaire_de_classe()
    
    return pj.afficher_personnage()


def texte_info():
    texte = [
    "Vous pensez que les gnomes ont le monopole de la technologie ?"
    "\nVous pouvez participer à mon amélioration :" 
    "\nhttps://github.com/laurie-boissay/clio"
    ]
    return texte[0]


def texte_classes():
    texte = "Les classes implémentées :\n\n"
    
    for k, v in classes_et_carac_associee.items():
        texte += k + " : " + v + "\n"
    
    return texte


def texte_joue(message):
    """
    On envoie le personnage dans la liste info_de_partie.
    Cette liste contient des dictionnaires.
    Le dictionnaire à l'indice 0 est attribué à la team n°0.

    On envoie le message.author du joueur dans team_des_joueurs.
    C'est un dictionnaire qui associe pseudo et n° de team.
    """

    #les paramètres sont séparés par le symbole :
    cmd = message.content.split(":")

    pseudo_player = message.author
    nom_perso = cmd[1]
    
    try:
        team = int(cmd[2])
    except ValueError:
        return "Il me faut un numéro de team."

    carac = cmd[3].split(",")
    autre = cmd[4].split(",")

    # le message.author du joueur est associé à son nom de personnage.
    info_de_partie[team][pseudo_player] = [nom_perso]

    #le message.author du joueur est associé à sa team.
    team_des_joueurs[message.author] = team

    #On associe le nom du perso à ses carac et classe.
    for i in range(len(carac)):
        info_de_partie[team][pseudo_player].append(int(carac[i]))
    for i in range(len(autre)):
        info_de_partie[team][pseudo_player].append(autre[i])

    #Confirmation de succés.
    
    return "Compris " + message.author.name + ", tu joues " + info_de_partie[team][pseudo_player][0] + "."


def texte_qui(message):
    if message.author not in team_des_joueurs:
        player = False

    if player:

        genre_perso = genre(message)

        if genre_perso == "androgyne":
            determinant = "un.e"
        elif genre_perso == "féminin":
            determinant = "une"
        else:
            determinant = "un"

        texte = "Tu joues " + nom_perso(message)
        texte += ", " + determinant + " " + perso_classe(message) + " :\n"
        texte += "Force : " +  str(force(message)) + "\n"
        texte += "Constitution : " + str(constitution(message)) + "\n"
        texte += "Dextérité : " + str(dexterite(message)) + "\n"
        texte += "Intelligence : " + str(intelligence(message)) + "\n"
        texte += "Sagesse : " + str(sagesse(message)) + "\n"
        texte += "Charisme : " + str(charisme(message)) + "\n"

    else:
        texte = message.author.name + ", tu n'as pas encore de personnage enregistré."
        texte += "\n> !aide"

    return texte


# !pj, team 0