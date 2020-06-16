"""
Ces listes et dictionnaires servent de sauvegarde de partie.
"""


info_de_partie = [] # prévisions
"""
info_de_partie = [
	{
	allowed_channel : channel.name,

	achats_autorisés : [nom_joueur_id, nom_joueur_id],					<= Pour la team n° 0 (implémenté)
	
	combat_autorisé : [nom_joueur_id, nom_joueur_id],

	quete en cours : {
		"titre" : "",
		"decription" : "",
		"boss" : "",
		"players" : [nom_joueur_id, nom_joueur_id, nom_joueur_id]
		}

	nom_joueur_id : {
		"p_prénom" : "",
		"p_nom" : "",
		"p_pronom" : "",
		"p_age" : "",
		"p_race" : "",
		"p_classe" : "",
		"p_genre" : "" ,
		"p_don" : "",
		"p_force" : X,
		"p_constitution" : X,
		"p_dextérité" : X,
		"p_intelligence" : X,
		"p_sagesse" : X,
		"p_charisme" : X,
		"p_défense" : X,
		"p_PV max" : X,
		"p_PV" : X,
		"p_PA" : X,
		"p_XP" : X,
		"p_sac" : [],
		"p_équipement" : [],
		},

	nom_joueur_id : {
		"p_prénom" : "",
		"p_nom" : "",
		"p_pronom" : "",
		"p_age" : "",
		"p_race" : "",
		"p_classe" : "",
		"p_genre" : "" ,
		"p_don" : "",
		"p_force" : X,
		"p_constitution" : X,
		"p_dextérité" : X,
		"p_intelligence" : X,
		"p_sagesse" : X,
		"p_charisme" : X,
		"p_défense" : X,
		"p_PV max" : X,
		"p_PV" : X,
		"p_PA" : X,
		"p_XP" : X,
		"p_sac" : [],
		"p_équipement" : [],
		},

	}

	{
	allowed_channel : channel.name,

	achats_autorisés : [nom_joueur_id, nom_joueur_id],
	
	combat_autorisés : [nom_joueur_id, nom_joueur_id],

	nom_joueur_id : {
		"p_prénom" : "",
		"p_nom" : "",
		"p_pronom" : "",
		"p_age" : "",
		"p_race" : "",
		"p_classe" : "",
		"p_genre" : "" ,
		"p_don" : "",													<= Pour la team n° 1 (prévisions)
		"p_force" : X,
		"p_constitution" : X,
		"p_dextérité" : X,
		"p_intelligence" : X,
		"p_sagesse" : X,
		"p_charisme" : X,
		"p_défense" : X,
		"p_PV max" : X,
		"p_PV" : X,
		"p_PA" : X,
		"p_XP" : X,
		"p_sac" : [],
		"p_équipement" : [],
		},

		nom_joueur_id : {
		"p_prénom" : "",
		"p_nom" : "",
		"p_pronom" : "",
		"p_age" : "",
		"p_race" : "",
		"p_classe" : "",
		"p_genre" : "" ,
		"p_don" : "",
		"p_force" : X,
		"p_constitution" : X,
		"p_dextérité" : X,
		"p_intelligence" : X,
		"p_sagesse" : X,
		"p_charisme" : X,
		"p_défense" : X,
		"p_PV max" : X,
		"p_PV" : X,
		"p_PA" : X,
		"p_XP" : X,
		"p_sac" : [],
		"p_équipement" : [],
		},
	

	"scénario" : 1,
	"avancement" : 3,
	"étapes nécessaires" : 5,
	"inocents tués" : 2,
	"quête en cours" : "5,3,12,4",
	"avancement quête" : 2,
	"étapes quêtes nécessaires" : 3,
	"code de sauvegarde" : "54,1,14/1,5,78/9"
	}
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
