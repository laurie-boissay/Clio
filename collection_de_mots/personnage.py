race_pers = [
	"humain",
	"nain",
	"elfe",
	"orc",
	"demi-orc",
	"halfelin",
	"gnome",
	"demi-elfe"
	]

age_pers = [
	"agé.e",
	"très agé.e",
	"jeune",
	"très jeune"
	]

classes_et_carac_associee = {
	"barbare" : "force",
	"barde" : "charisme",
	"druide" : "sagesse",
	"guerrière/guerrier" : "force",
	"guerrier" : "force",
	"guerrière" : "force",
	"mage" : "intelligence",
	"nécromancienne" : "intelligence",
	"nécromancien.ne" : "intelligence",
	"nécromancien" : "intelligence",
	"paladin" : "charisme",
	"paladin.e" : "charisme",
	"paladine" : "charisme",
	"prêtre" : "sagesse",
	"prêtresse" : "sagesse",
	"prêtre.sse" : "sagesse",
	"rodeuse" : "dextérité",
	"rodeur" : "dextérité",
	"rodeur/rodeuse" : "dextérité",
	"voleur/voleuse" : "dextérité",
	"voleur" : "dextérité",
	"voleuse" : "dextérité",
	}

classe = [
	"barbare",
	"barde",
	"druide",
	"guerrière/guerrier",
	"mage",
	"nécromancien.ne",
	"paladin.e",
	"prêtre.sse",
	"rodeur/rodeuse",
	"voleur/voleuse", 
	]

classe_f = [
	"barbare",
	"barde",
	"druide", 
	"guerrière",
	"mage",
	"nécromancienne",
	"paladine",
	"prêtresse",
	"rodeuse",
	"voleuse",
	]

classe_m = [
	"barbare",
	"barde",
	"druide",
	"guerrier",
	"mage",
	"nécromancien",
	"paladin",
	"prêtre",
	"rodeur",
	"voleur",
	]

toutes_classes = [
	[
	"barbare",
	"barde",
	"druide",
	"guerrière/guerrier",
	"mage",
	"nécromancien.ne",
	"paladin.e",
	"prêtre.sse",
	"rodeur/rodeuse",
	"voleur/voleuse", 
	],

	[
	"barbare",
	"barde",
	"druide", 
	"guerrière",
	"mage",
	"nécromancienne",
	"paladine",
	"prêtresse",
	"rodeuse",
	"voleuse",
	],

	[
	"barbare",
	"barde",
	"druide",
	"guerrier",
	"mage",
	"nécromancien",
	"paladin",
	"prêtre",
	"rodeur",
	"voleur",
	],
]

dons_par_classes = [
	#barbare
	{
	"berserker" : "Augmente sa constitution de 3 pour la durée du combat.\n(non cumulable).",
	"railler" : "les ennemis ont X fois plus de chances de le/la prendre provisoirement pour cible (X=force).",
	"furie" : "Sous mi-PV, double les dégâts infligés.\n(passif).",
	},

	#barde
	{
	"marche" : "augmente de 2 les dégâts des membres du groupe pour la durée du combat.\n(non cumulable)",
	"ode" : "augmente de 2 le charisme des membres du groupe pour la durée du combat.\n(non cumulable)",
	"ballade" : "chaque ennemis doit résister à l'envie de danser pour attaquer ce tour-ci.",
	},

	#druide
	{
	"ronces" : "chaque ennemis essaie de se dépêtrer pour attaquer ce tour-ci.",
	"épines" : "chaque ennemi subit 1dX dégâts ce tour-ci (X=sagesse).",
	"bienfait" : "soigne tous les membres du groupe de x PV (X=sagesse)."
	},

	#guerrière/guerrier
	{
	"cri" : "augmente sa force de 3 pour la durée du combat.\n(non cumulable).",
	"robuste" : "augmente sa défense de 2 pour la durée du combat.\n(non cumulable).",
	"railler" : "les ennemis ont X fois plus de chances de le/la prendre provisoirement pour cible (X=force).",
	},

	#mage
	{
	"cible" : "l'attention des ennemis est attirée vers le personnage designé.",
	"ombre" : "les ennemis oublient provisoirement le/la mage.",
	"sommeil" : "1dX ennemis (X=intelligence) doivent resister ou s'endormir.",
	},

	#mage
	{
	"drain" : "vole 1dX PV à sa cible (X=intelligence).",
	"réanimation" : "a X chances/10 de relever un mort (X=intelligence) + 1 au toucher par morts-vivants.\n(passif).",
	"animation" : "a X chances/10 de relever un mort (X=intelligence) + 1 dégâts par morts-vivants.\n(passif).",
	},

	#paladin.e
	{
	"lumière" : "les ennemis ont X fois plus de chances de le/la prendre provisoirement pour cible (X=charisme).",
	"intervention" : "soigne complétement 1 allié.",
	"marteau" : "étourdit 1 ennemi pendant X tours (X=charisme)",
	},

	#prêtre.sse
	{
	"bienfait" : "soigne tous les membres du groupe de X PV (X=sagesse).",
	"intervention" : "soigne complétement 1 allié.",
	"benediction" : "augmente sa sagesse de 3 pour la durée du combat.\n(non cumulable).",
	},

	#rodeur/rodeuse
	{
	"animal" : "augmente de 1 les chances de toucher des membres du groupe pour la durée du combat.\n(passif).",
	"visée" : "augmente de 3 sa dextérité pour la durée du combat.\n(non cumulable).",
	"reconnaissance" : "joue en premier/première en cas d'embuscade.\n(passif)",
	},

	#voleur/voleuse
	{
	"ombre" : "les ennemis oublient provisoirement le/la voleur/voleuse.",
	"fourbe" : "inflige X dégâts (X=dextérité) à une cible.",
	"acide" : "chaque ennemi subit 1dX dégâts ce tour-ci (X=dextérité)."
	},
]

