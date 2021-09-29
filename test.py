from objects.Board import Board
from objects.Window import Window
from objects.Robot import Robot
import json
from objects.Graph import Graph

b = Board()
r = Robot(b, Robot.NOT_INFORMED)

r.x = 0
r.y = 0
print(r.search(24))

# print(json.dumps(graph.nodes, indent=3))

## TODO Ajouter l'exploration
