from random import randrange


from generer.nom import *
from generer.classe_personnage import Personnage



class Quete:
	
	def __init__(self):
		
		self.nom = ""
		self.nb_salles = randrange(5,10)
		self.boss = self.set_boss()
		self.type_ennemis = ""
		

	def set_boss(self):
		nb_players = 1 #A modifier
		ennemi = Personnage()
		ennemi.set_particularites()
		ennemi.set_total_points(nb_players)
		ennemi.set_valeur_max(nb_players)
		return ennemi.get_personnage()