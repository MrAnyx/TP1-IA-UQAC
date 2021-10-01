from objects.Graph import Graph
from objects.Board import Board
import math


# TODO Commenter le code

class Processor:
    def __init__(self, board):
        self.graph = None
        self.board = board

    def get_room_coords_from_id(self, id):
        return [id % 5, math.floor(id / 5)]

    def get_room_id_from_coords(self, coords):
        return coords[0] + (coords[1] * 5)

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
                id = i + 5 * j
                neighbors_ids = list(
                    map(lambda el: self.get_room_id_from_coords(el), neighbors)
                )

                graph[id] = neighbors_ids

        self.graph = Graph(graph)

    # Les performances de cet algorithme dépendent de la manière dont le graph est construit
    # Les noeuds seront pris dans l'ordre donc il ce peut que les solutions soient différentes selon le graph
    # Cet algorithme retourne la première solution qu'il trouve (ce n'est pas forcement la plus optimisée)
    def depth_first_search(self, start_key, path=[]):
        [start_x, start_y] = self.get_room_coords_from_id(start_key)

        path = path + [start_key]
        if self.board.get_board()[start_x][start_y] in [
            Board.DUST,
            Board.JEWEL,
            Board.BOTH,
        ]:
            return path

        for node in self.graph.get_node_neighbors(start_key):
            if node not in path:
                _tmp_path = self.depth_first_search(node, path)
                if _tmp_path:
                    return _tmp_path

        return None

    # Exploration non informée
    # Ici, l'algo retourne la solution la plus courte entre deux noeuds
    def depth_first_search_optimized(self, start_key, path=[]):
        [start_x, start_y] = self.get_room_coords_from_id(start_key)

        path = path + [start_key]
        if self.board.get_board()[start_x][start_y] in [
            Board.DUST,
            Board.JEWEL,
            Board.BOTH,
        ]:
            return path

        shortest_path = None
        for node in self.graph.get_node_neighbors(start_key):
            if node not in path:
                _tmp_path = self.depth_first_search_optimized(node, path)
                if _tmp_path:
                    if not shortest_path or len(_tmp_path) < len(shortest_path):
                        shortest_path = _tmp_path

        return shortest_path

    # Exploration informée avec une heuristique (norme entre deux cases)
    def greedy_search(self):
        pass
