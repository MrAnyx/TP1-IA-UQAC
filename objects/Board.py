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
    """

    NOTHING = 0
    JEWEL = 1
    DUST = 2
    BOTH = 3

    def __init__(self):
        self.board = [[0 for j in range(5)] for i in range(5)]
        #TODO : S'en servir
        self.performance_metric = 0

    def init_board(self):
        for i in range(5):
            for j in range(5):
                self.board[i][j] = random.randint(0, 3)
        
                
    def get_board(self):
        return self.board
    
    def get_performance_metric(self):
        return self.performance_metric

    def random_dust(self):
        dust_prob = 0.33

        _x = random.randint(0, 4)
        _y = random.randint(0, 4)

        prob = random.random()

        # Add dust to current room
        if prob < dust_prob and self.board[_x][_y] not in [2, 3]:
            self.board[_x][_y] = self.board[_x][_y] + 2

    def random_jewel(self):
        jewel_prob = 0.33

        _x = random.randint(0, 4)
        _y = random.randint(0, 4)

        prob = random.random()

        # Add dust to current room
        if prob < jewel_prob and self.board[_x][_y] not in [1, 3]:
            self.board[_x][_y] = self.board[_x][_y] + 1

    def random_dust_jewel(self):
        self.random_dust()
        self.random_jewel()

    #TODO : mettre à jour la mesure de performance pour les methodes clean and take

    def clean(self, room) : 
        if room[0] in range(5) and room[1] in range(5) :
            self.board[room[0]][room[1]] = 0
    
    def take(self, room) :
        if self.board[room[0]][room[1]] in [1, 3]:
            self.board[room[0]][room[1]] = self.board[room[0]][room[1]] - 1

    

   
