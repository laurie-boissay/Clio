from collection_info.save_game import *

from generer.personnage import *
from generer.quete import *



def texte_quete(message):
    refuser = "\n\n*Pour refuser cette quête et la rendre indisponible :*\n> !refuser"

    participer = "\n\n*Pour prendre part au combat :*\n> !accepter"

    téléporter = "\n\n*Pour téléporter le groupe dans le donjon :*\n> !téléporter"

    if len(info_de_partie[num_team(message)]["quête en cours"]) > 0 :
        texte = "Vous avez déjà une quête en cours :\n"
        texte += info_de_partie[num_team(message)]["quête en cours"]["Titre"]
        texte += refuser + participer + téléporter

        return texte

    generer_donjon(message)

    texte = info_de_partie[num_team(message)]["quête en cours"]["Titre"] + "\n\n"
    texte += info_de_partie[num_team(message)]["quête en cours"]["Description"]
    texte += refuser + participer + téléporter

    return texte


def texte_refuser(message):
    if len(info_de_partie[num_team(message)]["quête en cours"]) == 0:
        return "Vous n'avez pas de quête en cours."

    if len(info_de_partie[num_team(message)]["quête en cours"]["players"]) > 0:
        texte = "Vous ne pouvez pas annuler cette quête car des membres de votre "
        texte += "équipe sont déjà dans le donjon !"
        texte += "\n\n*Pour prendre part au combat :*\n> !accepter"
        texte += "\n\n*Vous serez téléporté.e dans le donjon."
        return texte

    texte = "La quête " + info_de_partie[num_team(message)]["quête en cours"]["Titre"]
    texte += " n'est plus disponible."

    info_de_partie[num_team(message)]["quête en cours"] = {}

    return texte


def texte_accepter(message):
    if len(info_de_partie[num_team(message)]["quête en cours"]) == 0 :
        return "Vous n'avez pas de quête en cours."

    if message.author not in info_de_partie[num_team(message)]["quête en cours"]["players"]:
        info_de_partie[num_team(message)]["quête en cours"]["players"].append(message.author)

    texte = "Vous participez à la quête " + info_de_partie[num_team(message)]["quête en cours"]["Titre"] + ".\n"
    texte += "Il y a actuellement " + str(len(info_de_partie[num_team(message)]["quête en cours"]["players"]))
    texte += " joueur.s/joueuse.s qui y participe.nt."

    return texte


def texte_teleporter(message):
    if len(info_de_partie[num_team(message)]["quête en cours"]) == 0 :
        return "Vous n'avez pas de quête en cours."

    if message.author not in info_de_partie[num_team(message)]["quête en cours"]["players"]:
        return "\n\n*Pour prendre part au combat :*\n> !accepter"

    for i in range(len(info_de_partie[num_team(message)]["quête en cours"]["players"])):
        for j in range(len(info_de_partie[num_team(message)]["achats_autorisés"])):
            if info_de_partie[num_team(message)]["quête en cours"]["players"][i] == info_de_partie[num_team(message)]["achats_autorisés"][j]:
                info_de_partie[num_team(message)]["achats_autorisés"].remove(info_de_partie[num_team(message)]["quête en cours"]["players"][i])

        if info_de_partie[num_team(message)]["quête en cours"]["players"][i] not in info_de_partie[num_team(message)]["combat_autorisé"]:
            info_de_partie[num_team(message)]["combat_autorisé"].append(info_de_partie[num_team(message)]["quête en cours"]["players"][i])

    texte = "Vous êtes arrivé.e à " + info_de_partie[num_team(message)]["quête en cours"]["Titre"] + "."
    
    return texte