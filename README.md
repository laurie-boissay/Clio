# Clio
Bot Discord Fr : JDR sur Discord


Clio (la muse de l'histoire) va annimer des parties de JDR sur Discord en tant que (débutante) maître de jeu.
Elle sera construire sur les bases de Calliope (la muse de la poësie épique) mon précédent bot Discord.

J'aimerai que Clio soit intelligente et puisse retenir des informations que les joueurs / joueuses tapent eux même sur Discord. Clio donnera des codes de sauvegardes aux utilisateurs / utilisatrices pour redémarrer la partie avec leur personnage et leur progression intacts après un redémarrage.

/!\ Je joins une image mais elle n'est pas de moi.

- elle est déjà capable d'associer un pseudo discord avec tout un personnage et un numéro de team ; 

- les commandes de jeux ne sont autorisées que dans le canal choisit par le créateur de la partie ; <= annulé

- pour certaines commandes, elle répond seulement en message privé pour ne pas poluer le canal de discussion.

10/06/20 :

- commandes déjà implémentées :
        !aide
        !nouvelle partie
        !pj
        !info
        !classes
        !genres
        !joue
        !qui
        !1d20+5
        
 - ajout de set d'équipement pour toutes les catégorie de personnages.
 
11/06/20 :

- modification de l'équipement. Il ne sera pas sous forme de set mais plus libre d'accés ;

- création d'une "boutique" d'armes et d'armures, la recherche se fait par mots clés. Le procésus fait partie de la narration. Il n'est pas encore possible "d'acheter" ;

- ajout de quelques dons pour 3 classes de personnages. Je cherche encore pour les autres.

12/06/20 :

- ajout de la commande pour acheter de l'équipement ;

- ajout de la commande pour s'équiper d'une armure ;

- ajout de la commande pour déséquiper une armure ;

- Les achats sont soit autorisés soit interdits ;

- ajout d'attributs de personnage.

13/06/20 :

- début de la fonction de combat : les joueurs/joueuses peuvent faire un jet de toucher avec une arme en leur possession. Les dés sont lancés avec le bonus de la stat appropriée ;

- chaque classe de personnage à trois dons. Les PJ sont générés avec un don aléatoire ou choisit de leur classe. Les dons sont expliqués grâce à la commande !dons.

14/06/20 :

- réorganisation du code ;

- import des fichiers de Calliope ;

- début d'implémentation de la génération de quêtes. Le commanditaire est généré en premier en fonction des choix des joueurs. Le texte de contexte est implémenté ;

- les personnages peuvent équiper et déséquiper jusqu'à 3 pièces d'armure. Les stat des personnages sont modifiés en fonction de l'armure ;

- les commandes utilisables en jeu ne sont lues que dans le canal définit comme autorisé.

15/06/20 :

- ajout d'attributs pour les PJ : nom, race, pronom, age ;

- modification du système de "sauvegarde", les attributs des personnages sont sauvegardés dans un dictionnaire plutôt que dans une liste ;

- modifiction du texte de contexte de quête. Ajout de détails sur le commanditaire.

16/06/20 :

- suppression du système de génération de quête et de zone ;

- début d'un système de génération de donjons ;

- les joueurs/joueuses d'une équipe peuvent générer un seul donjon à la fois ;

- un.e joueur/joueuse peut accepter la quête (le donjon);

- tou.te.s les joueurs/joueuses peuvent rejoindre le combat individuelement ;

- il est possible de refuser la quête si aucun.e joueur/joueuse n'a rejoint le combat ;

- un.e joueur/joueuse peut téléporter le groupe de joueurs/joueuses dans le donjon, les combats sont autorisés pour eux/elles ;

- un.e joueur/joueuse peut se téléporter dans le donjon si le combat a déjà commencé.
