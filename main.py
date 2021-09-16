from objects.Board import Board
from objects.Window import Window
from objects.Robot import Robot
import time

# Todo: Commenter le code

b = Board()
r = Robot(b)
w = Window(500, 500, False, "TP1 IA", b, r)
w.display_board()

_counter = 1

while(r.energy > 0):
   # if(_counter % 2 == 0): b.random_dust_jewel()
   b.random_dust_jewel()

   goal = r.select_nearest_not_empty_room()
   r.reach_selected_room(goal)
   
   if(r.is_on_goal(goal)):
      r.clean_or_take(goal)

   _counter += 1
   w.display_board()
   r.display_current_energy()
   time.sleep(1)

w.mainloop()