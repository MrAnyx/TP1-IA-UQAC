# Auteur : Robin Bidanchon

import math
import random

from utils.Decorator import deprecated


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
        # On crée un tableau 2D (de 5 par 5) pour symboliser le manoir
        self.board = [[0 for j in range(5)] for i in range(5)]

    @deprecated
    def _init_board(self):
        # Pour chaque pièce du manoir
        for i in range(5):
            for j in range(5):
                # On génère aléatoirement de la poussière, un bijou et les deux
                self.board[i][j] = random.randint(0, 2)

    def random_dust_jewel(self):
        """
        Cette fonction permet de sélectionner une pièce de manière aléatoire et d'y positionner de la poussière ou un bijou de manière aléatoire également
        Dans le cas ou une pièce contient déjà de la poussière et qu'on y ajoute un bijou, alors la pièce finale contiendra de la poussière ET un bijou
        """

        # On séléctionne aléatoirement une pièce dans le manoir
        _x = random.randint(0, 4)
        _y = random.randint(0, 4)

        # On génère une probabilité entre 0 et 1
        prob = random.random()

        # Si la probabilité est < 1/3 ET que la pièce ne contient ni de la poussière, ni de la poussière ET un bijou
        if prob < 0.33 and self.board[_x][_y] not in [2, 3]:
            # Alors on ajoute de la poussière à la pièce sélectionnée
            self.board[_x][_y] = self.board[_x][_y] + 2

        # Si la probabilité est > 2/3 ET que la pièce ne contient ni un bijou, ni de la poussière ET un bijou
        elif prob > 0.66 and self.board[_x][_y] not in [1, 3]:
            # Alors on ajoute un bijou à la pièce sélectionnée
            self.board[_x][_y] = self.board[_x][_y] + 1

        # On retourne les coordonnées de la pièce qui a été modifiée
        return [_x, _y]

    # Getter pour le board
    # Permet de récuperer l'état du board dans avoir à faire Board.board
    def get_board(self):
        return self.board
