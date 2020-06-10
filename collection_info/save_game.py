"""
Ces listes et dictionnaires servent de sauvegarde de partie.
"""


info_de_partie = [] # prévisions
"""
info_de_partie = [
	{
	nom_joueur_id : "nom_perso",
	nom_joueur_id : "nom_perso",
	nom_joueur_id : "nom_perso",
	"scénario" : 1,
	"avancement" : 3,													<= Pour la team n° 0
	"étapes nécessaires" : 5,
	"inocents tués" : 2,
	"quête en cours" : "5,3,12,4",	<= code identification quête.
	"avancement quête" : 2,
	"étapes quêtes nécessaires" : 3,
	"nom_perso" : [3,4,5,0,1,2, druide],
	"nom_perso" : [1,0,2,4,3,5, mage],	<= les valeurs des carac des héros, classe, stuff...
	"nom_perso" : [0,5,3,4,1,2, moine],

	"code de sauvegarde" : "54,1,14/1,5,78/9"	<= code a entrer en cas de perte de données.
	}

	{
	nom_joueur_id : "nom_perso",
	nom_joueur_id : "nom_perso",
	nom_joueur_id : "nom_perso",
	"scénario" : 2,
	"avancement" : 0,													<= Pour la team n° 1...
	"étapes nécessaires" : 6,
	"inocents tués" : 0,
	"quête en cours" : "1,10,2,7",
	"avancement quête" : 1,
	"étapes quêtes nécessaires" : 3,
	...
	}
]
"""

allowed_channels = []
"""
allowed_channels = [
	id_channel_allowed_1,
	id_channel_allowed_2,
	id_channel_allowed_3,
]
"""


team_des_joueurs = {}
"""
team_des_joueurs = {
	nom_perso_id : n°_team,
	nom_perso_id : n°_team,
	nom_perso_id : n°_team,
}
"""
