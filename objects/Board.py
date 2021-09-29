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

    def __init__(self):
        self.board = [[0 for j in range(5)] for i in range(5)]

    def init_board(self):
        for i in range(5):
            for j in range(5):
                self.board[i][j] = random.randint(0, 2)

    def random_dust_jewel(self):
        _x = random.randint(0, 4)
        _y = random.randint(0, 4)

        prob = random.random()

        # Add dust to current room
        if prob < 0.33 and self.board[_x][_y] not in [2, 3]:
            self.board[_x][_y] = self.board[_x][_y] + 2

        # Add jewel to current room
        elif prob > 0.66 and self.board[_x][_y] not in [1, 3]:
            self.board[_x][_y] = self.board[_x][_y] + 1

    def get_board(self):
        return self.board

    def get_room_coords_from_id(self, id):
        return [math.floor(id / 5), id % 5]

    def get_room_id_from_coords(self, coords):
        return coords[0] + (coords[1] * 5)

    # Todo Factoriser la fonction pour ne pas avoir 4 if à la suite
    def get_neighbor_rooms(self, current):
        neighbor = []
        if current[0] > 0:
            neighbor.append([current[0] - 1, current[1]])  # [x-1, y]

        if current[0] < 4:
            neighbor.append([current[0] + 1, current[1]])  # [x+1, y]

        if current[1] > 0:
            neighbor.append([current[0], current[1] - 1])  # [x, y-1]

        if current[1] < 4:
            neighbor.append([current[0], current[1] + 1])  # [x, y+1]

        return neighbor

    def create_graph(self):
        """
        Renvoie un dictionnaire de type :
        {
            "node_id" : [neighbors_id]
            ...
        }
        """
        graph = {}
        for i in range(5):
            for j in range(5):
                neighbors = self.get_neighbor_rooms([i, j])
                coords = [i, j]
                id = i + 5 * j
                neighbors_ids = list(
                    map(lambda el: self.get_room_id_from_coords(el), neighbors)
                )

                # if i == j == 0:
                #     node = Node(None, coords, id)

                graph[id] = neighbors_ids

        return graph
