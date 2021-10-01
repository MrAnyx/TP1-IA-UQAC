# Auteur : Robin Bidanchon

import json
import math
import random
import time

from utils.Decorator import deprecated
from utils.ProcessorHelper import ProcessorHelper

from objects.InformedProcessor import InformedProcessor
from objects.UninformedProcessor import UninformedProcessor


class Robot:
    """
    La classe Robot représente l'agent intelligent qui peut intéragir et parcourir son environnement.
    Il possède des coordonnées x et y afin de pouvoir le localiser.
    Il possède également un compteur car, chacune des actions qu'il fait lui coût un point d'énergie
    Enfin, pour se déplacer et prendre des décisions, il doit connaitre l'organisation de son environnement

    De plus, l'ensemble des calculs effectués lors de la prise de décision du chemin le plus court son effectués par la classe Processor
    """

    INFORMED = 1
    NOT_INFORMED = 2

    def __init__(self, board, search_type, optimized=True, energy=30):

        # On définie la position initiale du robot de manière aléatoire dans le manoir
        self.x = random.randint(0, 4)
        self.y = random.randint(0, 4)
        self.energy = energy
        self.board = board
        self.room_cleaned = 0
        self.search_type = search_type

        # Permet de savoir si le robot est en train de rejoindre une * ou en train d'effectuer une exploration
        self.will_explore = True
        self.is_reaching_room = False

        # Ces deux attributs permettent de sauvegarder l'état interne du robot
        self.path = []
        self.goal = None

        self.optimized = optimized

        # Le processeur du robot permet d'effectuer les actions de recherche / sélection de la bonne pièce
        # Il se charge d'effectuer les calculs
        self.uninformed_processor = UninformedProcessor(self.board)
        self.informed_processor = InformedProcessor(self.board)

    # Permet de déplacer le robot d'une case vers le haut
    def move_up(self):
        self.y = self.y - 1

    # Permet de déplacer le robot d'une case vers le bas
    def move_down(self):
        self.y = self.y + 1

    # Permet de déplacer le robot d'une case vers la droite
    def move_right(self):
        self.x = self.x + 1

    # Permet de déplacer le robot d'une case vers la gauche
    def move_left(self):
        self.x = self.x - 1

    def position(self):
        return [self.x, self.y]

    # Cette fonction permet d'atteindre une pièce en fonction de ses coordonnées
    def reach_selected_room(self, room_coord):
        """
        Par exemple, on pourrait avoir en paramètre : [3, 2]
        Sachant que la position actuelle du robot est : [2, 2]
        Dans ce cas, la valeur en X de la pièce à atteindre est supérieur à la position en X du robot, donc nous allons le déplacer d'une case vers la droite
        Si le robot se situe déjà sur son but, on ne bouge pas
        """

        # On récupère la position précédente du robot afin de mettre à jour l'affichage dans la fenêtre
        prev_pos = [self.x, self.y]

        # Si le robot de situe déjà sur son but ou que le paramètre room_coord vaut None
        if self.is_on_goal(room_coord) or not room_coord:
            # On ne bouge pas
            return
        else:
            # Si la pièce à atteindre se situe au dessus du robot
            if room_coord[1] < self.y:
                # On bouge le robot vers le haut
                self.move_up()
            # Si la pièce à atteindre se situe en dessous du robot
            elif room_coord[1] > self.y:
                # On bouge le robot vers le bas
                self.move_down()
            # Si la pièce à atteindre se situe sur la gauche du robot
            elif room_coord[0] < self.x:
                # On bouge le robot vers la gauche
                self.move_left()
            # Si la pièce à atteindre se situe sur la droite du robot
            elif room_coord[0] > self.x:
                # On bouge le robot vers la droite
                self.move_right()

            # Si il y a un déplacement, on décrémente la valeur de l'énergie
            self.energy -= 1

        # On retourne la position précédente
        return prev_pos

    # Cette fonction permet de savoir si le robot se situe sur son but final
    def is_on_goal(self, goal):
        # Si les coordonnées du robot correspondent au coordonnées du but
        if [self.x, self.y] == goal:
            return True
        return False

    def clean_or_take(self, goal):
        """
        Cette fonction permet de, en fonction de l'état de la case ou se situe le robot, de récupérer le bijou et de ramasser la poussière
        Cette fonctione ne sera appelé que si le robot a atteint son but, c'est à dire, lorsqu'il se trouve dans la dernière pièce du chemin de son état interne
        """

        # On récupère l'état de la pièce correspondant au but du robot
        # Autrement-dit, est-ce que la pièce contient de la poussière et/ou un bijou
        current_room_state = self.board.get_board()[goal[0]][goal[1]]

        # Si la pièce contient uniquement de la poussière ou uniquement un bijou
        if current_room_state in [1, 2]:
            # On décrémente l'énergie du robot de 1
            self.energy -= 1
        # Si dans la pièce, il y a de la poussière ET un bijou
        elif current_room_state == 3:
            # On décrémente de 2 la valeur de l'énergie
            self.energy -= 2

        # On incrémente la valeur correspondant au nombre de pièce nettoyées par le robot
        self.room_cleaned += 1

        # On met à jour l'état de la pièce ou se situe le robot
        # Autrement-dit, on met la valeur de la pièce à 0
        self.board.get_board()[goal[0]][goal[1]] = 0

        # On réinitialise le but du robot
        self.goal = None

        # On met à jour son état interne
        self.is_reaching_room = False
        self.will_explore = True

    def display_current_state(self):
        """
        Cette fonction permet d'afficher l'état actuel du robot
        On affiche le chemin ainsi que le but qui sauvegardé dans son état interne
        On affiche également sa position actuelle ainsi que son niveau d'énergie
        """
        print(f"path : {self.path}")
        print(f"goal : {self.goal}")
        print(f"will explore : {self.will_explore}")
        print(f"is reaching goal : {self.is_reaching_room}")
        print(f"Current position coords : {[self.x, self.y]}")

        if self.energy > 10:
            print(f"Current energy of the robot : {self.energy}")

        elif self.energy > 0 and self.energy <= 10:
            print(f"I'm running out of energy, i will die soon : {self.energy}")

        else:
            print(f"Oops, i died ☠. I cleaned {self.room_cleaned} rooms")

        print("")

    # Cette fonction permet de vérifier le type de la variable but. Si c'est un indice ou des coordonnées
    @deprecated
    def _goal_is_coords(self, goal):
        if type(goal) is int:
            return False
        else:
            return True

    @deprecated
    def _convert_path_with_goal_type(self, path, goal):
        """
        Cette fonction permet de convertir le type le chemin trouvé par l'algorithme en fonction du type de la variable but
        Si le but est exprimé en coordonnées, le chemin sera lui aussi exprimé en coordonnées
        Si le but est exprimé en indice, le chemin sera lui aussi exprimé en indice
        """
        return (
            path
            if not self._goal_is_coords(goal)
            else list(
                map(
                    lambda room_id: ProcessorHelper.get_room_coords_from_id(room_id),
                    path,
                )
            )
        )

    def find_best_path(self):
        """
        Cette fonction permert de lancer l'algorithme de recherche selon l'état du robot
        Si le robot est dans un état non-informé, alors l'algorithme non-informé sera lancé et inversement
        Dans les deux cas, le chemin vers une pièce non vide sera retourné
        """

        # On génère le graph correspondant à la disposition des pièces dans le manoir

        # On récupère l'indice de la pièce ou se situe le robot en fonction de ses coordonnées actuelles
        current_position_id = ProcessorHelper.get_room_id_from_coords(self.position())

        # Si le robot n'est pas informé
        if self.search_type == self.NOT_INFORMED:

            self.uninformed_processor.save_graph()
            # Si le robot est optimisé
            if self.optimized:
                # On récupère le chemin vers la pièce non cide la plus proche
                path = self.uninformed_processor.depth_first_search_optimized(
                    current_position_id
                )
            else:
                # Sinon, on récupère le chemin vers la première pièce non vide que l'algorithme DFS trouve
                path = self.uninformed_processor.depth_first_search(current_position_id)

        # Sinon, on effectue une recherche informée
        else:
            self.informed_processor.save_graph()
            path = self.informed_processor.greedy_search(
                self.board.get_board(), self.position()
            )

            if len(path) != 0:
                path = list(
                    map(
                        lambda coords: ProcessorHelper.get_room_id_from_coords(coords),
                        path,
                    )
                )

        # On retourne le chemin vers la pièce
        return path

    #  Cette fonction permet de récuperer le chemin vers une pièce non vide et de mettre à jour l'état interne du robot
    def explore(self):
        print("I'm exploring the board to find the best path\n")

        # On récupère le chemin vers une pièce non vides
        # En fonction de l'état du robot, l'algorithme informé ou non informé sera lancé
        path = self.find_best_path()

        # Si un chemin est trouvé par l'algorithme
        if path:

            # On met à jour l'état interne du robot
            self.will_explore = False
            self.is_reaching_room = True

            if self.search_type == self.NOT_INFORMED:
                # On sauvegarde le chemin
                # Ici, on sauvegarde le chemin uniquement à partir de l'indice 1 car l'indice 0 correspond à la position actuelle du robot
                self.path = path[1:]

            else:
                self.path = path

            # On sauvegarde le but
            self.goal = ProcessorHelper.get_room_coords_from_id(path[-1])
