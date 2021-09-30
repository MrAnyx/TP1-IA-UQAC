from objects.Board import Board
from objects.Window import Window
from objects.Robot import Robot
from threading import *
import time
from utils.WindowHelper import WindowHelper

# TODO Commenter le code

b = Board()
r = Robot(b, Robot.NOT_INFORMED)
w = Window(500, 500, False, "TP1 IA", b, r)

WindowHelper.display_board(b, w, r)


def update_env():
    global r, b
    while r.energy > 0:
        b.random_dust_jewel()
        WindowHelper.display_board(b, w, r)

        time.sleep(2)


def update_robot():
    global r, b
    while r.energy > 0:
        if r.will_explore:
            r.explore()

        r.display_current_state()

        if r.is_on_goal(r.goal):
            r.clean_or_take(r.goal)
            r.is_reaching_room = False
            r.will_explore = True
            WindowHelper.display_board(b, w, r)

        if r.is_reaching_room and r.path:
            next_room = r.processor.get_room_coords_from_id(r.path.pop(0))
            r.reach_selected_room(next_room)
            WindowHelper.display_board(b, w, r)

        time.sleep(1)


t1 = Thread(target=update_env, args=[])
t2 = Thread(target=update_robot, args=[])

t1.start()
t2.start()


w.mainloop()
