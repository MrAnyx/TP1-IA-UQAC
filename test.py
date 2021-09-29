from objects.Board import Board
from objects.Window import Window
from objects.Robot import Robot
import json

b = Board()
r = Robot(b, Robot.NOT_INFORMED)

# print(json.dumps(b.create_graph(), indent=3))

graph = b.create_graph()

# Les performances de cet algorithme dépendent de la manière dont le graph est construit
# def depth_first_search(graph, start, end, path=[]):
#     path.append(start)
#     if start == end:
#         return path
#     shortest = None
#     for node in graph[start]:
#         if node not in path:
#             newpath = depth_first_search(graph, node, end, path)
#             if newpath:
#                 return newpath

#     return None


def depth_first_search_optimized(graph, start, end, path=[]):
    path = path.append(start)
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = depth_first_search_optimized(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


print(depth_first_search_optimized(graph, 11, 9))
