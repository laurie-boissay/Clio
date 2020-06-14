
from random import randrange


from collection_info.save_game import *

from generer.personnage import *
from generer.quete import *

from collection_de_mots.quetes import *
from generer.classe_quete import Quete



def texte_quete(message):
    """
    génère un menu de quête.

    Si les joueurs ne sont pas en ville, renvoie un message d'erreur/aide.
    """
    texte = ""
    #if message.author not in info_de_partie[num_team(message)]["achats_autorisés"]:
        #texte = "Vous n'êtes pas en ville actuellement."

    #else:
        #text = "Vous êtes dans la ville de " # + nom_ville() + "."

    texte += "Vous êtes prêt.e.s à partir à l'aventure et vous cherchez à vous occuper.\n"
    texte += "choisissez :\n\n"

    texte += "Vous rodez dans les petites ruelles sombres de la ville :\n> !roder\n\n"
    texte += "Vous cherchez une taverne pour vous renseignez, écouter les rumeurs :\n> !taverne\n\n"
    texte += "Vous explorer la ville à la recherche d'un tableau annonces :\n> !tableau\n\n"
    texte += "Vous coller des annonces sur les murs de la ville pour vous faire connaître :\n> !annonces\n\n"
    texte += "Vous vous renseignez sur les primes :\n> !primes\n\n"

    return texte


def texte_roder(message):
    quete = Quete()
    quete.set_commanditaire_exclu(la_ligue_de_la_lumiere)
    commanditaire = quete.get_commanditaire()
    contexte_pioche = contexte_quetes_illegales[randrange(len(contexte_quetes_illegales))]
    texte = phrases_contexte(contexte_pioche, commanditaire)

    return texte


def texte_taverne(message):
    quete = Quete()
    quete.set_commanditaire_exclu(la_ligue_de_l_ombre)
    commanditaire = quete.get_commanditaire()
    texte = phrases_contexte("tavernier", commanditaire)

    return texte


def texte_tableau(message):
    quete = Quete()
    quete.set_commanditaire_exclu(la_ligue_de_l_ombre)  
    commanditaire = quete.get_commanditaire()
    texte = phrases_contexte("annonce", commanditaire)
    
    return texte


def texte_annonces(message):
    quete = Quete()
    quete.set_commanditaire_exclu(la_ligue_de_l_ombre)
    commanditaire = quete.get_commanditaire()
    texte = phrases_contexte("accostés", commanditaire)
    
    return texte


def texte_primes(message):
    quete = Quete()
    texte = phrases_contexte("prime", "La caserne")
    
    return texte

