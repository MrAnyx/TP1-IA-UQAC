import random
import math

# from Node import Node


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
        self.board = [[0 for j in range(5)] for i in range(5)]
        self.performance_metric = 25

    def random_dust(self):
        """
        Génère de la poussière dans une pièce vide ou avec bijou avec une probabilité de 1/3.
        Met à jour la mesure de performance en conséquence.
        """
        dust_prob = 0.33

        _x = random.randint(0, 4)
        _y = random.randint(0, 4)

        prob = random.random()

        # Add dust to current room
        if prob < dust_prob and self.board[_x][_y] not in [2, 3]:
            self.board[_x][_y] = self.board[_x][_y] + 2
            self.performance_metric = self.performance_metric - 1

        return [_x, _y]

    def random_jewel(self):
        """
        Génère un bijou dans une pièce vide ou avec poussière avec une probabilité de 1/3.
        Mets à jour la mesure de performance en conséquence.
        """
        jewel_prob = 0.33

        _x = random.randint(0, 4)
        _y = random.randint(0, 4)

        prob = random.random()

        # Add jewel to current room
        if prob < jewel_prob and self.board[_x][_y] not in [1, 3]:
            self.board[_x][_y] = self.board[_x][_y] + 1

        return [_x, _y]

    def random_dust_jewel(self):
        """
        Génére un bijou et/ou de la poussière avec une certaine probabilité chacun.
        Retourne les positions où les élements ont été générés.
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

    def get_board(self):
        return self.board

    def get_performance_metric(self):
        return self.performance_metric
