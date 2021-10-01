# Auteur : Robin Bidanchon

import json

from objects.Board import Board
from objects.Graph import Graph
from objects.Robot import Robot
from objects.Window import Window

# Ce fichier permet de simplement tester des fonctionnalités en cours de développement

b = Board()
b.board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
r = Robot(b, Robot.NOT_INFORMED)

r.x = 3
r.y = 3
print(r.find_best_path())
