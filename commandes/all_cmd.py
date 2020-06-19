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
            # Créer une nouvelle partie, renvoie un texte
            texte = texte_initialiser(message)
            canal = message.author

        elif message.content.startswith('!rejoindre'):
            # La personne envoie message.author et un n° de team dans la liste team_des_joueurs.
            # Renvoie un texte.
            texte = texte_rejoindre(message)
            canal = message.author

        elif message.content.startswith('!pj'):
            # Génère un PJ, renvoi un texte.
            texte = texte_pj(message)
            canal = message.author

        elif message.content.startswith('!info'):
            # Renvoie le lien vers mon Github.
            texte = texte_info()
            canal = message.author

        elif message.content.startswith('!classes'):
            # Renvoie un texte : la liste des classes et la caractéristique prio associée.
            texte = texte_classes()
            canal = message.author

        elif message.content.startswith('!genres'):
                # Renvoie la liste des genres qui influencent la génération d'un prénom.
                texte = texte_genres()
                canal = message.author

        elif message.content.startswith('!races'):
                # Renvoie la liste des genres qui influencent la génération d'un prénom.
                texte = texte_races()
                canal = message.author

        elif message.content.startswith('!dons'):
            # Renvoie la liste des dons.
            texte = texte_dons(message)
            canal = message.author

        elif message.content.startswith('!qui') and len(message.content) == 4:
            # Renvoie un résumé d personnage.
            texte = texte_qui(message)
            canal = message.author

        elif message.author in team_des_joueurs:
            # Seulement si la personne a rejoint une partie :

            if message.content.startswith('!armes'):
                # Renvoie la liste des armes par mots clés.
                texte = boutique_d_armes(message)
                canal = message.author

            elif message.content.startswith('!achat'):
                # Le personnage obtient un objet, perd de l'argent.
                texte = achat(message)
                canal = message.author

            elif message.content.startswith('!équiper'):
                # Le personnage s'équipe d'une pièce d'armure.
                texte = equiper(message)
                canal = message.author

            elif message.content.startswith('!déséquiper'):
                # Le personnage déséquipe d'une pièce d'armure.
                texte = desequiper(message)
                canal = message.author
            
            elif message.content.startswith('!joue'):
                # La personne enregistre son personnage dans info_de_partie.
                texte = texte_joue(message)
                texte = bon_canal(message, texte)

            elif message.content.startswith('!quête'):
                # Génère une quête et la stock dans info_de_partie.
                texte = texte_quete(message)
                texte = bon_canal(message, texte)

            elif message.content.startswith('!refuser'):
                # Efface la quête de info_de_partie.
                texte = texte_refuser(message)
                texte = bon_canal(message, texte)

            elif message.content.startswith('!accepter'):
                # Ajoute la personne à la liste des joueurs/joueuses participant à la quête.
                texte = texte_accepter(message)
                texte = bon_canal(message, texte)

            elif message.content.startswith('!téléporter'):
                # Le groupe participant à la quête ne peut plus faire d'achat, lance le combat.
                texte = texte_teleporter(message)
                texte = bon_canal(message, texte)

            elif message.content.startswith('!quitter'):
                # Retire le personnage de la liste des participants à la quête, achat autorisé.
                texte = texte_quitter(message)
                texte = bon_canal(message, texte)

            elif message.content.startswith('!journal'):
                # Affiche une description de la quête en cours.
                texte = texte_journal(message)
                texte = bon_canal(message, texte)

            elif message.content.strip("!").lower() in armes_2_mains:
                # Le personnage utilise une arme à deux mains.
                texte = attaque_arme(message, "deux mains")
                texte = bon_canal(message, texte)

            elif message.content.strip("!").lower() in armes_1_main:
                # Le personnage utilise une arme à une main.
                texte = attaque_arme(message, "une main")
                texte = bon_canal(message, texte)
            
                
    return canal, texte




