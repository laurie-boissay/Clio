from random import randrange


from collection_de_mots.personnage import *
from collection_de_mots.equipement import *

from generer.nom import *

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
		self.type_pers = "PJ"

		self.total_points = 12
		self.valeur_max = 3

		self.prenom = ""
		self.nom = ""
		self.genre = ""
		self.race = ""
		self.pronom = ""
		self.age = ""

		self.classe = ""
		self.classe_indice = None

		self.carac = {
			"force" : 0,
			"constitution" : 0,
			"dextérité" : 0,
			"intelligence" : 0,
			"sagesse" : 0,
			"charisme" : 0,
			}

		self.defense = 10
		self.vie_max = 10
		self.arme = ""
		self.armure = []

		self.don = ""
		
		self.xp = 0
		self.argent = 100
		self.niveau = 1

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
			if len(couple) > 1:
				couple[0] = couple[0].strip(" ")
				couple[1] = couple[1].strip(" ")
				if couple[0] == "prénom":
					self.prenom = couple[1].capitalize()
				elif couple[0] == "nom":
					self.nom = couple[1].capitalize()
				elif couple[0] == "race":
					self.race = couple[1].lower()
				elif couple[0] == "genre":
					self.genre = couple[1].lower()
				elif couple[0] == "classe":
					self.classe = couple[1].lower()
				elif couple[0] == "don":
					self.don = couple[1].lower()
				elif couple[0] == "age":
					self.age = couple[1].lower()
				
	

	def set_particularites(self):
		"""
		Pour chaque attribut vide, on génère une valeur.

		Pour les PJ, on génère une classe et un indice de classe.
		Pour les PNJ, on génère un métier.

		Les valeurs des attributs générés sont enregistrées.

		Un pronom est définit en fonction du genre du personnage.
		"""
		
		self.set_genre()
		self.set_race()
		self.set_classe()
		self.set_don()
		self.set_pronom()

		if self.type_pers == "PJ":
			self.set_prenom()
			self.set_nom()
			self.set_age()


	def set_genre(self):
		if self.genre == "":
			self.genre = genre_pers[randrange(len(genre_pers))]


	def set_race(self):
		if self.race == "":
			self.race = race_pers[randrange(len(race_pers))]


	def set_age(self):
		if self.age == "":
			self.age = age_pers[randrange(len(age_pers))]


	def set_classe(self):
		if self.classe == "" or (self.classe not in classe_m and self.classe not in classe_f and self.classe not in classe):
			self.classe_indice = randrange(len(classe))
			if self.genre == "masculin":
				self.classe = classe_m[self.classe_indice]
			elif self.genre == "féminin":
				self.classe = classe_f[self.classe_indice]
			else:
				self.classe = classe[self.classe_indice]

			if self.classe_indice == None:
				for i in range(len(classe)):
					if self.genre == "féminin":
						if self.classe == classe_f[i]:
							self.classe_indice = i
					elif self.genre == "masculin":
						if self.classe == classe_m[i]:
							self.classe_indice = i
					else:
						if self.classe == classe[i]:
							self.classe_indice = i


	def set_prenom(self):
		self.prenom = prenom_pers(self.genre, self.race)


	def set_nom(self):
		self.nom = nom_pers(self.genre, self.race)


	def set_pronom(self):

		if self.genre == "masculin":
			self.pronom = "Il"

		elif self.genre == "féminin":
			self.pronom = "Elle"

		else:
			self.pronom = "Iel"


	def set_don(self):

		liste_dons_classe = []
		for i in range(len(toutes_classes)):
			for j in range(len(toutes_classes[i])):
				if self.classe == toutes_classes[i][j]:
					for k, v in dons_par_classes[j].items():
						liste_dons_classe.append(k)
		
		if self.don == "" or self.don not in liste_dons_classe:
			self.don = liste_dons_classe[randrange(len(liste_dons_classe))]

		
	def stat_prioritaire_de_classe(self):
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
		commande = "nom=" + self.nom + ", "
		commande = "race=" + self.race + ", "
		commande = "age=" + self.age + ", "
		commande += "classe=" + self.classe + ", "
		commande += "genre=" + self.genre + ", "
		commande += "don=" + self.don + ", "

		self.commande_pj += commande


	def set_commande_save(self):

		commande = ":" + self.prenom + ","
		commande += self.nom + ","
		commande += self.pronom + ","
		commande += self.age + ","
		commande += self.race + ","
		commande += self.classe + ","
		commande += self.genre + ","
		commande += self.don + ":"

		commande += str(self.carac["force"]) + ","
		commande += str(self.carac["constitution"]) + ","
		commande += str(self.carac["dextérité"]) + ","
		commande += str(self.carac["intelligence"]) + ","
		commande += str(self.carac["sagesse"]) + ","
		commande += str(self.carac["charisme"]) + ","
		commande += str(self.defense) + ","
		commande += str(self.vie_max) + ","
		commande += str(self.vie_max) + ","
		commande += str(self.argent) + ","
		commande += str(self.xp) + ","
		commande += str(self.niveau)

		self.commande_save += commande


	def set_points_de_vie_maximum(self):
		self.vie_max += self.carac["constitution"]
		

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
		"\nNom : " , self.nom,
		"\nGenre : " , self.genre,
		"\nAge : " , self.age,
		"\nRace : " , self.race,
		"\nClasse : " , self.classe,
		"\nDon : " , self.don,
		"\n\nPV max : " , str(self.vie_max), "\n",
		]

		for k in self.carac.keys():
			text += k + " : " + str(self.carac[k]) + "\n"

		for i in range(len(text)):
			text_a_afficher += text[i]

		self.set_commande_pj()
		self.set_commande_save()

		text_a_afficher += "\n\n"
		text_a_afficher += "```!classes```Affiche les classes disponibles.\n"
		text_a_afficher += "```!genres```Affiche les genres qui influencent le prénom.\n"
		text_a_afficher += "```!races```Affiche les races qui influencent le prénom.\n"
		text_a_afficher += "```!dons:" + self.classe + "```Affiche les dons disponibles.\n"
		text_a_afficher += "\n\n*Personnalise ton personnage :*\n"
		text_a_afficher += "*(Tu peux laisser certains paramètres vides, je les remplirai.)*\n"
		text_a_afficher += self.commande_pj

		text_a_afficher += "\n\n*Sauvegarde ton personnage :*\n"
		text_a_afficher += self.commande_save

		return text_a_afficher


	def set_type_pers(self, type_pers):
		self.type_pers = type_pers


	def set_total_points(self):
		nb = self.niveau - 1
		self.total_points = 12 + nb


	def set_valeur_max(self):
		nb = self.niveau - 1
		self.valeur_max = 3 + nb


	def get_personnage(self):
		personnage = {
			"genre" : self.genre,
			"race" : self.race,
			"classe" : self.classe,
			"don" : self.don,
			"prénom" : self.prenom,
			"pronom" : self.pronom,
			"nom" : self.nom,
			"age" : self.age,
		}

		return personnage


	def set_niveau(self, niveau):
		self.niveau = niveau


	def set_arme(self):
		arme = armes_par_classe[self.classe_indice][randrange(len(armes_par_classe[self.classe_indice]))]
		self.arme = arme


	def set_armure(self, multiplicateur):
		if multiplicateur > 1:
			armure_par_classe[self.classe_indice].remove("rien")

		for i in range(3):
			piece_armure = armure_par_classe[self.classe_indice][randrange(len(armure_par_classe[self.classe_indice]))]
			if piece_armure != "rien":
				self.armure.append(piece_armure)
				self.set_defense(piece_armure)

		if multiplicateur > 1:
			armure_par_classe[self.classe_indice].append("rien")
		

	def set_defense(self, piece_armure):
			valeur_def = armes_armures[2][piece_armure][0][0]
			valeur_dex = armes_armures[2][piece_armure][1][0]

			self.defense += valeur_def
			if len(armes_armures[2][piece_armure]) > 4:
				self.carac["dextérité"] -= valeur_dex


	def get_ennemi(self):
		personnage = {
			"genre" : self.genre,
			"race" : self.race,
			"classe" : self.classe,
			"don" : self.don,
			"pronom" : self.pronom,
			"PV max : " : self.vie_max,
			"PV" : self.vie_max,
			"niveau" : self.niveau,
			"défense" : self.defense,
			"arme" : self.arme,
			"armure" : self.armure,

			"force" : self.carac["force"],
			"constitution" : self.carac["constitution"],
			"dextérité" : self.carac["dextérité"],
			"intelligence" : self.carac["intelligence"],
			"sagesse" : self.carac["sagesse"],
			"charisme" : self.carac["charisme"],
		}
		print(personnage, "\n\n")
		return personnage
