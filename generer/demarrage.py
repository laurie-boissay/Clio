from collection_de_mots.equipement import *


def initialiser():
	for k, v in armes_armures[0].items():
		armes_1_main.append(k)

	for k, v in armes_armures[1].items():
		armes_2_mains.append(k)

	for k, v in armes_armures[2].items():
		armures.append(k)
	