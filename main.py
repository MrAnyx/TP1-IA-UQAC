from objects.Board import Board
from objects.Window import Window
from objects.Robot import Robot
from threading import *
import time

# Todo: Commenter le code

b = Board()
r = Robot(b)

w = Window(500, 500, False, "TP1 IA", b, r)

# _counter = 1

def update_env():
   global r, b
   while(r.energy > 0):
      b.random_dust_jewel()
      time.sleep(1)

def update_window():
   global w, r
   while r.energy > 0:
      w.display_board()
      time.sleep(.5)

def update_robot():
   global r
   while(r.energy > 0):
      goal = r.select_nearest_not_empty_room()
      r.reach_selected_room(goal)
      
      if(r.is_on_goal(goal)):
         r.clean_or_take(goal)

      r.display_current_energy()
      time.sleep(.5)

t1 = Thread(target=update_env, args=[])
t2 = Thread(target=update_robot, args=[])
t3 = Thread(target=update_window, args=[])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


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

w.mainloop()