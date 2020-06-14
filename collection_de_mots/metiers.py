"""
Les listes + 1 dictionnaire permettant de générer des métiers/classes de personnages.

poste_palais_justice
poste_caserne
poste_capitainerie
poste_chateau
poste_guilde
poste_temple
pers_metier
metiers_et_carac_associee {}
pas_étudiant_e
"""


poste_palais_justice = [
	"juge",
	"avocat.e",
	"greffier/greffière",
	"garde",
	"procureur"
	]

poste_caserne = [
	"garde",
	"soldat",
	"sergent.e",
	"lieutenant.e",
	"capitaine",
	"commandant.e",
	"commissaire"
	]

poste_capitainerie =[
	"marin",
	"capitaine",
	"docker"
	]

poste_chateau = [
	"reine/roi",
	"ministre",
	"conseiller/conseillère",
	"soldat",
	"serviteur/servante",
	"soldat",
	"serviteur/servante",
	"soldat",
	"serviteur/servante",
	"soldat",
	"serviteur/servante",
	"cuisinier/cuisinière"
	]

poste_guilde = [
	"le chef",
	"le bras droit du chef",
	"simple membre",
	"simple membre",
	"simple membre",
	"simple membre",
	"simple membre",
	"simple membre",
	"simple membre"
	]

poste_temple =[
	"grand.e prêtre.sse",
	"moine",
	"copiste",
	"évèque",
	"moine",
	"moine",
	"moine",
	"moine",
	"moine",
	"moine",
	"moine"
	]

pers_metier = [
	"alchimiste",
	"apprenti.e",
	"artisan.ne",
	"archer/archère",
	"architecte",
	"assassin",
	"astrologue",
	"barde",
	"boulanger/boulangère",
	"bourreau",
	"capitaine",
	"cartographe",
	"chasseur/chasseuse",
	"chevalier/chevalière",
	"comédien.ne",
	"conseillère/conseiller royal.e",
	"contremaître",
	"courtisant/courtisanne",
	"couturier/couturière",
	"cuisinière/cuisinier",
	"duc/duchesse",
	"druide",
	"écuyère/écuyer",
	"écrivain.e publique/public",
	"éleveur/éleveuse",
	"étudiant.e",
	"forgeron.ne",
	"garde",
	"géographe",
	"guerrière/guerrier",
	"haut-placé.e",
	"joalière/joalier",
	"juge",
	"linguiste",
	"maçon.ne",
	"maire",
	"mage",
	"marchand.e",
	"maréchal.e ferrant.e",
	"marin",
	"médecin",
	"mendiant.e",
	"meunière/meunier",
	"mineur/mineuse",
	"nécromancien.ne",
	"ministre",
	"paladin.e",
	"paysan.ne",
	"pêcheur/pêcheuse",
	"peintre",
	"prefet",
	"prêtre.sse",
	"prince.sse",
	"professeur.e",
	"reine/roi",	
	"servante/serviteur",
	"serveur/serveuse",
	"sorcier/sorcière",
	"soldat.e",
	"tanneur/tanneuse",
	"tavernier/tavernière",
	"voleur/voleuse",
	]
	
metiers_et_carac_associee = {
	"alchimiste" : "Intelligence",
	"apprenti.e" : "Selon le métier étudié",
	"artisan.ne" : "Dextérité",
	"archer/archère" : "Dextérité",
	"architecte" : "Intelligence",
	"assassin" : "Dextérité",
	"astrologue" : "Sagesse",
	"barbare" : "Force",
	"barde" : "Charisme",
	#"boulanger/e" : ,
	"bourreau" : "Force",
	"capitaine" : "Sagesse",
	"cartographe" : "Intelligence",
	"chasseur/chasseuse" : "Dextérité",
	"chevalier/chevalière" : "Force",
	"comédien.ne" : "Charisme",
	"conseillère/conseiller" : "Sagesse",
	"contremaître" : "Sagesse",
	"couturier/couturière" : "Dextérité",
	"courtisant/courtisanne" : "Charisme",
	#"cuisinière/cuisinier" : ,
	"duc/duchesse" : "Charisme",
	"druide" : "Sagesse",
	"écuyère/écuyer" : "Constitution",
	"écrivain.e" : "Intelligence",
	"éleveur/éleveuse" : "Constitution",
	"étudiant.e" : "Selon le métier étudié",
	"forgeron.ne" : "Force",
	"garde" : "Force",
	"géographe" : "Intelligence",
	"guerrière/guerrier" : "Force",
	"haut-placé.e" : "Charisme",
	"joalière/joalier" : "Dextérité",
	"juge" : "Sagesse",
	"linguiste" : "Intelligence",
	"maçon.ne" : "Force",
	"maire" : "Charisme",
	"mage" : "Intelligence",
	"marchand.e" : "Charisme",
	"maréchal.e" : "Constitution",
	"marin" : "Constitution",
	"médecin" : "Intelligence",
	"mendiant.e" : "Constitution",
	#"meunière/meunier" : ,
	"mineur/mineuse" : "Force",
	"nécromancien.ne" : "Intelligence",
	"ministre" : "Charisme",
	"moine" : "Sagesse",
	"paladin.e" : "Charisme",
	"paysan.ne" : "Constitution",
	"pêcheur/pêcheuse" :"Constitution" ,
	"peintre" : "Sagesse",
	"prefet" : "Charisme",
	"prêtre.sse" : "Sagesse",
	"prince.sse" : "Charisme",
	"professeur.e" : "Intelligence",
	"reine/roi" : "Charisme",
	"rodeur/rodeuse" : "Dextérité",
	"servante/serviteur" : "Constitution",
	"serveur/serveuse" : "Constitution",
	"sorcier/sorcière" : "Intelligence",
	"soldat.e" : "Force",
	"tanneur/tanneuse" : "Constitution",
	"tavernier/tavernière" : "Sagesse",
	"voleur/voleuse" : "Dextérité",
	}


pas_étudiant_e = [
	"apprenti.e",
	"capitaine",
	"duc/duchesse",
	"écuyère/écuyer",
	"étudiant.e",
	"haut-placé.e",
	"maire",
	"mendiant.e",
	"ministre",
	"prince.sse",
	"reine/roi",

	"archer/archère",
	"assassin", 
	"barbare",
	"barde",
	"druide",
	"guerrière/guerrier",
	"mage",
	"moine",
	"nécromancien.ne",
	"paladin.e",
	"prêtre.sse",
	"rodeur/rodeuse",
	"sorcier/sorcière",
	"voleur/voleuse",
	]
	