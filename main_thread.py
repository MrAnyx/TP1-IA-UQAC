from objects.Board import Board
from objects.Window import Window
from objects.Robot import Robot
import threading
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
        new_state = b.random_dust_jewel()
        WindowHelper.display_updated_room(b, w, r, new_state)

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

            WindowHelper.display_updated_room(b, w, r, [r.x, r.y])

        if r.is_reaching_room and r.path:
            next_room = r.processor.get_room_coords_from_id(r.path.pop(0))
            prev_room = r.reach_selected_room(next_room)
            WindowHelper.display_updated_robot_position(b, w, r, prev_room, next_room)

        time.sleep(1)


t1 = threading.Thread(target=update_env)
t2 = threading.Thread(target=update_robot)

t1.start()
t2.start()

w.mainloop()
