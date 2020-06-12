"""
Ces listes et dictionnaires servent de sauvegarde de partie.
"""


info_de_partie = [] # prévisions
"""
info_de_partie = [
	{
	allowed_channel : channel.name,

	achats_autorisés : [nom_joueur_id, nom_joueur_id],					<= Pour la team n° 0 (implémenté)
	
	combat_autorisés : [nom_joueur_id, nom_joueur_id],

	nom_joueur_id : ["nom_perso",F,Co,D,I,S,Ch,def,PV_max,PV,PA,xp,classe,genre,don,[sac],[équipé]],
	nom_joueur_id : ["nom_perso",F,Co,D,I,S,Ch,def,PV_max,PV,PA,xp,classe,genre,don,[sac],[équipé]],
	nom_joueur_id : ["nom_perso",F,Co,D,I,S,Ch,def,PV_max,PV,PA,xp,classe,genre,don,[sac],[équipé]],

	}

	{
	allowed_channel : channel.name,

	achats_autorisés : [nom_joueur_id, nom_joueur_id],
	
	combat_autorisés : [nom_joueur_id, nom_joueur_id],

	nom_joueur_id : ["nom_perso",F,Co,D,I,S,Ch,def,PV_max,PV,PA,xp,classe,genre,don,[sac],[équipé]],
	nom_joueur_id : ["nom_perso",F,Co,D,I,S,Ch,def,PV_max,PV,PA,xp,classe,genre,don,[sac],[équipé]],
	nom_joueur_id : ["nom_perso",F,Co,D,I,S,Ch,def,PV_max,PV,PA,xp,classe,genre,don,[sac],[équipé]],

	"scénario" : 1,
	"avancement" : 3,													<= Pour la team n° 1 (prévisions)
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
