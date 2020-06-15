from commandes.personnages import *
from commandes.combats import *
from commandes.guide_aide import *
from commandes.quetes import *

from generer.demarrage import *
from generer.personnage import *


def all_users_cmd(message, client):
    """
    Définit un canal et un texte par défaut.
        Vérifie pour chaque message tappé s'il
        s'agit d'une commande.
            Si oui, appelle la fonction appropriée
            qui peut modifier le texte.
    Renvoie le texte, le canal.
    """
    canal = message.channel
    texte = "not a cmd"

    if (message.author != client.user): # User is not Clio.
            
        if 'clio clio clio' in message.content:
            canal = message.author
            texte = ("https://raw.githubusercontent.com/laurie-boissay/Clio/master/clio__muse_of_history_by_cetrece-dcwuzqk.png")

        elif message.content.startswith('!aide'): 
            # Renvoi un message d'aide.
            texte = texte_aide()

        elif message.content.startswith('!initialiser'):
            texte = texte_initialiser(message)
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
                texte = texte_genres()

        elif message.content.startswith('!races'):
                # Renvoi la liste des genres qui influencent la génération d'un prénom.
                texte = texte_races()

        elif message.content.startswith('!dons'):
            texte = texte_dons(message)

        elif message.content.startswith('!qui'):
            texte = texte_qui(message)

        elif message.content.startswith('!quête'): # A déplacer plus bas après les tests.
                texte = texte_quete(message)

        elif message.content.startswith('!roder'): # A déplacer plus bas après les tests.
                texte = texte_roder(message)

        elif message.content.startswith('!taverne'): # A déplacer plus bas après les tests.
                texte = texte_taverne(message)

        elif message.content.startswith('!tableau'): # A déplacer plus bas après les tests.
                texte = texte_tableau(message)

        elif message.content.startswith('!annonces'): # A déplacer plus bas après les tests.
                texte = texte_annonces(message)

        elif message.content.startswith('!primes'): # A déplacer plus bas après les tests.
                texte = texte_primes(message)        

        elif message.author in team_des_joueurs:

            if message.content.startswith('!armes'):
                texte = boutique_d_armes(message)

            try :
                if message.channel.name == info_de_partie[num_team(message)]["allowed_channel"]:

                    if message.content.startswith('!joue'):
                        texte = texte_joue(message)

                    elif message.content.startswith('!achat'):
                        texte = achat(message)

                    elif message.content.startswith('!équiper'):
                        texte = equiper(message)

                    elif message.content.startswith('!déséquiper'):
                        texte = desequiper(message)

                    elif message.content.strip("!").lower() in armes_2_mains:
                        texte = attaque_arme(message, "deux mains")

                    elif message.content.strip("!").lower() in armes_1_main:
                        texte = attaque_arme(message, "une main")

            except AttributeError:
                texte = "Tu n'es pas dans le bon canal, rends toi dans : "
                texte += info_de_partie[num_team(message)]["allowed_channel"] + "."
                

                
    return canal, texte