carac = [
	"force",
	"dextérité",
	"constitution",
	"intelligence",
	"sagesse",
	"charisme",
	]

genre_pers = [
	"féminin",
	"masculin",
	"androgyne",
	]

prenoms_humains_f = [
	"An",
	"Annia",
	"Alaina",
	"Aminata",
	"Aïssata",
	"Aya",
	"Berthille",
	"Bérénia",
	"Fatou",
	"Floraline",
	"Gadrielle",
	"Jocynthe",
	"Kéline",
	"Koralie",
	"Liya",
	"Linh",
	"Malaïka",
	"Marille",
	"Mytrinne",	
	"Naelwen",
	"Natasha",
	"Ngoc",
	"Odaelle",
	"Oumou",
	"Prescille",
	"Shana"
	"Sorsha",
	"Télinne",
	"Véronnelle",
	"Wendoline",
	]

prenoms_nains_f = [
	"Astrid",
	"Arnhild",
	"Berthild",
	"Brynild",
	"Eldrid",
	"Ermenhild",
	"Frida",
	"Gerda",
	"Grimhild",
	"Gudrun",
	"Helga",
	"Hilda",
	"Ingrid",
	"Klothild",
	"Sigrid",
	"Strida",
	"Diesa"
	]

prenoms_elfes_f = [
	"Elberenh",
	"Elidhwen",
	"Ellenùviel",
	"Laurelinn",
	"Linaëwen",
	"Laendorië",
	"Maelwë",
	"Maerwen",
	"Nennenvaël",
	"Ninwelotë",
	"Tintaëlle",
	"Aëldill",
	"Aluinill",
	"Aliann",
	"Dianaë",
	"Eilinelle",
	"Elenwëe",
	"Lùthill",
	"Ninielle",
	"Nolwaënn",
	"Mirielle",
	"Keltienn"
	]

prenoms_orcs_f = [
	"Aoga",
	"Bargula",
	"Caroka",
	"Droga",
	"Eroka",
	"Farga",
	"Goroga",
	"Hurla",
	"Jorgula",
	"Kroka",
	"Krusha",
	"Luga",
	"Moga",
	"Noroka",
	"Roka",
	"Urdua",
	"Baggi",
	"Emen",
	"Engong",
	"Myev",
	"Neega",
	"Ovak",
	"Ownka",
	"Shautha",
	"Vola",
	"Volen"
	]

prenoms_halfelins_f = [
	"Eglantine",
	"Lila",
	"Jacinthe",
	"Rose",
	"Margueritte",
	"Muguette",
	"Pâquerette",
	"Prune",
	"Jasmine",
	"Cerise"
	]

prenoms_gnomes_f = [
	"Thérèse",
	"Huguette",
	"Rose",
	"Marceline",
	"Jeannette",
	"Eugénie",
	"Denise",
	"Germaine",
	"Charlotte",
	"Gyslaine"
	]

prenoms_humains_m = [
	"Adalrik",
	"Arn",
	"Bernulf",
	"Brand",
	"Edwald",
	"Ferwin",
	"Gerulf",
	"Godfred",
	"Gunter",
	"Habib",
	"Halfdan",
	"Ingvar",
	"Jin",
	"Keenan",
	"Ketil",
	"Knud",
	"Lassana",
	"Lothar",
	"Madhi",
	"Osvald",
	"Roderick",
	"Rurik",
	"Sékou",
	"Sigfred",
	"Sigmar",
	"Sigvald",
	"Souleymane",
	"Stig",
	"Svenn",
	"Tao",
	"Thorsten",
	"Yu",
	]

