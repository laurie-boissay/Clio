from commandes.personnages import *
from commandes.combats import *
from commandes.guide_aide import *
from commandes.quete import *


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
            canal = message.author

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
                canal = message.author

        elif message.content.startswith('!races'):
                # Renvoi la liste des genres qui influencent la génération d'un prénom.
                texte = texte_races()
                canal = message.author

        elif message.content.startswith('!dons'):
            texte = texte_dons(message)
            canal = message.author

        elif message.content.startswith('!qui') and len(message.content) == 4:
            texte = texte_qui(message)
            canal = message.author

        elif message.author in team_des_joueurs:

            if message.content.startswith('!armes'):
                texte = boutique_d_armes(message)
                canal = message.author

            elif message.content.startswith('!achat'):
                texte = achat(message)
                canal = message.author

            elif message.content.startswith('!équiper'):
                texte = equiper(message)
                canal = message.author

            elif message.content.startswith('!déséquiper'):
                texte = desequiper(message)
                canal = message.author
            
            elif message.content.startswith('!joue'):
                texte = texte_joue(message)
                texte = bon_canal(message, texte)

            elif message.content.startswith('!quête'):
                texte = texte_quete(message)
                texte = bon_canal(message, texte)

            elif message.content.startswith('!refuser'):
                texte = texte_refuser(message)
                texte = bon_canal(message, texte)

            elif message.content.startswith('!accepter'):
                texte = texte_accepter(message)
                texte = bon_canal(message, texte)

            elif message.content.startswith('!téléporter'):
                texte = texte_teleporter(message)
                texte = bon_canal(message, texte)

            elif message.content.startswith('!quitter'):
                texte = texte_quitter(message)
                texte = bon_canal(message, texte)

            elif message.content.startswith('!journal'):
                texte = texte_journal(message)
                texte = bon_canal(message, texte)

            elif message.content.strip("!").lower() in armes_2_mains:
                texte = attaque_arme(message, "deux mains")
                texte = bon_canal(message, texte)

            elif message.content.strip("!").lower() in armes_1_main:
                texte = attaque_arme(message, "une main")
                texte = bon_canal(message, texte)
            
                
    return canal, texte
















