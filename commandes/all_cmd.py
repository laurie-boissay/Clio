import discord

from commandes.des import *

from collection_info.save_game import *

from generer.classe_personnage import Personnage

from collection_de_mots.personnage import *


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

        elif message.content.startswith('!joue'):
            texte = texte_joue(message)

        elif message.content.startswith('!qui'):
            texte = texte_qui(message)

        elif message.content.startswith('!'):
            texte = commande_des(message.content)
            if texte != "not a cmd" :
                texte = str(qui_joue(message)) + " s'empare des dés : " + texte
          
    return canal, texte


def qui_joue(message):
    """
    Renvoie le nom du personnage associé au joueur/
    à la joueuse.
    """
    team = num_team(message)
       
    for k, v in  info_de_partie[team].items():
        if k == message.author:
            perso = v

    return perso

def num_team(message):
    """
    Renvoie le numéro de team associé au joueur/
    à la joueuse.
    """
    try:
        for k, v in team_des_joueurs.items():
            if k == message.author:
                team = v
    except UnboundLocalError:
        texte = "inconu.e"

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
    
    "\n\n```!joue:Clio:0:3,0,3,1,3,2,druide```"
    "Tous les joueurs doivent enregistrer leur personnage suivi du numéro de team."
    "\nClio dans cet exemple est le nom de personnage et 0 est le numéro de team."
    "\nJe génère moi même la commande de sauvegarde, il suffit de la copier-coller et valider !"
    "\nVos noms de personnage doivent tous être différents."

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
    pj.bonus_de_metier()
    
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
    team = int(cmd[2])
    carac = cmd[3].split(",")

    # le message.author du joueur est associé à son nom de personnage.
    info_de_partie[team][pseudo_player] = nom_perso

    #le message.author du joueur est associé à sa team.
    team_des_joueurs[message.author] = team

    #On associe le nom du perso à ses carac et classe.
    info_de_partie[team][nom_perso] = []
    for i in range(len(carac)-1):
        info_de_partie[team][nom_perso].append(int(carac[i]))
    info_de_partie[team][nom_perso].append(carac[-1])

    #Confirmation de succés.
    
    return "Compris " + message.author.name + ", tu joues " + info_de_partie[team][pseudo_player] + "."


def texte_qui(message):
    texte = "Tu joues " + qui_joue(message)
    texte += ", un.e " + str(info_de_partie[num_team(message)][qui_joue(message)][6]) + " :\n"
    texte += "Force : " + str(info_de_partie[num_team(message)][qui_joue(message)][0]) + "\n"
    texte += "Constitution : " + str(info_de_partie[num_team(message)][qui_joue(message)][1]) + "\n"
    texte += "Dextérité : " + str(info_de_partie[num_team(message)][qui_joue(message)][2]) + "\n"
    texte += "Intelligence : " + str(info_de_partie[num_team(message)][qui_joue(message)][3]) + "\n"
    texte += "Sagesse : " + str(info_de_partie[num_team(message)][qui_joue(message)][4]) + "\n"
    texte += "Charisme : " + str(info_de_partie[num_team(message)][qui_joue(message)][5]) + "\n"

    return texte