import random
from objects.Sensor import Sensor
from objects.Effector import Effector
from objects.Node import Node


class Agent:
    """
    La classe Agent représente l'agent intelligent qui peut intéragir et parcourir son environnement.
    Il possède des coordonnées x et y afin de pouvoir le localiser.
    Il possède également un compteur car, chacune des actions qu'il fait lui coût un point d'énergie
    Il possède un capteur pour observer son environnement et un effecteur pour agir sur celui-ci
    """

    MOVE_UP = "UP"
    MOVE_DOWN = "DOWN"
    MOVE_RIGHT = "RIGHT"
    MOVE_LEFT = "LEFT"
    TAKE = "TAKE"
    CLEAN = "CLEAN"

    def __init__(self, board, start_state, processor, optimized=True, energy=200):
        self.x = random.randint(0, 4)
        self.y = random.randint(0, 4)
        self.sensor = Sensor(board)
        self.effector = Effector(board)
        self.energy = energy
        self.start_state = start_state
        self.processor = processor
        self.optimized = optimized

    ### Actions possibles ###

    def move_up(self):
        self.y = self.y - 1
        self.energy = self.energy - 1

    def move_down(self):
        self.y = self.y + 1
        self.energy = self.energy - 1

    def move_right(self):
        self.x = self.x + 1
        self.energy = self.energy - 1

    def move_left(self):
        self.x = self.x - 1
        self.energy = self.energy - 1

    def take(self):
        self.effector.take([self.x, self.y])
        self.energy = self.energy - 1

    def clean(self):
        self.effector.clean([self.x, self.y])
        self.energy = self.energy - 1

    def observe_environment(self):
        self.board_state, self.board_perf_metric = self.sensor.observe_environment()
        print("Mesure de performance de l'environnement : ", self.board_perf_metric)

    def update_my_state(self):
        pass

    def choose_an_action(self):
        # Initialisation du processeur
        self.processor.board = self.board_state

        # Initialisation de l'état initial
        self.start_state.position = [self.x, self.y]
        self.start_state.dirt_number = self.processor.get_board_dirt_number()
        self.start_state.room_state = self.board_state[self.x][self.y]
        self.start_state.cleaned_rooms = []

        # Initialisation du noeud racine
        start_node = Node(self.start_state)

        if self.optimized:
            # Pour le DFS optimisé, il est nécessaire de retenir le coût
            best_so_far = {
                "dirt_number": self.processor.get_board_dirt_number(),
                "actions": [],
                "cost": 15,
            }
            self.actions = None
            self.actions = self.processor.depth_first_search_optimized(
                start_node, best_so_far
            )
        else:
            best_so_far = {
                "dirt_number": self.processor.get_board_dirt_number(),
                "actions": [],
            }
            self.actions = None
            self.actions = self.processor.depth_first_search(start_node, best_so_far)

        # S'il n'y a pas de suite d'action qui nettoie tout le manoir
        if self.actions is None:

            # On récupére le premier meilleur chemin trouvé
            self.actions = best_so_far["actions"]

        print("Nouveau parcours : ", self.actions)

    def just_do_it(self):
        for action in self.actions:
            if action == self.MOVE_UP:
                self.move_up()
            elif action == self.MOVE_DOWN:
                self.move_down()
            elif action == self.MOVE_LEFT:
                self.move_left()
            elif action == self.MOVE_RIGHT:
                self.move_right()
            elif action == self.CLEAN:
                self.clean()
            elif action == self.TAKE:
                self.take()
