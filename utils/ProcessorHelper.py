# Auteur : Robin Bidanchon

import math


class ProcessorHelper:

    # Permet de convertir l'indice d'une pièce en coordonnées
    @staticmethod
    def get_room_coords_from_id(id):
        """
        Par exemple, l'indice 2 correspond aux coordonnées : [0, 2]
        """
        return [id % 5, math.floor(id / 5)]

    # Permet de convertir les coordonnées d'une pièce en indice
    @staticmethod
    def get_room_id_from_coords(coords):
        """
        Par exemple, les coordonnées [1, 0] correspondent à l'indice 5
        """
        return coords[0] + (coords[1] * 5)

    # Permet de récupérer les voisins d'une case à partir du board initial
    @staticmethod
    def get_neighbor_rooms(current):
        neighbor = []

        # Si on n'est pas sur le bord de gauche
        if current[0] > 0:
            neighbor.append([current[0] - 1, current[1]])  # [x-1, y]

        # Si on n'est pas sur le bord de droite
        if current[0] < 4:
            neighbor.append([current[0] + 1, current[1]])  # [x+1, y]

        # Si on n'est pas sur le bord du haut
        if current[1] > 0:
            neighbor.append([current[0], current[1] - 1])  # [x, y-1]

        # Si on n'est pas sur le bord du bas
        if current[1] < 4:
            neighbor.append([current[0], current[1] + 1])  # [x, y+1]

        return neighbor

    # Crée le graph à partir des voisin de chaque pièce
    @staticmethod
    def create_graph():
        """
        Renvoie un dictionnaire de type :
        {
            "node_id" : [neighbors_id]
            ...
        }
        """
        graph = {}
        # On parcourt toutes les pièces
        for i in range(5):
            for j in range(5):
                # On récupère les voisins de la pièce actuelle
                neighbors = ProcessorHelper.get_neighbor_rooms([i, j])
                # On récupère son indice
                id = ProcessorHelper.get_room_id_from_coords([i, j])
                # Pour l'ensemble des voisins de la pièce actuelle, on convertit les coordonnées en indice avec la fonction map
                neighbors_ids = list(
                    map(
                        lambda el: ProcessorHelper.get_room_id_from_coords(el),
                        neighbors,
                    )
                )
                # Pour la pièce actuelle, on indique les voisins possibles
                graph[id] = neighbors_ids

        return graph

    # Cette fonction permet de connaitre l'ensemble des pièces qui contiennent de la poussière et/ou un bijou
    @staticmethod
    def get_not_empty_room(board):
        not_empty_room = []

        # Pour chaque pièce du manoir
        for i in range(5):
            for j in range(5):

                # Si l'état de la pièce est différent de 0, c'est à dire, si la pièce contient de la poussière et/ou un bijou
                if board[i][j] != 0:

                    # On ajoute la pièce actuelle dans la liste
                    not_empty_room.append([i, j])

        # On retourne la liste des pièces qui ne sont pas vides
        return not_empty_room

    # Cette fonction permet de sélectionner la pièce la plus proche en fonction de la norme euclidienne
    # Comme indiqué par le décorateur ci-dessous, cette fonction n'est plus utilisée
    @staticmethod
    def select_nearest_not_empty_room(current_position, board):

        #  On récupère l'ensemble des pièces qui ne sont pas vides
        not_empty_room = ProcessorHelper.get_not_empty_room(board)

        # S'il n'y en a pas
        if len(not_empty_room) == 0:
            # On retourne -1
            return -1
        else:
            # On parcourt chacune des pièces qui ne sont pas vides
            for idx, room in enumerate(not_empty_room):

                # On calcule la norme Euclidienne entre les la position du robot et la pièce
                _min = math.sqrt(
                    math.pow(room[0] - current_position[0], 2)
                    + math.pow(room[1] - current_position[1], 2)
                )

                # Si la nouvelle valeur que l'on vient de calculer et inférieur à la précédente
                if idx == 0 or _min < min:

                    # On la sauvegarde l'indice et la valeur de la norme
                    min = _min
                    index = idx

        # On retourne les coordonnées de la pièce la plus proche
        return not_empty_room[index]
