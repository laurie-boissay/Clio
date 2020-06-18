from collection_info.save_game import *

from generer.personnage import *
from generer.quete import *
from generer.combat import *


def texte_quete(message):
    """
    Vérifie qu'il n'y a pas de quête en cours :
        si oui : message d'aide.
        si non : génère une quête.
    """
    refuser = "\n\n*Pour refuser cette quête et la rendre indisponible :*\n> !refuser"

    participer = "\n\n*Pour prendre part au combat :*\n> !accepter"

    téléporter = "\n\n*Pour téléporter le groupe dans le donjon :*\n> !téléporter"

    journal = "\n\n*Pour voir le  journal de quête :*\n> !journal"

    if len(quete_en_cours(message)) > 0 :
        texte = "Vous avez déjà une quête en cours :\n"
        texte += titre(message) + "."
        texte += refuser + participer + téléporter + journal

    else:
        info_de_partie[num_team(message)]["quête en cours"]["ennemis"] = []
        texte = generer_donjon(message)
        texte += refuser + participer + téléporter

    return texte


def texte_refuser(message):
    """
    Vérifie s'il y a une quête en cours :
        si non : texte d'erreur

    Vérifie si des joueurs ont déjà accepté la quête :
        si oui : texte d'erreur + aide.
        si non, efface la quête en cours + texte confiramtion

    Renvoie le texte.
    """
    if len(quete_en_cours(message)) == 0:
        texte = "Vous n'avez pas de quête en cours."

    elif len(players(message)) > 0:
        texte = "Vous ne pouvez pas annuler cette quête car des membres de votre "
        texte += "équipe l'ont déjà acceptée !"
        texte += "\n\n*Pour prendre part au combat :*\n> !accepter"

    else:
        texte = "La quête " + titre(message)
        texte += " n'est plus disponible."

        info_de_partie[num_team(message)]["quête en cours"] = {}

    return texte


def texte_accepter(message):
    """
    Vérifie s'il y a une quête en cours :
        si non : Renvoie un texte d'erreur

    Vérifie si je joueur/ la joueuse a déjà accepté la quête.
        si non, l'ajoute à la liste.

    Renvoie un texte de confirmation indiquant le nombre de personnes
    dans la liste des participants.
    """

    if len(info_de_partie[num_team(message)]["quête en cours"]) == 0 :
        return "Vous n'avez pas de quête en cours."

    if message.author not in players(message):
        info_de_partie[num_team(message)]["quête en cours"]["players"].append(message.author)

    texte = "Vous participez à la quête " + titre(message) + ".\n"
    texte += "Il y a actuellement " + str(len(players(message)))
    texte += " joueur.s/joueuse.s qui y participe.nt."

    return texte


def texte_quitter(message):
    """
    Vérifie s'il y a une quête en cours :
        si non : Renvoie un texte d'erreur

    Vérifie si la personne est dans la liste des participants:
        si oui : retire la personne de la liste.

    Vérifie si la personne est dans la liste autorisant le combat:
        si oui : retire la personne de la liste.

    Vérifie si la personne est dans la liste autorisant les achat:
        si non : ajoute la personne à la liste.

    Renvoie un texte de confirmation.
    """
    if len(quete_en_cours(message)) == 0 :
        return "Vous n'avez pas de quête en cours."

    if message.author in players(message):
        info_de_partie[num_team(message)]["quête en cours"]["players"].remove(message.author)

    if message.author in combat(message):
        info_de_partie[num_team(message)]["combat_autorisé"].remove(message.author)

    if message.author not in achats(message):
        info_de_partie[num_team(message)]["achats_autorisés"].append(message.author)

    texte = "Vous êtes en ville."

    return texte


def texte_journal(message):
    """
    Vérifie s'il y a une quête en cours :
        si non : Renvoie un texte d'erreur
        si oui : Renvoie la description de la quête en cours + texte aide.
    """
    if len(quete_en_cours(message)) == 0 :
        return "Vous n'avez pas de quête en cours."

    else:
        texte = description_donjon(message)
        texte += "\n\n*Pour refuser cette quête et la rendre indisponible :*\n> !refuser"
        texte += "\n\n*Pour prendre part au combat :*\n> !accepter"
        texte += "\n\n*Pour téléporter le groupe dans le donjon ou pour vous téléporter dans le"
        texte += " donjon et rejoindre le groupe :*\n> !téléporter"

    return texte


def texte_teleporter(message):
    """
    Vérifie s'il y a une quête en cours :
        si non : Renvoie un texte d'erreur

    Vérifie si la personne est dans la liste des participants au combat :
        si non : renvoie un texte d'aide.

    Vérifie si tous les membres du groupe ont un personnage.
        Si non : renvoie un texte d'erreur.

    Chaque personne dans la liste des participants est retirée de la liste
    autorisant les achats.

    Appele la fonction generer_ennemis

    Renvoie un texte de confirmation
    + description ennemis
    + aide
    """
    if len(quete_en_cours(message)) == 0 :
        return "Vous n'avez pas de quête en cours."

    if message.author not in players(message):
        return "\n\n*Pour prendre part au combat :*\n> !accepter"

    texte = "Membres du groupe présent.e.s dans " + titre(message) + " :\n"
    for i in range(len(players(message))):
        try:
            texte += "- " + find_player_charac_name(message, players(message)[i]) + "\n"
        except TypeError:
            texte = "Un.e des membres du groupe n'a pas de personnage : " + players(message)[i].name
            texte += "\n*Pour créer un personnage :*\n> !pj"
            return texte

    for i in range(len(players(message))):
        for j in range(len(achats(message))):
            if players(message)[i] == achats(message)[j]:
                info_de_partie[num_team(message)]["achats_autorisés"].remove(players(message)[i])

    if len(ennemis_dans_salle(message)) == 0:
       generer_ennemis(message)

    texte += "\n" + texte_decrivant_ennemis(message)

    texte += "\n\n*Pour quitter le donjon :*\n> !quitter"

    return texte