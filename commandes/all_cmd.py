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

        elif message.content.startswith('!rejoindre'):
            texte = texte_rejoindre(message)
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

        elif message.content.startswith('!achat') and message.author in team_des_joueurs:
            texte = achat(message)

        elif message.content.startswith('!équiper') and message.author in team_des_joueurs:
            texte = equiper(message)

        elif message.content.startswith('!déséquiper') and message.author in team_des_joueurs:
            texte = desequiper(message)

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

#nom_joueur_id : ["nom_perso",F,Co,D,I,S,Ch,def,PV_max,PV,PA,xp,classe,genre,don,[sac],[équipé]],

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

def defense(message):
    """
    Renvoie (int) le charisme du personnage associé au joueur/
    à la joueuse.
    """
    return info_de_partie[num_team(message)][message.author][7]

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


def boutique_d_armes(message):
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
            mot_cle = mot_cle[1].lower()
            mot_cle = mot_cle.strip(" ")
        
            return liste_d_armes(mot_cle)
 

def liste_d_armes(mot_cle):
    trouvaille = ""
    for i in range(len(armes_armures)):

        for k, v in armes_armures[i].items():
            if mot_cle in k or mot_cle in v[0] or mot_cle in v[-3] or mot_cle in v[-2] or mot_cle in str(v[-1]):
                trouvaille += k.capitalize() + " : "
                for f in range(len(v)-3):
                    trouvaille += str(v[f][0]) + v[f][1] + v[f][2] + ".\n"
                trouvaille += "Utilisable " + v[-3] + ", " + v[-2] + " : " + str(v[-1]) + " PA.\n\n"

    if trouvaille == "":
        texte = "Ha non j'ai pas ça. J'espère quand même vous revoir, bonne journée."
    else:
        texte = "J'ai quelque chose qui pourrait bien vous intéresser !\n\n" + trouvaille
        texte += "Alors, ça vous plaît ?"
        texte += "\n> !achat:épée rutillante"

    return texte

def achat(message):
    if message.author not in info_de_partie[num_team(message)]["achats_autorisés"]:
        return "Les achats sont autorisés en ville uniquement."

    else:
        marchandise = message.content.split(":")
        
        if len(marchandise) == 1 or marchandise[1] == "":
            texte = "Pafait, quel est le nom exact de cet objet que vous souhaitez acheter ?\n"
            texte += "> !achat:nom précis de l'objet"
        else:
            objet = marchandise[1].strip(" ")
            objet = objet.lower()
            texte = ""

            for i in range(len(armes_armures)):
                for k, v in armes_armures[i].items():
                    if objet == k:
                        texte += "C'est en effet une pièce magnifique"

                        if argent(message) - v[-1] >= 0 :
                            texte += ".\n" + str(argent(message)) + " - " + str(v[-1]) + " = "
                            info_de_partie[num_team(message)][message.author][10] -= v[-1]
                            texte += str(argent(message))
                            texte += "\nEt elle est maintenant à vous. Bonne journée"
                            sac(message).append(k)
                        
                        else:
                            texte += " mais visiblement, vous n'avez pas de quoi vous l'offrir pour l'instant."

            if texte == "":
                texte += "Hum... non ça ne me dit rien."

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
    "\nCette commande te renvoie en message privé. C'est une commande."

    "\n\n```!rejoindre:NUM TEAM"
    "\nCommunique cette commande aux joueurs que tu souhaite inviter dans la partie."
    "\nTous les joueurs/ toutes les joueuses doivent m'envoyer cette commande en message privé."
    "\nTu seras ensuite invité à rejoindre le canal dédié à la partie pour générer ton personnage."

    "\n\n```!pj```"
    "Tu peux personnaliser ton personnage:"
    "```!pj, prénom=Clio, classe=druide, genre=androgyne```"
    "```!pj, prénom=Prune```"
    "```!pj, genre=masculin```"
    
    "\n\nTous les joueurs doivent enregistrer leur personnage."
    "\nJe génère moi même la commande de sauvegarde, il suffit de la copier-coller et valider !"

    "\n\n```!qui```"
    'Permet de vérifer que ton perso est bien "enregistré".'
    "\nDans cet exemple 0 est le numéro de team."           
    ]
    return texte[0]


def texte_nouvelle_partie(message):
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
        texte = "La commande :```!nouvelle partie```doit être tapée dans le canal ou va se jouer la partie.\n"

    return texte


def texte_rejoindre(message):
    cmd = message.content.split(":")

    pseudo_player = message.author

    try:     
        team = int(cmd[1])
        #le message.author du joueur est associé à sa team.
        team_des_joueurs[message.author] = team
        texte = message.author.name + " Tu as bien rejoins la team n°" + str(team_des_joueurs[message.author])
        texte += ".\nLe canal écrit discord autorisé pour cette partie est : "
        texte += info_de_partie[team]["allowed_channel"]

        texte += "\n\nJe t'invite à t'y rendre pour générer ton personnage :"
        texte += "```!pj```"

    except ValueError:
        texte = "Il me faut un numéro de team."
    except IndexError:
        texte = "Ce numéro de team n'est pas bon."

    return texte


