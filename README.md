# jeux-bataille-navale en python

La bataille navale, appelée aussi touché-coulé, est un jeu de société dans lequel deux joueurs doivent placer des « navires » sur une grille tenue secrète et tenter de « toucher » les navires adverses. Le gagnant est celui qui parvient à couler (c'est-à-dire toucher toutes les cases) tous les navires de l'adversaire avant que tous les siens ne le soient.

Le principe du jeu de bataille navale semble trouver son origine dans le jeu français L'Attaque1 lors de la Première Guerre mondiale. On a aussi trouvé des liens de parenté avec le jeu de E. I. Horseman en 1890 (Baslinda2) et on dit que des officiers russes y auraient joué antérieurement à la première guerre3. La première version commerciale du jeu fut publiée en 1931 par la Starex Novelty Co. sous le nom de Salvo4. Ce jeu est devenu populaire lors de son apparition en 1943 dans les publications américaines de divertissement de la Milton Bradley Company qui l'exploita sous la forme papier jusqu'en 1967, où elle sortit un jeu de plateau5, puis en réalisa une version électronique en 1977.

# Règles

La bataille navale oppose deux joueurs. Chaque joueur dispose de deux grilles carrées de côté 10, dont les lignes sont numérotées de 1 à 10 et les colonnes de A à J, ainsi que d'une flotte composée de quelques bateaux d'une à cinq cases de long.

L'une des grilles représente la zone contenant sa propre flotte. Au début du jeu, chaque joueur place ses bateaux sur sa grille, en s'assurant que deux bateaux ne sont pas adjacents. L'autre représente la zone adverse, où il cherchera à couler les bateaux de son adversaire.

Chaque joueur, à son tour, annonce une case (par exemple « B6 »), et son adversaire lui répond si le tir tombe à l'eau ou au contraire s'il touche un bateau. Dans ce dernier cas, il annonce « touché » s'il reste des cases intactes au bateau ciblé, et « touché-coulé » si non.

Diverses variantes existent, par exemple le fait de tirer les coups par salves et de ne donner que le résultat global de la salve.
Liste des navires
Fin d'une partie de Bataille Navale (les joueurs y comparent le plus souvent leurs grilles respectives) à bord d'un porte-avions de l'U.S. Navy.

Chaque joueur possède les mêmes navires, dont le nombre et le type dépendent des règles du jeu choisies.

Une disposition peut ainsi comporter :

    1 Porte-avions (5 cases) ;
    1 Croiseur (4 cases) ;
    2 Contre-torpilleurs (3 cases) ;
    1 Torpilleur (2 cases).

Une autre disposition courante en Belgique est :

    1 Cuirassé (4 cases) ;
    2 Croiseurs (3 cases) ;
    3 Torpilleurs (2 cases) ;
    4 Sous-marin (1 case).

# Stratégie
Lorsque le plus petit bateau a une longueur de 2, une stratégie qui permet d'accélérer la découverte des bateaux adverses tout en étant sur de ne pas en rater est de tirer en damier, seulement une case sur 27. 
