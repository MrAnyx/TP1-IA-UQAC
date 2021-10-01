import random


class Board:
    """
    La classe Board permet de représenter l'environment. Le manoir de 5x5 pièces.
    Chaque pièce peut contenir de la poussière, des bijoux et rien.
       0 => rien
       1 => bijoux
       2 => poussière
       3 => bijoux ET poussière

    La répartition des éléments dans les pièces est faite de manière pseudo-aléatoire.
    L'environnement gère sa propre mesure de performance :
        -> 1 pt par pièce propre
        -> + 1 pt par bijou ramassé
        -> - 1 pt par bijou aspiré

    """

    NOTHING = 0
    JEWEL = 1
    DUST = 2
    BOTH = 3

    def __init__(self):
        # On crée un tableau 2D (de 5 par 5) pour symboliser le manoir
        self.board = [[0 for j in range(5)] for i in range(5)]
        # On y associe une mesure de performance simple : 1 pt par case vide
        self.performance_metric = 25

    def random_dust(self):
        """
        Génère de la poussière dans une pièce vide ou avec bijou avec une probabilité de 1/3.
        Met à jour la mesure de performance en conséquence.
        """
        # On donne une probabilité à la poussière d'apparaître
        dust_prob = 0.33

        # On séléctionne aléatoirement une pièce dans le manoir
        _x = random.randint(0, 4)
        _y = random.randint(0, 4)

        # On génère une probabilité entre 0 et 1
        prob = random.random()

        # Si la probabilité est < 1/3 ET que la pièce ne contient ni de la poussière, ni de la poussière ET un bijou
        if prob < dust_prob and self.board[_x][_y] not in [2, 3]:
            # Alors on ajoute de la poussière à la pièce sélectionnée
            self.board[_x][_y] = self.board[_x][_y] + 2
            # Et on met à jour la mesure de performance
            self.performance_metric = self.performance_metric - 1

        return [_x, _y]

    def random_jewel(self):
        """
        Génère un bijou dans une pièce vide ou avec poussière avec une probabilité de 1/3.
        Mets à jour la mesure de performance en conséquence.
        """
        # On donne une probabilité à la poussière d'apparaître
        jewel_prob = 0.33

        # On séléctionne aléatoirement une pièce dans le manoir
        _x = random.randint(0, 4)
        _y = random.randint(0, 4)

        # On génère une probabilité entre 0 et 1
        prob = random.random()

        # Si la probabilité est < 1/3 ET que la pièce ne contient ni un bijou, ni de la poussière ET un bijou
        if prob < jewel_prob and self.board[_x][_y] not in [1, 3]:
            # Alors on ajoute un bijou à la pièce sélectionnée
            self.board[_x][_y] = self.board[_x][_y] + 1
            # Et on met à jour la mesure de performance
            self.performance_metric = self.performance_metric - 1

        return [_x, _y]

    def random_dust_jewel(self):
        """
        Cette fonction permet de séléctionner une pièce de manière aléatoire et d'y positionner de la poussière ou un bijou de manière aléatoire également
        Dans le cas ou une pièce contient déjà de la poussière et qu'on y ajoute un bijou, alors la pièce finale contiendra de la poussière ET un bijou
        """
        dust_update = self.random_dust()
        jewel_update = self.random_jewel()
        return [dust_update, jewel_update]

    def clean(self, room):
        """
        Vide une pièce et met à jour la mesure de performance en conséquence.
        """
        if self.board[room[0]][room[1]] in [1, 3]:
            # Aspirer un bijou diminue la mesure de performance
            self.performance_metric = self.performance_metric - 1
        elif self.board[room[0]][room[1]] == 2:
            # Aspirer de la poussiere augmente la mesure de performance
            self.performance_metric = self.performance_metric + 1
        # Dans tous les cas, la piece est videe
        self.board[room[0]][room[1]] = 0

    def take(self, room):
        """
        Retire un bijou de la pièce s'il y en a un.
        Met à jour la mesure de performance.
        """
        if self.board[room[0]][room[1]] in [1, 3]:
            self.board[room[0]][room[1]] = self.board[room[0]][room[1]] - 1

            # Ramasser un bijou augmente la mesure de performance
            self.performance_metric = self.performance_metric + 1

    # Getter pour le board
    # Permet de récuperer l'état du board dans avoir à faire Board.board
    def get_board(self):
        return self.board

    # Getter pour la mesure de performance
    # Permet de récuperer la mesure de performance du board dans avoir à faire Board.performance_metric
    def get_performance_metric(self):
        return self.performance_metric
