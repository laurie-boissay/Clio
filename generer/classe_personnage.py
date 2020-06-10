from random import randrange
from collection_de_mots.personnage import *

class Personnage:
	"""
	Définit les caractéristiques et attributs d'un PJ d'après 
	les paramètres saisits par l'utilisateur.

	Associe les informations pour créer un texte d'ambiance décrivant
	le personnage et la commande pour l'enregistrer.

	Renvoie le texte et la commande.
	"""

	def __init__(self):
		"""
		caractéristiques des personnages.
		"""
		self.cmd_texte = ""

		self.total_points = 12
		self.valeur_max = 3

		self.prenom = ""
		self.genre = ""
		self.pronom = ""
		self.team = "ERREUR"

		self.classe = ""
		self.arme_distance = ""
		self.arme_cac = ""
		self.armure = 0

		self.carac = {
			"Force" : 0,
			"Constitution" : 0,
			"Dextérité" : 0,
			"Intelligence" : 0,
			"Sagesse" : 0,
			"Charisme" : 0,
			}

		self.commande_pj = "\n> !pj, "
		self.commande_save = "\n> !joue"

	def set_cmd_texte(self, message):
		"""
		Découpe la saisie de l'utilisateur en paramètres utilisables
		et les index dans cmd_text.

		Les attributs proscrits, les attributs et Les caractéristiques
		commencent à patir de l'indice 1.
		"""
		self.cmd_texte = list(message.content.split(","))
		for i in range(1, len(self.cmd_texte), 1):
			self.cmd_texte[i] = self.cmd_texte[i].strip(" ")

	def set_param_identite(self):
		"""
		Découpe chaque paramètre en couple attribut + valeur.

		Lorsqu'un attribut a été définit par l'utilisateur,
		la valeur lui correspondant est enregistrée. 
		"""
		for i in range(1, len(self.cmd_texte), 1):
			couple = self.cmd_texte[i].split("=")
			couple[0] = couple[0].strip(" ")
			couple[1] = couple[1].strip(" ")
			if couple[0] == "prénom":
				self.prenom = couple[1]
			elif couple[0] == "genre":
				self.genre = couple[1].lower()
			elif couple[0] == "classe":
				self.classe = couple[1].lower()
			elif couple[0] == "team":
				self.team = couple[1]
			

	def set_particularites(self):
		"""
		Pour chaque attribut vide, on génère une valeur.

		Les valeurs des attributs générés sont enregistrées.

		Un pronom est définit en fonction du genre du personnage.
		"""
		if self.genre == "":
			self.genre = genre[randrange(len(genre))]

		if self.classe == "":
			if self.genre == "androgyne":
				self.classe = classe[randrange(len(classe))]
			elif self.genre == "féminin":
				self.classe = classe_f[randrange(len(classe_f))]
			else:
				self.classe = classe_m[randrange(len(classe_m))]

		if self.prenom == "":
			if self.genre == "féminin":
				self.prenom = prenoms_f[randrange(len(prenoms_f))]
			elif self.genre == "masculin":
				self.prenom = prenoms_m[randrange(len(prenoms_m))]
			else:
				self.prenom = prenoms_a[randrange(len(prenoms_a))]

		elif self.genre == "masculin":
			self.pronom = "Il"

		elif self.genre == "féminin":
			self.pronom = "Elle"

		else:
			self.pronom = "Iel"


	def bonus_de_metier(self):
		"""
		Cette fonction doit définir quelle est sa caractéristique prioritaire.

		La classe est comparée au dictionnaire : classes_et_carac_associee.

		"""
		points_distribues = 0
		
		nb_points = randrange(1, self.valeur_max)

		for k, v in classes_et_carac_associee.items():
			if self.classe == k:				
				self.carac[v] += nb_points
				points_distribues += nb_points

		while points_distribues < self.total_points:
			self.ajoute_1_dans_carac()
			points_distribues += 1


	def ajoute_1_dans_carac(self):
		"""
		Ajoute 1 point dans une caractéristique aléatoire si valeur_max
		n'est pas atteinte.

		Si valeur_max est déjà atteinte, la fonction boucle sur elle même.
		"""	
		
		j = carac[randrange(len(carac))]

		if self.carac[j] < self.valeur_max:
			self.carac[j] += 1
		else:
			self.ajoute_1_dans_carac()


	def set_commande_pj(self):
		commande = "prénom=" + self.prenom + ", "
		commande += "classe=" + self.classe + ", "
		commande += "genre=" + self.genre + ", "
		commande += "team=" + self.team 
		self.commande_pj += commande


	def set_commande_save(self):
		commande = ":" + self.prenom
		commande += ":" + self.team + ":"

		commande += str(self.carac["Force"]) + ","
		commande += str(self.carac["Constitution"]) + ","
		commande += str(self.carac["Dextérité"]) + ","
		commande += str(self.carac["Intelligence"]) + ","
		commande += str(self.carac["Sagesse"]) + ","
		commande += str(self.carac["Charisme"]) + ","
		commande += self.classe

		self.commande_save += commande
		

	def afficher_personnage(self):
		"""
		Mets en forme le texte qui sera renvoyé.

		Si le type de personnage est PJ, génère l'atout du PJ et l'ajoute
		au texte.

		Massage de Calliope + Attributs (+ Atout) + Caractéristiques.
		"""
		text_a_afficher = ""
		text = [
		"J'ai façonné un personnage qui pourrait correspondre à tes attentes :\n"

		"\nPrénom : " , self.prenom,
		"\nGenre : " , self.genre,
		"\nClasse : " , self.classe,
		"\n\n"
		]

		for k in self.carac.keys():
			text += k + " : " + str(self.carac[k]) + "\n"

		for i in range(len(text)):
			text_a_afficher += text[i]

		self.set_commande_pj()
		self.set_commande_save()

		text_a_afficher += "\n\n"
		text_a_afficher += "```!classes```Affiche les classes qui donnent une carractéristique prioritaire.\n"
		text_a_afficher += "```!genres```Affiche les genres qui influencent le prénom.\n"
		text_a_afficher += "\n\n*Personnalise ton personnage :*\n"
		text_a_afficher += "*(Tu peux laisser certains paramètres vides mais pas le n° de team.)*\n"
		text_a_afficher += self.commande_pj

		text_a_afficher += "\n\n*Sauvegarde ton personnage :*\n"
		text_a_afficher += self.commande_save

		return text_a_afficher