def texte_joue(message):
    """
    On envoie le personnage dans la liste info_de_partie.
    Cette liste contient des dictionnaires.
    Le dictionnaire à l'indice 0 est attribué à la team n°0.

    On envoie le message.author du joueur dans team_des_joueurs.
    C'est un dictionnaire qui associe pseudo et n° de team.

    nom_joueur_id : ["nom_perso",F,Co,D,I,S,Ch,def,PV_max,PV,PA,xp,classe,genre,don,[sac],[équipé]]
    """

    #les paramètres sont séparés par le symbole :
    if message.author not in team_des_joueurs:
        return "Tu dois d'abord rejoindre une team."

    cmd = message.content.split(":")

    if len(cmd) != 4:
        return "Cette commande n'est pas valide."
    
    team = num_team(message)

    nom_perso = cmd[1]
    carac = cmd[2].split(",")
    autre = cmd[3].split(",")

    # le message.author du joueur est associé à son nom de personnage.
    info_de_partie[team][message.author] = [nom_perso]

       #On associe le nom du perso à ses carac et classe.
    for i in range(len(carac)):
        info_de_partie[team][message.author].append(int(carac[i]))
    
    for i in range(len(autre)):
        info_de_partie[team][message.author].append(autre[i])

    info_de_partie[team][message.author].append([])
    info_de_partie[team][message.author].append([])
    
    info_de_partie[team]["achats_autorisés"].append(message.author)

    #Confirmation de succés.
    texte = "Compris " + message.author.name + ", tu joues " + info_de_partie[team][message.author][0] + "."
    texte += "\nTu peux regarder ton personnage à tous moments :"
    texte += "```!qui```\n\n"
    texte += "Bienvenue en ville, que dirais-tu d'en profiter pour acheter de l'équipement ?"
    texte += "\nRends toi à la boutique d'armes la plus proche :"
    texte += "\n```!armes```"

    return texte


def texte_qui(message):
    if message.author in team_des_joueurs:
        player = False

        genre_perso = genre(message)

        if genre_perso == "masculin":
            determinant = "un"
            pronom = "il"           
        elif genre_perso == "féminin":
            determinant = "une"
            pronom = "elle"
        else:
            determinant = "un.e"
            pronom = "iel"

        sac = texte_possessions(message, "sac")
        equipement = texte_possessions(message, "equipement")

        texte = "Tu joues " + nom_perso(message).capitalize()
        texte += ", " + determinant + " " + perso_classe(message) + " :\n"
        texte += "Force : " +  str(force(message)) + "\n"
        texte += "Constitution : " + str(constitution(message)) + "\n"
        texte += "Dextérité : " + str(dexterite(message)) + "\n"
        texte += "Intelligence : " + str(intelligence(message)) + "\n"
        texte += "Sagesse : " + str(sagesse(message)) + "\n"
        texte += "Charisme : " + str(charisme(message)) + "\n"

        texte += "\n" + pronom.capitalize() + " a " + str(pv(message)) + " PV sur un maximum de "
        texte += str(vie_max(message)) + "  et " + str(argent(message)) + " PA en poche.\n"
        texte += pronom.capitalize() + " a " + str(xp(message)) + " points d'expérience.\n"
        texte += nom_perso(message).capitalize() + " a la capacité " + don(message) + ".\n"
        texte += pronom.capitalize() + " a " + str(defense(message)) + " en défense.\n"
        texte += "Son sac contient : " + sac + "et " + pronom + " porte : " + equipement

        if equipement == "rien " and sac != "rien ":
            texte += "\n\n*Tu dois t'équiper de ton armure pour bénéficier de son bonus :*\n"
            texte += "> !équiper:armure de cuir"
        
        elif equipement != "rien ":
            texte += "\n*Tu peux déséquiper ton armure :*\n"
            texte += "> !déséquiper:armure de cuir"

    else:
        texte = message.author.name + ", tu n'as pas encore de personnage enregistré."
        texte += "\n> !aide"

    return texte

def equiper(message):
    objet = message.content.split(":")
 
    if len(objet) == 1 or objet[1] == "":
        texte = "Que veux tu équiper ?\n"
        texte += "> !équiper:nom précis de l'objet"
    else:
        objet = objet[1].strip(" ")
        objet = objet.lower()
        texte = ""

        if objet not in sac(message):
            texte += "Tu ne possède pas cet objet : " + objet + "."

        elif objet not in armes_armures[2]:
            texte += "Cet objet : " + objet + " n'est pas une armure."
        
        elif len(equipement(message)) > 0 :
            texte += "Tu porte déjà une armure. Pour déséquiper un objet :\n"
            texte += "> !déséquiper:armure de cuir"
       
        else:
            sac(message).remove(objet)
            equipement(message).append(objet)
            texte += "Tu as équipé : " + objet + "."
            
    return texte


def desequiper(message):
    objet = message.content.split(":")
 
    if len(objet) == 1 or objet[1] == "":
        texte = "Que veux tu déséquiper ?\n"
        texte += "> !déséquiper:nom précis de l'objet"
    else:
        objet = objet[1].strip(" ")
        objet = objet.lower()
        texte = ""

        if objet not in equipement(message):
            texte += "Tu n'as pas équipé cet objet : " + objet + "."

        else:
            equipement(message).remove(objet)
            sac(message).append(objet)
            texte += "Tu as déséquipé : " + objet + "."
            
    return texte

def texte_possessions(message, indice):
    if indice == "sac" :
        objet = sac(message)
    elif indice == "equipement":
        objet = equipement(message)

    if objet == []:
        texte = "rien "
    else:
        texte = ""
        for i in range(len(objet)):
            texte += "\n- " + objet[i]
        texte += "\n"

    return texte

def texte_pj(message):
    pj = Personnage()
    pj.set_cmd_texte(message)
    pj.set_param_identite()
    pj.set_particularites()
    pj.stat_prioritaire_de_classe()
    pj.set_points_de_vie_maximum()
    
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
