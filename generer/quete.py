from generer.classe_quete import Quete
from generer.personnage import *
from generer.nom import *
from generer.combat import *



from collection_info.save_game import *

from collection_de_mots.noms import *




def butin(message):
	# Renvoie la liste du butin (texte).
	return info_de_partie[num_team(message)]["quête en cours"]["butin"]


def objectif(message):
	# Renvoie l'objectif (texte).
	return info_de_partie[num_team(message)]["quête en cours"]["objectif"]


def titre(message):
	# Renvoie le titre de a quête (texte).
	return info_de_partie[num_team(message)]["quête en cours"]["titre"]


def generer_donjon(message):
	"""
	Créer une liste vide de joueurs prenant part au combat.
	Créer une liste vide de butin.

	Génère une esquisse de boss et stocke ces info dans un dictionnaire.
	
	Appele la fonction qui génère un objectif de quête.
	Stock l'objectif de quête.
	
	Appele la fonction qui génère la difficulté du donjon.
	Stock la difficulté du donjon.

	Appele la fonction qui génère un titre de donjon.
	Stock le titre de donjon.

	Appele la fonction qui génère la déscription de la quête.

	Renvoie un texte descriptif de la quête.
	"""

	info_de_partie[num_team(message)]["quête en cours"]["players"] = []
	info_de_partie[num_team(message)]["quête en cours"]["butin"] = []

	quete = Quete()
	boss = quete.set_boss()
	info_de_partie[num_team(message)]["quête en cours"]["boss"] = boss
	
	info_de_partie[num_team(message)]["quête en cours"]["objectif"] = objet_precieux()
	
	quete.difficulte_generale()
	info_de_partie[num_team(message)]["quête en cours"]["difficulté"] = quete.get_difficulte_generale()

	info_de_partie[num_team(message)]["quête en cours"]["titre"] = titre_donjon(message)
	
	texte = "**" + titre(message) + " :**\n\n"
	texte += description_donjon(message)

	return texte
    
    
def titre_donjon(message):
	"""
	Génère le titre du donjon.
	"""
	
	lieu = lieu_quete_nom[randrange(len(lieu_quete_nom))]
	adj_boss = boss_adj[randrange(len(boss_adj))]

	if boss(message)["genre"] == "féminin" :
		boss_determinant = "de la"
	elif boss(message)["genre"] == "masculin" :
		boss_determinant = "du"
	else:
		boss_determinant = "du/ de la"

	titre_donjon = lieu.capitalize() + " " + boss_determinant + " " + boss(message)["classe"] + " " + adj_boss

	return titre_donjon


def description_donjon(message):
	"""
	Génère la description du donjon.
	"""	
	texte = "Vous devez pénétrer dans " + titre(message) + " et affronter "
	texte += boss(message)["prénom"] + " " + boss(message)["nom"] + ".\n"
	texte += objectif_donjon(message) + "\n\n"
	texte += "Difficulté de la quête : " + difficulte(message)["niveau"] + ".\nIl y a "
	texte += str(difficulte(message)["nb salles"]) + " salles à explorer.\nLa récompense pour ramener "
	texte += objectif(message)
	texte += " est de " + str(difficulte(message)["récompense"]) + " PA par personne."
	
	return texte
	

def objectif_donjon(message):
	"""
	Génère un texte qui décrit l'objectif.
	"""
	texte = boss(message)["pronom"] + " détient " + objectif(message) + ". Il faut lui reprendre."

	return texte