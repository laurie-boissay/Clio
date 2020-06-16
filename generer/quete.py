from generer.classe_quete import Quete
from generer.personnage import *


from collection_info.save_game import *


def generer_donjon(message):

    info_de_partie[num_team(message)]["quête en cours"]["Titre"] = "titre de la quête"

    info_de_partie[num_team(message)]["quête en cours"]["Description"] = "Description de la quête."
    
    info_de_partie[num_team(message)]["quête en cours"]["players"] = []