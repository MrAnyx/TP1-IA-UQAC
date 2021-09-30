from objects.Board import Board
from objects.Window import Window
from objects.Robot import Robot
from threading import *
import time

# TODO Commenter le code

b = Board()
r = Robot(b, Robot.NOT_INFORMED)
w = Window(500, 500, False, "TP1 IA", b, r)


def update_env():
    global r, b
    while r.energy > 0:
        b.random_dust_jewel()
        time.sleep(1)


def update_robot():
    global r, b
    while r.energy > 0:
        goal = r.select_nearest_not_empty_room()
        r.reach_selected_room(goal)

        if r.is_on_goal(goal):
            r.clean_or_take(goal)

        r.display_current_energy()
        time.sleep(1)


t2 = Thread(target=update_robot, args=[])
t1 = Thread(target=update_env, args=[])

t2.start()
t1.start()

while r.energy > 0:
    w.display_board()
    time.sleep(1)

w.mainloop()
