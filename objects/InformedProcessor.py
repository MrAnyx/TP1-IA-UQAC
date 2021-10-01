# Autheur : Vasco Andréassian--Orengo, Robin Bidanchon


import random
import math
from utils.ProcessorHelper import ProcessorHelper
from objects.Triplet import Triplet


class InformedProcessor:
    def __init__(self, board):
        self.board = board.get_board()

    # Retourne la case pleine la plus proche
    def closeDirt(self, board, pos):
        dist = 6
        goal = []
        for i in range(0, 5):
            for j in range(0, 5):
                if board[i][j] in [1, 2, 3]:
                    a = math.sqrt((pos[0] - i) ** 2 + (pos[1] - j) ** 2)
                    if a < dist:
                        goal.append([i, j])
                        dist = a
        return goal

    # Retourne les indices des voisins d'une case
    def getVoisins(self, pos):
        indVoisins = []
        if pos[0] > 0:
            indVoisins.append([pos[0] - 1, pos[1]])
        if pos[0] < 4:
            indVoisins.append([pos[0] + 1, pos[1]])
        if pos[1] > 0:
            indVoisins.append([pos[0], pos[1] - 1])
        if pos[1] < 4:
            indVoisins.append([pos[0], pos[1] + 1])
        return indVoisins

    # Calcule l'heuristique c'est à dire la distance entre le noeud actuel et l'arrivée
    def heuristique(self, pos, goal):
        return math.sqrt((pos[0] - goal[0]) ** 2 + (pos[1] - goal[1]) ** 2)

    # Vérifie si on est arrivée sur une case pleine
    def fin(self, pos, goal):
        if (pos[0] == goal[0]) and (pos[1] == goal[1]):
            return False
        return True

    # Fonction qui renvoie le chemin optimal
    def cheminOpti(self, board, position):

        goal = self.closeDirt(board, position)
        path = []

        if goal != []:
            # Boucle qui s'arrête lorsque le robot est passé sur toutes les cases pleines
            for k in range(1):
                openIndex = []
                closeIndex = []
                arbre = []
                indice = 0
                index = 0
                arbre.append(
                    Triplet(self.heuristique(position, goal[k]), position, -1, -1)
                )

                # Boucle qui s'arrête lorsque le robot est arrivé sur une case pleine
                while self.fin(position, goal[k]):

                    # Indexation des fils directs du noeud
                    indice += 1
                    openIndex.append(indice)
                    arbre[index].setLChild(indice)
                    posVois = self.getVoisins(position)
                    nbVois = len(posVois)
                    for i in range(0, nbVois - 1):
                        keep = True
                        for j in closeIndex:
                            if arbre[j].isPresent(posVois[i]):
                                keep = False
                                break
                        if keep:
                            indice += 1
                            openIndex.append(indice)
                            arbre.append(
                                Triplet(
                                    self.heuristique(posVois[i], goal[k]),
                                    posVois[i],
                                    -1,
                                    indice,
                                )
                            )
                    arbre.append(
                        Triplet(
                            self.heuristique(posVois[-1], goal[k]), posVois[-1], -1, -1
                        )
                    )

                    # Changement du noeud vers celui avec le meilleur f
                    f = 26
                    for i in openIndex:
                        tempf = arbre[i].val
                        if tempf < f:
                            position[0] = arbre[i].pos[0]
                            position[1] = arbre[i].pos[1]
                            f = tempf
                            index = i
                    path.append([position[0], position[1]])
                    closeIndex.append(index)
                    openIndex.remove(index)

                    # Incrémentation du chemin jusqu'à la position actuelle
                    if f > 25:
                        break

        return path

    def greedy_search(self, board, current_position):
        path = self.cheminOpti(board, current_position)
        return path
