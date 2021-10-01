from objects.Board import Board
from objects.Window import Window
from objects.Agent import Agent
from objects.State import State
from objects.Processor import Processor
import threading
import time
from utils.WindowHelper import WindowHelper

# TODO Commenter le code

b = Board()
a = Agent(b, State(0, 0, 0), Processor(0))
w = Window(500, 500, False, "TP1 IA", b, a)

WindowHelper.display_board(b, w, a)


def update_env():
    global r, b
    while a.energy > 0:
        new_state = b.random_dust_jewel()
        WindowHelper.display_updated_room(b, w, a, new_state[0])
        WindowHelper.display_updated_room(b, w, a, new_state[1])
        time.sleep(2)


def update_agent():
    global a
    while a.energy > 0:
        a.observe_environment()
        a.update_my_state()
        a.choose_an_action()
        # a.just_do_it()
        time.sleep(1)

        for action in a.actions:
            if action in [
                Agent.MOVE_UP,
                Agent.MOVE_DOWN,
                Agent.MOVE_LEFT,
                Agent.MOVE_RIGHT,
            ]:
                prev_room = [a.x, a.y]

                if action == Agent.MOVE_UP:
                    a.move_up()
                elif action == Agent.MOVE_DOWN:
                    a.move_down()
                elif action == Agent.MOVE_LEFT:
                    a.move_left()
                elif action == Agent.MOVE_RIGHT:
                    a.move_right()

                WindowHelper.display_updated_robot_position(
                    b, w, a, prev_room, [a.x, a.y]
                )
            elif action == Agent.CLEAN:
                a.clean()
                WindowHelper.display_updated_room(b, w, a, [a.x, a.y])
            elif action == Agent.TAKE:
                a.take()
                WindowHelper.display_updated_room(b, w, a, [a.x, a.y])
            time.sleep(1)


t1 = threading.Thread(target=update_env, args=[])
t2 = threading.Thread(target=update_agent, args=[])

t1.start()
t2.start()

w.mainloop()
