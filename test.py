from objects.Board import Board
from objects.Window import Window
from objects.Robot import Robot
import json
from objects.Graph import Graph

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
