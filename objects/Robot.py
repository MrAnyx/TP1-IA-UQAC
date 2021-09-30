import json
import random
import math
from utils.Decorator import deprecated
from objects.Processor import Processor
import time


class Robot:
    """
    La classe Robot représent l'agent intelligent qui peut intéragir et parcourir son environnement.
    Il possède des coordonnées x et y afin de pouvoir le localiser.
    Il possède également un compteur car, chacune des actions qu'il fait lui coût un point d'énergie
    Enfin, pour se déplacer et prendre des décisions, il doit connaitre son environnement
    """

    INFORMED = 1
    NOT_INFORMED = 2

    def __init__(self, board, search_type, energy=200):
        self.x = random.randint(0, 4)
        self.y = random.randint(0, 4)
        self.energy = energy
        self.board = board
        self.room_cleaned = 0
        self.search_type = search_type

        # Permet de savoir si le robot est en train de rejoindre une  ou en train d'effectuer une exploration
        self.will_explore = True
        self.is_reaching_room = False

        self.path = []
        self.goal = None

        # Le processeur du roobt permet d'effectuer les actions de recherche / sélection de la bonne pièce
        self.processor = Processor(self.board)

    def move_up(self):
        self.y = self.y - 1

    def move_down(self):
        self.y = self.y + 1

    def move_right(self):
        self.x = self.x + 1

    def move_left(self):
        self.x = self.x - 1

    @deprecated
    def _get_not_empty_room(self):
        not_empty_room = []
        for i in range(5):
            for j in range(5):
                if self.board.get_board()[i][j] != 0:  # Si la pièce n'est pas vide
                    not_empty_room.append([i, j])

        return not_empty_room

    @deprecated
    def select_nearest_not_empty_room(self):
        not_empty_room = self._get_not_empty_room()
        if len(not_empty_room) == 0:
            return -1
        else:
            for idx, room in enumerate(not_empty_room):
                _min = math.sqrt(
                    math.pow(room[0] - self.x, 2) + math.pow(room[1] - self.y, 2)
                )
                if idx == 0 or _min < min:
                    min = _min
                    index = idx

        return not_empty_room[index]

    def reach_selected_room(self, room_coord):
        if self.is_on_goal(room_coord) or not room_coord:
            return
        else:
            if room_coord[1] < self.y:
                self.move_up()
            elif room_coord[1] > self.y:
                self.move_down()
            elif room_coord[0] < self.x:
                self.move_left()
            elif room_coord[0] > self.x:
                self.move_right()

            self.energy -= 1

    def is_on_goal(self, goal):
        if [self.x, self.y] == goal:
            return True
        return False

    def clean_or_take(self, goal):
        current_room_state = self.board.get_board()[goal[0]][goal[1]]
        if current_room_state in [1, 2]:
            self.energy -= 1
        elif current_room_state == 3:
            self.energy -= 2

        self.room_cleaned += 1
        self.board.get_board()[goal[0]][goal[1]] = 0
        self.goal = None

    def display_current_state(self):
        print(f"path : {self.path}")
        print(f"goal : {self.goal}")
        print(f"Current position coords : {[self.x, self.y]}")
        if self.energy > 10:
            print(f"Current energy of the robot : {self.energy}")
        elif self.energy > 0 and self.energy <= 10:
            print(f"I'm running out of energy, i will die soon : {self.energy}")
        else:
            print(f"Oops, i died ☠. I cleaned {self.room_cleaned} rooms")

        print("")

    def _goal_is_coords(self, goal):
        if type(goal) is int:
            return False
        else:
            return True

    def _convert_path_with_goal_type(self, path, goal):
        return (
            path
            if not self._goal_is_coords(goal)
            else list(
                map(
                    lambda room_id: self.processor.get_room_coords_from_id(room_id),
                    path,
                )
            )
        )

    def find_best_path(self):
        self.processor.create_graph()
        current_position_id = self.processor.get_room_id_from_coords([self.x, self.y])

        if self.search_type == self.NOT_INFORMED:
            path = self.processor.depth_first_search_optimized(current_position_id)
        else:
            path = self.processor.greedy_search()

        return path

    def explore(self):
        print("I'm exploring the board to find the best path")
        time.sleep(3)

        path = self.find_best_path()

        if path:
            self.will_explore = False
            self.is_reaching_room = True
            self.path = path
            self.goal = self.processor.get_room_coords_from_id(path[-1])
