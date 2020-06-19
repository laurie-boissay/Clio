"""
Ces listes et dictionnaires servent de sauvegarde de partie.
"""


info_de_partie = []
"""
info_de_partie = [
	{
	"allowed_channel" : channel.name,

	"achats_autorisés" : [nom_joueur_id, nom_joueur_id],					<= Pour la team n° 0
	
	"combat_autorisé" : [nom_joueur_id, nom_joueur_id],

	"niveau des joueurs" : [],

	quete en cours : {
		"titre" : "",
		"boss" : {
			"genre" : "",
			"race" : "",
			"classe" : "",
			"don" : "",
			"prénom" : "",
			"pronom" : "",
			"nom" : "",
			"age" : "",
			},
		"difficulté" : {
			"difficulté" : "",
			"nb salles" : x,
			"récompense" : "",
			"multiplicateur" : x,
			},
		"players" : [nom_joueur_id, nom_joueur_id, nom_joueur_id],
		"butin" : [],
		"objetcif" : "",
		"ennemis" : [
				{
				"classe" : "",
				"race" : "",
				"don" : "",
				"force" : X,
				"constitution" : X,			<= ennemi 0
				"dextérité" : X,
				"intelligence" : X,
				"sagesse" : X,
				"charisme" : X,
				"défense" : X,
				"PV max" : X,
				"PV" : X,
				"armure" : [],
				"arme" : [],
				}
			]
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
		"p_niveau" : X,
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
		"p_niveau" : X,
		"p_sac" : [],
		"p_équipement" : [],
		},

	}

	
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
