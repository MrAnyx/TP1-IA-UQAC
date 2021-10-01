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

    # Exploration informée avec une heuristique (norme entre deux cases)
    def greedy_search(self):
        pass

    def expand(self, node):
        """
        A partir d'un noeud, renvoie les noeuds voisins.
        Certaines actions ne sont volontairement pas explorés.
        Par exemple, s'il y a de la poussière sur la position du robot,
        la seule issue est d'aspirer.
        """
        sucessors = []

        # Pièce vide = les noeuds sucesseurs sont les déplacements vers les cases voisines
        if node.state.room_state == Board.NOTHING:

            # Vérifie si le mouvement est possible et évite les retours en arrière inutiles
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

        # Pièce avec de la poussière = un successeur : aspirer
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
        """
        Renvoie le nombre de pièce non propres du manoir.
        """
        dirt_number = 0
        for row in range(5):
            for col in range(5):
                if self.board[row][col] != Board.NOTHING:
                    dirt_number = dirt_number + 1
        return dirt_number

    def depth_first_search(self, start_node, best_so_far, actions=[]):
        """
        Execute l'algorithme d'exploration Depth First Search.
        L'objectif est de trouver une série d'actions qui rend le manoir
        propre. L'algorithme se limite à une coût maximum prédéfini, s'il
        ne trouve pas de résultat en dessous de ce coût, il renvoie le premier
        meilleur résultat qu'il a rencontré, celui qui donne le plus grand nombre de
        pièces vidées.
        """

        if start_node.action:
            actions = actions + [start_node.action]

        # But et critère d'arrêt
        max_depth = 15
        if start_node.state.dirt_number == 0:
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

    def depth_first_search_optimized(self, start_node, best_so_far, actions=[]):
        """
        Cette fois-ci, l'algorithme est optimisé dans le sens ou le chemin retourné à la fin est le plus court possible
        L'algorithme est globalement le même que pour la fonction depth_first_search
        La principale différence est que l'on sauvegarde l'ensemble des chemins retournés et on les compares entre eux pour retourner le plus court
        Le chemin retourné correspond donc au chemin le plus court la position actuelle du robot et la pièce contenant de la poussière ou un bijou la plus proche
        """

        if start_node.action:
            actions = actions + [start_node.action]

        max_depth = 15

        # On crée une variable pour sauvegarder le chemin le plus court
        shortest_path = None

        # Condition de fin pour la fonction récurssive
        # Si le manoir est propre
        if start_node.state.dirt_number == 0:
            return actions

        # Mémorisation du meilleur plan d'action pour l'instant
        # Au cas où il n'y a pas de résultat qui vide tout le manoir est trouvé
        if (
            start_node.state.dirt_number < best_so_far["dirt_number"]
            and start_node.depth < best_so_far["cost"]
        ):
            best_so_far["dirt_number"] = start_node.state.dirt_number
            best_so_far["actions"] = actions

        # Si on a pas atteint la profondeur maximale (donc le coût maximum )
        if start_node.depth < max_depth:

            # Pour chaque noeud générés à partir du noeuds courants
            for node in self.expand(start_node):

                # On appelle de manière récurssive l'algorithme DFS avec la pièce de départ
                _tmp_actions = self.depth_first_search_optimized(
                    node, best_so_far, actions
                )

                # Si un chemin est retourné par la fonction
                if _tmp_actions:

                    # On le compare avec le chemin le plus court précédemment sauvegardé
                    if not shortest_path or len(_tmp_actions) < len(shortest_path):

                        # Si le nouveau chemin est plus court, on le conserve et un supprime l'ancien
                        shortest_path = _tmp_actions

        # On retourne le chemin le moins coûteux
        return shortest_path
