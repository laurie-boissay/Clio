from random import randrange

from collection_de_mots.personnage import *
from collection_de_mots.noms import *

"""
Génère des noms de lieux, d'objets, d'animaux, de personnes, de métiers.
	
Décrit une zone de type ville ou village.
"""


def nom_pers(genre, race) :
	"""
	Donne un nom au personnage selon :
		- son genre ;
		- sa race.

	Particularité pour le genre androgyne ou autre genre définit par l'utilisateur,
	un genre pour le nom est pioché aléatoirement et la fonction boucle sur elle même.

	Enfin, quand l'utilisateur à définit une autre race que celle listée dans race_pers,
	une race est piochée pour son nom de personnage.
	"""
	if genre == "féminin" :
		if race == "humains" or race == "humain" or race == "demi-elfes" or race == "demi-elfe":
			nom = noms_humains[randrange(len(noms_humains))]
		elif race == "nains" or race == "nain" :
			nom = noms_nains[randrange(len(noms_nains))]
		elif race == "elfes" or race == "elfe":
			nom = noms_elfes[randrange(len(noms_elfes))]
		elif race == "orcs" or race == "orc" or race == "demi-orcs" or race == "demi-orc": 
			nom = "du-clan-de-" + prenoms_orcs_f[randrange(len(prenoms_orcs_f))]
		elif race == "halfelins" or race =="halfelin":
			nom = noms_halfelins[randrange(len(noms_halfelins))]
		elif race == "gnomes" or race =="gnome":
			nom = noms_gnomes[randrange(len(noms_gnomes))]			
		else : # Autres races
			race = race_pers[randrange(len(race_pers))]
			return nom_pers(genre, race)

	elif genre == "masculin" :
		if race == "humains" or race == "humain" or race == "demi-elfes" or race == "demi-elfe":
			nom = noms_humains[randrange(len(noms_humains))] 
		elif race == "nains" or race == "nain":
			nom = noms_nains[randrange(len(noms_nains))]
		elif race == "elfes" or race == "elfe" :
			nom = noms_elfes[randrange(len(noms_elfes))]
		elif race == "orcs" or race == "orc" or race == "demi-orcs" or race == "demi-orc":
			nom = "du-clan-de-" + prenoms_orcs_m[randrange(len(prenoms_orcs_m))]
		elif race == "halfelins" or race == "halfelin":
			nom = noms_halfelins[randrange(len(noms_halfelins))]
		elif race == "gnomes" or race =="gnome":
			nom = noms_gnomes[randrange(len(noms_gnomes))]
		else : # Autres races
			race = race_pers[randrange(len(race_pers))]
			return nom_pers(genre, race)

	else : # autres genres
		genre_pers.remove("androgyne")
		genre = genre_pers[randrange(len(genre_pers))]
		genre_pers.append("androgyne")
		
		return nom_pers(genre, race)
	
	return nom


def prenom_pers(genre, race) :
	"""
	Donne un prénom au personnage selon :
		- son genre ;
		- sa race.

	Particularité pour le genre androgyne ou autre genre définit par l'utilisateur,
	un genre pour le prénom est pioché aléatoirement et la fonction boucle sur elle même.

	Enfin, quand l'utilisateur à définit une autre race que celle listée dans race_pers,
	une race est piochée pour son prénom de personnage.
	"""
	if genre == "féminin" :
		if race == "humains" or race == "humain":
			prenom = prenoms_humains_f[randrange(len(prenoms_humains_f))]
		elif race == "nains" or race == "nain" :
			prenom = prenoms_nains_f[randrange(len(prenoms_nains_f))]
		elif race == "elfes" or race == "elfe" or race == "demi-elfes" or race == "demi-elfe":
			prenom = prenoms_elfes_f[randrange(len(prenoms_elfes_f))]
		elif race == "orcs" or race == "orc" or race == "demi-orcs" or race == "demi-orc": 
			prenom =  prenoms_orcs_f[randrange(len(prenoms_orcs_f))]
		elif race == "halfelins" or race =="halfelin":
			prenom = prenoms_halfelins_f[randrange(len(prenoms_halfelins_f))]
		elif race == "gnomes" or race =="gnome":
			prenom = prenoms_gnomes_f[randrange(len(prenoms_gnomes_f))]			
		else : # Autres races
			race = race_pers[randrange(len(race_pers))]
			return prenom_pers(genre, race)

	elif genre == "masculin" :
		if race == "humains" or race == "humain":
			prenom = prenoms_humains_m[randrange(len(prenoms_humains_m))] 
		elif race == "nains" or race == "nain":
			prenom = prenoms_nains_m[randrange(len(prenoms_nains_m))]
		elif race == "elfes" or race == "elfe"  or race == "demi-elfes" or race == "demi-elfe":
			prenom = prenoms_elfes_m[randrange(len(prenoms_elfes_m))]
		elif race == "orcs" or race == "orc" or race == "demi-orcs" or race == "demi-orc":
			prenom = prenoms_orcs_m[randrange(len(prenoms_orcs_m))]
		elif race == "halfelins" or race == "halfelin":
			prenom = prenoms_halfelins_m[randrange(len(prenoms_halfelins_m))]
		elif race == "gnomes" or race =="gnome":
			prenom = prenoms_gnomes_m[randrange(len(prenoms_gnomes_m))]
		else : # Autres races
			race = race_pers[randrange(len(race_pers))]
			return prenom_pers(genre, race)

	else : # autres genres
		genre_pers.remove("androgyne")
		genre = genre_pers[randrange(len(genre_pers))]
		genre_pers.append("androgyne")
		return prenom_pers(genre, race)
	
	return prenom


