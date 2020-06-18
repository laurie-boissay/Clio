
from collection_de_mots.equipement import *

from collection_info.save_game import *

from generer.personnage import *



def liste_d_armes(mot_cle):
    """
    Vérifie que le mot_cle est dans la liste des armes et armures.
        si non, retourne un texte indiquant que non.
        si oui, forme un texte avec toutes les occurences.
            Vérifie si le texte n'est pas trop long pour être afficher 
            sur Discord.
                si oui, modifie le texte pour demander une précision.
    Renvoie le texte.
    """
    trouvaille = ""
    for i in range(len(armes_armures)):

        for k, v in armes_armures[i].items():
            if mot_cle in k or mot_cle in v[0] or mot_cle in v[-3] or mot_cle in v[-2] or mot_cle in str(v[-1]):
                trouvaille += "**" + k.capitalize() + " : **"
                for f in range(len(v)-3):
                    trouvaille += str(v[f][0]) + v[f][1] + v[f][2] + ".\n"
                trouvaille += "Utilisable " + v[-3] + ", " + v[-2] + " : " + str(v[-1]) + " PA.\n\n"

    if trouvaille == "":
        texte = "Ha non j'ai pas ça. J'espère quand même vous revoir, bonne journée."
    else:
        texte = "J'ai quelque chose qui pourrait bien vous intéresser !\n\n" + trouvaille
        texte += "Alors, ça vous plaît ?"
        texte += "\n> !achat:épée rutillante"

    if len(texte) > 2000:
        texte = "ça prendrait la journée à tout déballer.".capitalize()
        texte += " Essayez de me décrire ce que vous voulez."
        texte += "\n> !armes:dextérité"
        texte += "\n> !armes:25"

    return texte
    

def bon_canal(message, texte):
    """
    Vérifie que la commande de jeu tapée par la personne est tapée dans le bon canal.
        si non : texte aide.

    En cas d'erreur AttributeError la personne est dans le canal message privé de Clio.

    """
    texte_erreur = "Tu n'es pas dans le bon canal, rends toi dans : "
    texte_erreur += info_de_partie[num_team(message)]["allowed_channel"] + "."

    try :
        if message.channel.name != info_de_partie[num_team(message)]["allowed_channel"]:
            texte = texte_erreur
            
    except AttributeError:
        texte = texte_erreur

    return texte