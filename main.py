from objects.Board import Board
from objects.Window import Window
from objects.Robot import Robot
from utils.Decorator import deprecated
from threading import *
import time

# Todo: Commenter le code
# Todo: Ajouter l'exploration non informé (sans boucle) et informée
# Todo: Faire en sorte de récupérer les bijou / poussière si la case est directement sur notre chemin

b = Board()
r = Robot(b, Robot.NOT_INFORMED)
w = Window(500, 500, False, "TP1 IA", b, r)

print(r.get_neighbor_rooms([0, 1], [[5, 4]]))

# _counter = 1

# while(r.energy > 0):
#    # if(_counter % 2 == 0): b.random_dust_jewel()
#    b.random_dust_jewel()

#    goal = r.select_nearest_not_empty_room()
#    r.reach_selected_room(goal)

#    if(r.is_on_goal(goal)):
#       r.clean_or_take(goal)

#    # _counter += 1
#    w.display_board()
#    r.display_current_energy()
#    time.sleep(1)

# w.mainloop()
