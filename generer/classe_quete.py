from random import randrange


from generer.nom import *
from generer.classe_personnage import Personnage

from collection_de_mots.quete import *



class Quete:
	
	def __init__(self):
		
		self.nom = ""
		self.difficulte = ""
		self.nb_salles = ""
		self.boss = self.set_boss()
		self.multiplicateur_ennemis = 1
		self.recompense = 0
		

	def set_boss(self):
		ennemi = Personnage()
		ennemi.set_particularites()
		return ennemi.get_personnage()


	def difficulte_generale(self):
		self.difficulte = difficulte_quete[randrange(len(difficulte_quete))]

		if self.difficulte == "facile":
			self.nb_salles = randrange(4,7)
			self.recompense = 50
			self.multiplicateur_ennemis = 1

		elif self.difficulte == "normale":
			self.nb_salles = randrange(5,10)
			self.recompense = 75
			self.multiplicateur_ennemis = 2

		else:
			self.nb_salles = randrange(7,12)
			self.recompense = 100
			self.multiplicateur_ennemis = 3


	def get_difficulte_generale(self):
		difficulte_generale = {
		"niveau" : self.difficulte,
		"nb salles" : self.nb_salles,
		"récompense" : self.recompense,
		"multiplicateur" : self.multiplicateur_ennemis,
		}
		return difficulte_generale