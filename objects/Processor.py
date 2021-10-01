from objects.Board import Board
from objects.Node import Node
from objects.Agent import Agent
import math


class Processor:
    def __init__(self, board):
        self.graph = None
        self.board = board

    def get_room_coords_from_id(self, id):
        return [id % 5, math.floor(id / 5)]

    def get_room_id_from_coords(self, coords):
        return coords[0] + (coords[1] * 5)

    # def get_neighbor_rooms(self, current):
    #     neighbor = []
    #     if current[0] > 0:
    #         neighbor.append([current[0] - 1, current[1]])  # [x-1, y]

    #     if current[0] < 4:
    #         neighbor.append([current[0] + 1, current[1]])  # [x+1, y]

    #     if current[1] > 0:
    #         neighbor.append([current[0], current[1] - 1])  # [x, y-1]

    #     if current[1] < 4:
    #         neighbor.append([current[0], current[1] + 1])  # [x, y+1]

    #     return neighbor

    # # Les performances de cet algorithme dépendent de la manière dont le graph est construit
    # # Les noeuds seront pris dans l'ordre donc il ce peut que les solutions soient différentes selon le graph
    # # Cet algorithme retourne la première solution qu'il trouve (ce n'est pas forcement la plus optimisée)
    # def depth_first_search(self, start_key, path=[]):
    #     [start_x, start_y] = self.get_room_coords_from_id(start_key)

    #     path = path + [start_key]
    #     if self.board.get_board()[start_x][start_y] in [
    #         Board.DUST,
    #         Board.JEWEL,
    #         Board.BOTH,
    #     ]:
    #         return path

    #     for node in self.graph.get_node_neighbors(start_key):
    #         if node not in path:
    #             _tmp_path = self.depth_first_search(node, path)
    #             if _tmp_path:
    #                 return _tmp_path

    #     return None

    # # Exploration non informée
    # # Ici, l'algo retourne la solution la plus courte entre deux noeuds
    # def depth_first_search_optimized(self, start_key, path=[]):
    #     [start_x, start_y] = self.get_room_coords_from_id(start_key)

    #     path = path + [start_key]
    #     if self.board.get_board()[start_x][start_y] in [
    #         Board.DUST,
    #         Board.JEWEL,
    #         Board.BOTH,
    #     ]:
    #         return path

    #     shortest_path = None
    #     for node in self.graph.get_node_neighbors(start_key):
    #         if node not in path:
    #             _tmp_path = self.depth_first_search_optimized(node, path)
    #             if _tmp_path:
    #                 if not shortest_path or len(_tmp_path) < len(shortest_path):
    #                     shortest_path = _tmp_path

    #     return shortest_path

    # Exploration informée avec une heuristique (norme entre deux cases)
    def greedy_search(self):
        pass

    def expand(self, node):
        sucessors = []

        # Pièce vide = les noeuds sucesseurs sont les déplacements vers les cases voisines
        if node.state.room_state == Board.NOTHING:

            if node.state.position[0] > 0 and node.action != Agent.MOVE_RIGHT:
                # [x-1, y]
                sucessors.append(
                    Node(
                        state=node.state.next_state(Agent.MOVE_LEFT, self.board),
                        parent=node,
                        action=Agent.MOVE_LEFT,
                    )
                )

            if node.state.position[0] < 4 and node.action != Agent.MOVE_LEFT:
                # [x+1, y]
                sucessors.append(
                    Node(
                        state=node.state.next_state(Agent.MOVE_RIGHT, self.board),
                        parent=node,
                        action=Agent.MOVE_RIGHT,
                    )
                )

            if node.state.position[1] > 0 and node.action != Agent.MOVE_DOWN:
                # [x, y-1]
                sucessors.append(
                    Node(
                        state=node.state.next_state(Agent.MOVE_UP, self.board),
                        parent=node,
                        action=Agent.MOVE_UP,
                    )
                )

            if node.state.position[1] < 4 and node.action != Agent.MOVE_UP:
                # [x, y+1]
                sucessors.append(
                    Node(
                        state=node.state.next_state(Agent.MOVE_DOWN, self.board),
                        parent=node,
                        action=Agent.MOVE_DOWN,
                    )
                )

        # Piece ou seulement le bijou a ete ramasse, il reste de la poussieree
        elif node.state.room_state == Board.DUST:

            sucessors.append(
                Node(
                    state=node.state.next_state(Agent.CLEAN, self.board),
                    parent=node,
                    action=Agent.CLEAN,
                )
            )

        # Pièce avec bijou = un successeur : ramasser
        else:  # Board.BOTH or Board.JEWEL

            sucessors.append(
                Node(
                    state=node.state.next_state(Agent.TAKE, self.board),
                    parent=node,
                    action=Agent.TAKE,
                )
            )
        return sucessors

    def get_board_dirt_number(self):
        dirt_number = 0
        for row in range(5):
            for col in range(5):
                if self.board[row][col] != Board.NOTHING:
                    dirt_number = dirt_number + 1
        return dirt_number

    def depth_first_search(self, start_node, best_so_far, actions=[]):
        if start_node.action:
            actions = actions + [start_node.action]

        # But et critère d'arrêt
        max_depth = 15
        if start_node.state.dirt_number == 0:
            best_so_far["actions"] = actions
            best_so_far["dirt_number"] = 0
            return actions

        # Mémorisation du meilleur plan d'action pour l'instant
        if start_node.state.dirt_number < best_so_far["dirt_number"]:
            best_so_far["dirt_number"] = start_node.state.dirt_number
            best_so_far["actions"] = actions

        if start_node.depth < max_depth:
            for node in self.expand(start_node):
                _tmp_actions = self.depth_first_search(node, best_so_far, actions)
                if _tmp_actions:
                    return _tmp_actions

        return None
