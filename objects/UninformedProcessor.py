# Auteur : Robin Bidanchon

from objects.Graph import Graph
from objects.Board import Board
from utils.ProcessorHelper import ProcessorHelper
import math
import random


class UninformedProcessor:
    """
    Cette classe permet d'effectuer les calculs relatifs au robot
    Elle permet de récupérer l'indice d'une pièce à partir de coordonnées et inversement
    Cette classe permet également d'effectuer la recherche non-informée (DFS) afin de déterminer le chemin optimal
    """

    def __init__(self, board):
        self.graph = None
        self.board = board

    # Crée le graph à partir des voisin de chaque pièce
    def save_graph(self):
        """
        Renvoie un dictionnaire de type :
        {
            "node_id" : [neighbors_id]
            ...
        }
        """
        graph = ProcessorHelper.create_graph()

        # On modifie l'état interne du processeur en sauvegardant le graph
        self.graph = Graph(graph)

    # Les performances de cet algorithme dépendent de la manière dont le graph est construit
    # Les noeuds seront pris dans l'ordre donc il ce peut que les solutions soient différentes selon le graph
    # Cet algorithme retourne la première solution qu'il trouve (ce n'est pas forcement la plus optimisée)
    def depth_first_search(self, start_key, path=[]):
        """
        Cet fonction permet de retourner le chemin entre la position actuelle et la première case contenantde la poussière ou un bijou.
        L'algorithme utilisé est le Depth-first search (DFS)
        Cependant, le chemin retourné n'est pas forcement le plus optimisé, ni le plus court.
        Il retourne seulement le premier chemin qu'il trouve.
        """

        # On récupère les coordonnées de la position placée en paramètre
        [start_x, start_y] = ProcessorHelper.get_room_coords_from_id(start_key)

        # On ajoute la nouvelle position à lé précédente afin de retourner le chemin final à la fin de la fonction récurssive
        path = path + [start_key]

        # Condition de fin pour la fonction récurssive
        # Si la pièce contient de la poussière et/ou un bijou
        if self.board.get_board()[start_x][start_y] in [
            Board.DUST,
            Board.JEWEL,
            Board.BOTH,
        ]:
            # On retourne le chemin actuel depuis la position initiale
            # C'est également la condition d'arrêt pour la fonction
            return path

        # Pour chaque voisin de la pièce actuelle placée en paramètre
        for node in self.graph.get_node_neighbors(start_key):

            # On vérifie si la pièce est dans la liste des éléments déjà visités
            if node not in path:

                # On appelle de manière récurssive l'algorithme DFS avec un pièce de départ, le premier voisin de la pièce actuelle
                _tmp_path = self.depth_first_search(node, path)

                # Si on chemin est retourné par la fonction
                if _tmp_path:

                    # On retourne le chemin
                    return _tmp_path

        # Sinon, on retourne None
        return None

    # Exploration non informée
    # Ici, l'algo retourne la solution la plus courte entre deux noeuds
    def depth_first_search_optimized(self, start_key, path=[]):
        """
        Cette fois-ci, l'algorithme est optimisé dans le sens ou le chemin retourné à la fin est le plus court possible
        L'algorithme est globalement le même que pour la fonction depth_first_search
        La principale différence est que l'on sauvegarde l'ensemble des chemins retournés et on les compares entre eux pour retourner le plus court
        Le chemin retourné correspond donc au chemin le plus court la position actuelle du robot et la pièce contenant de la poussière ou un bijou la plus proche
        """

        # On récupère les coordonnées de la position placée en paramètre
        [start_x, start_y] = ProcessorHelper.get_room_coords_from_id(start_key)

        # On ajoute la nouvelle position à lé précédente afin de retourner le chemin final à la fin de la fonction récurssive
        path = path + [start_key]

        # Condition de fin pour la fonction récurssive
        # Si la pièce contient de la poussière et/ou un bijou
        if self.board.get_board()[start_x][start_y] in [
            Board.DUST,
            Board.JEWEL,
            Board.BOTH,
        ]:
            # On retourne le chemin actuel depuis la position initiale
            # C'est également la condition d'arrêt pour la fonction
            return path

        # On crée une variable pour sauvegarder le chemin le plus court
        shortest_path = None

        # Pour chaque voisin de la pièce actuelle placée en paramètre
        for node in self.graph.get_node_neighbors(start_key):

            # On vérifie si la pièce est dans la liste des éléments déjà visités
            if node not in path:

                # On appelle de manière récurssive l'algorithme DFS avec un pièce de départ, le premier voisin de la pièce actuelle
                _tmp_path = self.depth_first_search_optimized(node, path)

                # Si on chemin est retourné par la fonction
                if _tmp_path:

                    # On le compare avec le chemin le plus court précédemment sauvegardé
                    if not shortest_path or len(_tmp_path) < len(shortest_path):

                        # Si le nouveau chemin est plus court, on le conserve et un supprime l'ancien
                        shortest_path = _tmp_path

        # On retourne le chemin le plus court
        return shortest_path
