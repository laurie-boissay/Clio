"""
Les commandes du personnage.
"""


from collection_de_mots.equipement import *

from generer.personnage import *

def texte_joue(message):
    """
    Vérifie que le joueur/ la joueuse a bien rejoint une partie.
        si non, renvoie un texte d'erreur.

    Cette fonction reçoit cette commande qui représente un personnage :
    !joue:Gell:3,1,3,3,1,1,10,11,11,100,0:paladin.e,androgyne,don

    Elle sépare le texte au niveau du symbole :

    Vérifie qu'il y a bien 4 parties.
        si non, renvoie un texte d'erreur.

    la partie[0] ne sert qu'a appeler la fonction ;
    la partie[1] est le nom du personnage ;
    la partie[2] concerne les entiers ;
    la partie[3] les autres caractéristiques du personnage.

    le message.author est associé au nom du perso.
        si la partie n'a pas été créée, renvoie un texte d'erreur.

    Envoie le personnage dans la liste info_de_partie.
    Cette liste contient des dictionnaires.
    Le dictionnaire à l'indice 0 est attribué à la team n°0.
    l'entrée nom_joueur_id du dictionnaire correspondant contient une liste :

    ["nom_perso",F,Co,D,I,S,Ch,def,PV_max,PV,PA,xp,classe,genre,don,[sac],[équipé]]

    Autorise message.author a faire des achats.

    texte de confirmation/aide.

    Renvoie le texte.
    """

    #les paramètres sont séparés par le symbole :
    if message.author not in team_des_joueurs:
        return "Tu dois d'abord rejoindre une team."

    cmd = message.content.split(":")

    if len(cmd) != 4:
        return "Cette commande n'est pas valide."
    
    team = num_team(message)

    nom_personnage = cmd[1]
    carac = cmd[2].split(",")
    autre = cmd[3].split(",")

    # le message.author du joueur est associé à son nom de personnage.
    try:
        info_de_partie[team][message.author] = [nom_personnage]

    except IndexError:
        return "Il faut d'abord créer une partie."

       #On associe le nom du perso à ses carac et classe.
    for i in range(len(carac)):
        info_de_partie[team][message.author].append(int(carac[i]))
    
    for i in range(len(autre)):
        info_de_partie[team][message.author].append(autre[i])

    info_de_partie[team][message.author].append([])
    info_de_partie[team][message.author].append([])
    
    info_de_partie[team]["achats_autorisés"].append(message.author)

    #Confirmation de succés.
    texte = "Compris " + message.author.name + ", tu joues " + nom_perso(message) + "."
    texte += "\nTu peux regarder ton personnage à tous moments :"
    texte += "```!qui```\n\n"
    texte += "Bienvenue en ville, que dirais-tu d'en profiter pour acheter de l'équipement ?"
    texte += "\nRends toi à la boutique d'armes la plus proche :"
    texte += "\n```!armes```"

    return texte


def texte_qui(message):
    """
    Renvoie un texte avec toutes les particularités du personnage
    + conseils et aide.
    Personnalise le texte en fonction du genre du personnage.
    """
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


def achat(message):
    """
    Vérifie si le joueur est autorisé a acheter.
        si non, renvoie un texte négatif.
        si oui, vérifie que la demande d'achat précise un objet.
            si non, demande une précision avec un texte d'aide.
            si oui, vérifie que l'objet existe.
                si non, signale que l'objet n'existe pas.
                si oui, vérifie que le personnage a assez d'argent pour payer.
                    si non, renvoie un texte négatif.
                    si oui :
                        - retranche la somme d'argent
                        - ajoute l'objet dans le sac du personnage
                        - signale que la transaction s'est bien passée.
    renvoie le texte.
    """
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
                            modifier_argent(message, -v[-1])
                            texte += str(argent(message))
                            texte += "\nEt elle est maintenant à vous. Bonne journée"
                            sac(message).append(k)
                        
                        else:
                            texte += " mais visiblement, vous n'avez pas de quoi vous l'offrir pour l'instant."

            if texte == "":
                texte += "Hum... non ça ne me dit rien."

    return texte
    

def equiper(message):
    """
    Vérifie que l'objet à équiper est précisé.
        si non, demande une précision.
    Vérifie que l'objet à équipé est bien dans la liste sac.
        si non signale l'erreur.
    Vérifie que la liste équipement contient moins de 4 objets.
        si non, signale l'erreur.
        si oui :
            l'objet est supprimé de la liste sac ;
            l'objet est ajouté à la liste équipement.
    Renvoie le texte.
    """
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
        
        elif len(equipement(message)) > 2 :
            texte += "Tu porte déjà 3 pièces d'armure. Pour déséquiper un objet :\n"
            texte += "> !déséquiper:armure de cuir"
       
        else:
            appliquer_stat_armure(message, objet, "+")
            sac(message).remove(objet)
            equipement(message).append(objet)
            texte += "Tu as équipé : " + objet + "."
            
    return texte


def desequiper(message):
    """
    Vérifie que l'objet à déséquiper est précisé.
        si non, demande une précision.
    Vérifie que l'objet à déséquipé est bien équipé.
        si non signale l'erreur.
        si oui, l'objet est supprimé de la liste équipement et
        l'objet est ajouté à la liste sac.
        texte de confirmation.
    Renvoie le texte.
    """
    objet = message.content.split(":")
 
    if len(objet) == 1 or objet[1] == "":
        texte = "Que veux tu déséquiper ?\n"
        texte += "> !déséquiper:nom précis de l'objet"
    else:
        objet = objet[1].strip(" ").lower()
        texte = ""

        if objet not in equipement(message):
            texte += "Cet objet n'es pas équipé : " + objet + "."

        else:
            appliquer_stat_armure(message, objet, "-")
            equipement(message).remove(objet)
            sac(message).append(objet)
            texte += "Tu as déséquipé : " + objet + "."
            
    return texte