def objet_precieux() :
	"""
	Pioche un nom + un ajectif pour former un nom d'objet précieux.
	"""
	return objet_nom[randrange(len(objet_nom))] + " " + objet_adj[randrange(len(objet_adj))]


'''
def nom_auberge() :
	"""
	Pioche un nom + un ajectif pour former un nom d'auberge.
	"""
	return auberge_nom[randrange(len(auberge_nom))] + " " + auberge_adj[randrange(len(auberge_adj))]


def nom_navire() :
	"""
	Pioche un nom + un ajectif pour former un nom de navire.
	"""
	return navire_nom[randrange(len(navire_nom))] + " " + navire_adj[randrange(len(navire_adj))]


def lieu_quete() :
	"""
	Pioche un nom + un ajectif pour former un lieu de quête couvert.
	"""
	return lieu_quete_nom[randrange(len(lieu_quete_nom))] + " " + lieu_quete_adj[randrange(len(lieu_quete_adj))]

def lieu_quete_ext() :
	"""
	Pioche un nom + un ajectif pour former un lieu de quête en extérieur.
	"""
	return ext_nom[randrange(len(ext_nom))] + " " + ext_adj[randrange(len(ext_adj))]

def animal_sacre():
	"""
	Pioche un nom + un ajectif pour former un nom d'animal sacré.
	"""
	return "le/l' "+ animal_sauvage[randrange(len(animal_sauvage))] + " " + objet_adj[randrange(len(objet_adj))]


def zone():
	"""
	Permet de lancer la génération d'une zone.
	Renvoie un texte de nom de ville et la commande
	permettant d'afficher la description de la zone.
	"""
	zone = Zone()	

	zone.contraintes("")
	zone.set_zone()

	zone.set_commande()
	
	return zone.get_zone_nom() + "." + zone.get_commande() + "\n"




def metier_pers() :
	"""
	Pioche un métier pour la personne. 
	Précise pour certains métiers le domaine ou un nom de bâtiment.
	"""
	metier = pers_metier[randrange(len(pers_metier))]
	
	if metier == "haut-placé.e" :
		texte = metier + " dans " +organisation[randrange(len(organisation))]
	
	elif metier == "éleveur/éleveuse" :
		texte = metier + " de/d' " + animal_elevage[randrange(len(animal_elevage))]
	
	elif metier == "paysan.ne" :
		texte = metier + " dans la culture " + champ[randrange(len(champ))]
	
	elif metier == "servante/serviteur" :
		texte = metier+ " dans " + organisation[randrange(len(organisation))]
	
	elif metier == "serveur/serveuse" or metier == "tavernier/tavernière" :
		texte = metier + " dans l'auberge " + nom_auberge()
	
	elif metier == "marchand.e" :
		texte = metier + " de/d' " +commerce[randrange(len(commerce))]
	
	elif metier == "capitaine" :
		texte = metier + " du bateau " + nom_navire()
	
	elif metier == "artisan.ne" :
		texte = metier + " " + artisanat[randrange(len(artisanat))]

	elif metier == "apprenti.e" :
		texte = metier + " " + classe_pers[randrange(len(classe_pers))]
	
	elif metier == "étudiant.e" :
		metier_appris = specialite(pas_étudiant_e)
		texte = metier + " " + metier_appris
	
	else :
		texte = metier
	
	return texte


def specialite(metiers_interdits):
	"""
	Définit la spécialité des étudiant/e en piochant dans la liste des métiers.

	Certaines associations étudiant/e-métier sont proscrites comme : étudiant/e étudiant/e.
	La fonction vérifie la spécialité piochée avec la liste pas_apprenti_e.

	En cas de concordance, la fonction boucle sur elle même.
	"""
	metier = pers_metier[randrange(len(pers_metier))]

	if metier in metiers_interdits:
		return specialite(metiers_interdits)
	else:
		return metier


def nom_zone(taille, rich, pop, activite_1):
	"""
	Génère un nom de zone selon :
		- la taille de la zone ;
		- La densité de population de la zone ;
		- la richesse des habitants ;
		- l'activité pricipale.
	"""
	if taille == "très petite" or taille == "petite" :
		if pop == "tranquille" or pop == "déserte" :
			phrase_1 = "le "
			phrase_3 = "hammeau "
		elif pop == "très peuplée" :
			phrase_1 = "la "
			phrase_3 = "bourgade "
		else : # pop == "surpeuplée" :
			phrase_1 = "La "
			phrase_3 = "ville "

	elif taille == "grande" or taille == "très grande" :
		if pop == "déserte (population rare)" :
			phrase_1 = "La "
			phrase_3 = "étendue "
		elif pop == "tranquille (population faible)" :
			phrase_1 = "le "
			phrase_3 = "village "
		elif pop == "très peuplée" :
			phrase_1 = "la "
			phrase_3 = "ville "
		else : # pop == "surpeuplée" :
			phrase_1 = "la "
			phrase_3 = "citée "

	else : #taille == "immense" :
		if pop == "déserte" or pop == "tranquille" :
			phrase_1 = "la "
			phrase_3 = "étendue "
		elif pop == "très peuplée" :
			phrase_1 = "la "
			phrase_3 = "citée "
		else : # pop == "surpeuplée" :
			phrase_1 = "la "
			phrase_3 = "mégapole "

	if rich == "misérable" :
		phrase_2 = "misérable "
	elif rich == "pauvre" :
		phrase_2 = "modeste "
	elif rich == "plutôt à l'aise financièrement" :
		phrase_2 = "magnifique "
	else : #"riche"
		if taille != "très petite" and taille != "petite" and pop != "déserte" and pop != "tranquille" :
			phrase_2 = "majestueux/se "
		else :
			phrase_2 = "joli/e "

	if activite_1 == "le commerce" :
		phrase_4 = commercants[randrange(len(commercants))]
	elif activite_1 == "l'esclavage" :
		phrase_4 = esclavage[randrange(len(esclavage))]
	elif activite_1 == "la religion" :
		phrase_4 = religion[randrange(len(religion))]
	elif activite_1 == "la magie" :
		phrase_4 = magie[randrange(len(magie))]
	elif activite_1 == "la contrebande" :
		phrase_4 = "franc/he"
	elif activite_1 == "l'élevage" :
		phrase_4 = eleveurs[randrange(len(eleveurs))]
	elif activite_1 == "l'alcool" :
		phrase_4 = alcool[randrange(len(alcool))]
	elif activite_1 == "la drogue" :
		phrase_4 = drogue[randrange(len(drogue))]
	elif activite_1 == "la pêche" :
		phrase_4 = "des pêcheurs"
	elif activite_1 == "la chasse" :
		phrase_4 = chasse[randrange(len(chasse))]
	elif activite_1 == "l'agriculture" :
		phrase_4 = "des champs verts"
	elif activite_1 == "l'artisanat" :
		phrase_4 = artisants[randrange(len(artisants))]
	else : #activite_1 == "extraction minière" :
		phrase_4 = matiere_extraite[randrange(len(matiere_extraite))]
	return phrase_1 + phrase_2 + phrase_3 + phrase_4

'''
