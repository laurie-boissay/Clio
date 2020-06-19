"""
Listes des équipements.
"""

armes_armures = [
	
	{# armes à une main
	"hache" : [[1, "d6 deg, touche sur la ", "force"], "à une main", "au corps à corps", 25],
	"épée" : [[1, "d6 deg, touche sur la ", "force"], "à une main", "au corps à corps", 25],

	"bouclier" : [[1, " en ", "défense"], "à une main", "comme armure", 25],

	"dague" : [[1, "d6 deg, touche sur la ", "dextérité"], "à une main", "au corps à corps", 25],

	"poignard sacrificiel" : [[1, "d6 deg, touche sur l\'", "intelligence"], "à une main", "au corps à corps", 25],

	"croix" : [[1, "d6 deg, touche sur la ", "sagesse"], "à une main", "au corps à corps", 25],
	"griffe" : [[1, "d6 deg, touche sur la ", "sagesse"], "à une main", "au corps à corps", 25],

	"rapière" : [[1, "d6 deg, touche sur le ", "charisme"], "à une main", "au corps à corps", 25],
	"morgenstern" : [[1, "d6 deg, touche sur le ", "charisme"], "à une main", "au corps à corps", 25],
	
	
	"hachette" : [[1, "d6 deg, touche sur la ", "force"], "à une main", "à distance", 25],

	"fronde" : [[1, "d6 deg, touche sur la ", "dextérité"], "à une main", "à distance", 25],
	"shuriken" : [[1, "d6 deg, touche sur la ", "dextérité"], "à une main", "à distance", 25],

	"baguette" : [[1, "d6 deg, touche sur l\'", "intelligence"], "à une main", "à distance", 25],
	"wangas" : [[1, "d6 deg, touche sur l\'", "intelligence"], "à une main", "à distance", 25],

	"livre saint" : [[1, "d6 deg, touche sur la ", "sagesse"], "à une main", "à distance", 25],
	"grigri" : [[1, "d6 deg, touche sur la ", "sagesse"], "à une main", "à distance", 25],

	"livre de chants" : [[1, "d6 deg, touche sur le ", "charisme"], "à une main", "à distance", 25],
	},

	{# armes à deux mains
	"épée lourde" : [[2, "d6 deg, touche sur la ", "force"], "à deux mains", "au corps à corps", 50],
	"hache de guerre" : [[2, "d6 deg, touche sur la ", "force"], "à deux mains", "au corps à corps", 50],

	"katana" : [[2, "d6 deg, touche sur la ", "dextérité"], "à deux mains", "au corps à corps", 50],
	"arbalète" : [[2, "d6 deg, touche sur la ", "dextérité"], "à deux mains", "à distance", 50],
	"arc" : [[2, "d6 deg, touche sur la ", "dextérité"], "à deux mains", "à distance", 50],

	"sceptre" : [[2, "d6 deg, touche sur l\'", "intelligence"], "à deux mains", "à distance", 50],
	"necronomicon" : [[2, "d6 deg, touche sur l\'", "intelligence"], "à deux mains", "à distance", 50],
	"faux" : [[2, "d6 deg, touche sur l\'", "intelligence"], "à deux mains", "au corps à corps", 50],
	
	"marteau sain" : [[2, "d6 deg, touche sur la ", "sagesse"], "à deux mains", "au corps à corps", 50],
	"baton" : [[2, "d6 deg, touche sur la ", "sagesse"], "à deux mains", "au corps à corps", 50],

	"marteau scintillant" : [[2, "d6 deg, touche sur le ", "charisme"], "à deux mains", "au corps à corps", 50],
	"épée rutillante" : [[2, "d6 deg, touche sur le ", "charisme"], "à deux mains", "au corps à corps", 50],

	"lyre" : [[2, "d6 deg, touche sur le ", "charisme"], "à deux mains", "à distance", 50],
	},

	{# comme armures
	"armure de plate" : [[2, " en ", "défense"], [-1, " en ", "dextérité"], "équipée", "comme pièce d'armure (3 slots)", 40],
	"armure de cuir" : [[1, " en ", "défense"], "équipée", "comme pièce d'armure (3 slots)", 40],
	"harnais souple" : [[1, " en ", "défense"], "équipé", "comme pièce d'armure (3 slots)", 40],
	"robe magique" : [[1, " en ", "défense"], "équipée", "comme pièce d'armure (3 slots)", 40],
	"vêtements élégants" : [[1, " en ", "défense"], "équipés", "comme pièce d'armure (3 slots)", 40],
	"robe de bure" : [[1, " en ", "défense"], "équipée", "comme pièce d'armure (3 slots)", 40],
	"pagne" : [[1, " en ", "défense"], "équipé", "comme pièce d'armure (3 slots)", 40],
	},
]


armes_par_classe = [
	#barbare
	[
		["hache", "bouclier",],
		["hache", "hachette",],
		["hache de guerre",],
	],

	#barde
	[
		["rapière","livre de chants",],
		["lyre",],
	],

	#druide
	[
		["griffe","grigri",],
		["baton",],
	],

	#guerrière/guerrier
	[
		["épée", "bouclier",],
		["épée", "hachette",],
		["épée lourde",],
	],

	#mage
	[
		["poignard sacrificiel", "baguette",],
		["sceptre",],
	],

	#nécromancien.ne
	[
		["poignard sacrificiel", "wangas",],
		["necronomicon",],
		["faux",],
	],

	#paladin.e
	[
		["morgenstern", "bouclier",],
		["épée rutillante",],
		["marteau scintillant",],
	],

	#prêtre.sse
	[
		["croix", "livre saint",],
		["croix", "bouclier",],
		["bouclier", "livre saint",],
		["marteau sain",],
		["baton",],
	],

	#rodeur/rodeuse
	[
		["dague", "fronde",],
		["arbalète",],
		["arc",],
	],

	#voleur/voleuse
	[
		["dague", "shuriken",],
		["Katana",],
	],
]

armure_par_classe = [
	#barbare
	[
	"rien",
	"pagne",
	],

	#barde
	[
	"rien",
	"vêtements élégants",
	],

	#druide
	[
	"rien",
	"armure de cuir",
	],

	#guerrière/guerrier
	[
	"rien",
	"armure de plate",
	"armure de cuir",
	],

	#mage
	[
	"rien",
	"robe magique",
	],

	#nécromancien.ne
	[
	"rien",
	"robe magique",
	],

	#paladin.e
	[
	"rien",
	"armure de plate",
	],

	#prêtre.sse
	[
	"rien",
	"robe de bure",
	],

	#rodeur/rodeuse
	[
	"rien",
	"harnais souple",
	],

	#voleur/voleuse
	[
	"rien",
	"harnais souple",
	],
]



armes_1_main = []

armes_2_mains = []

armures = []