prenoms_nains_m = [
	"Gloin",
	"Krorin",
	"Thorin",
	"Buldur",
	"Trorin",
	"Orik",
	"Durok",
	"Guerann",
	"Korik",
	"Barrend",
	"Brottor"
	]

prenoms_elfes_m = [
	"Arwendil",
	"Caëldwendir",
	"Eldwyndor",
	"Elberenhdir",
	"Elendur",
	"Gilgalendil",
	"Irwildur",
	"Laurelith",
	"Linaëndir",
	"Laendoril",
	"Nennendir",
	"Aëdin",
	"Caëndor",
	"Cirion",
	"Doralion",
	"Ealdor",
	"Findalion",
	"Glorfindor",
	"Haëldion",
	"Laurendor",
	"Morwendir",
	"Raëldirion"
	]

prenoms_orcs_m = [
	"Aog",
	"Bargul",
	"Carok",
	"Drog",
	"Erok",
	"Farg",
	"Gorog",
	"Hurl",
	"Jorgul",
	"Krok",
	"Krush",
	"Lug",
	"Mog",
	"Norok",
	"Rok",
	"Urdu",
	"Dench",
	"Feng",
	"Gell",
	"Henk",
	"Holg",
	"Imsh",
	"Keth",
	"Krusk",
	"Ront",
	"Shump",
	"Thokk"
	]

prenoms_halfelins_m = [
	"Bill",
	"Bern",
	"Don",
	"Duky",
	"Eckel",
	"Fili",
	"Ged",
	"Gerry",
	"Hek",
	"Hicks",
	"Jack",
	"Karl",
	"Litle",
	"Luky",
	"Mike",
	"Polo",
	"Sam",
	"Titi"
	]

prenoms_gnomes_m = [
	"Albert",
	"Edgard",
	"Eustache",
	"Firmin",
	"Isidore",
	"Nestor",
	"Charles",
	"Bertrand",
	"Louis",
	"Guy",
	"Guilbert"
	]

noms_nains = [
	"Mâchefer",
	"Briseroc",
	"Forgefer",
	"Tranchetroll",
	"Cassegranit",
	"Briselame",
	"Ecu-de-chêne",
	"Marteleur",
	"Peau-de-pierre"
	]

noms_humains = [
	"Dubois",
	"Dupont",
	"Deschamps",
	"Boulanger",
	"Charpentier",
	"nacunoeil",
	"Dumoulin",
	"Marin",
	"Dubourg",
	"Marchand",
	"Tavernier",
	"Lenoir",
	"Legrand",
	"Lepetit",
	"Legros"
	]

noms_halfelins =[
	"Sur-le-pont",
	"Dubois",
	"Sous-colline",
	"Moulinbas",
	"Verte-prairie",
	"Du-hautchamp",
	"Rivière",
	"Du-lac-aux-joncs",
	"Feuilledethé",
	"SousRameau"
	]

noms_gnomes = [
	"Blumdenplick",
	"Dimtigballen",
	"Vondemacht",
	"Kolerbiltag",
	"Wurmenship",
	"Aliserwilp",
	"Uhldimmerstelp",
	"Molkenpulp",
	"Bimpbelinedor"
	]

noms_elfes = [
	"Amastacia",
	"Fleur-d'Etoile",
	"Amakiir",
	"Fleur-de-Gemme",
	"Galanodel",
	"Murmure-de-Lune",
	"Holimion",
	"Rosée-de-Diamant",
	"Liadon",
	"Feuille-d'Argent",
	"Meliamne",
	"Pied-de-Chêne",
	"Naïlo",
	"Brise-Nocturne",
	"Siannodel",
	"Ruisseau-de-Lune",
	"Ilphukiir",
	"Bouton-de-Gemme",
	"Xiloscient",
	"Pétale-d'Or"
	]

carac_mots = [
	"p_prénom",
	"p_nom",
	"p_pronom",
	"p_age",
	"p_race",
	"p_classe",
	"p_genre",
	"p_don",
]

carac_entiers = [
	"p_force",
	"p_constitution",
	"p_dextérité",
	"p_intelligence",
	"p_sagesse",
	"p_charisme",

	"p_défense",
	"p_PV max",
	"p_PV",
	"p_PA",
	"p_XP",
]
