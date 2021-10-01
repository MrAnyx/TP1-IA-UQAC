from objects.Agent import Agent
from objects.Board import Board


class State:
    def __init__(self, position, dirt_number, room_state, cleaned_rooms=[]):
        self.position = position
        self.dirt_number = dirt_number
        self.room_state = room_state
        self.cleaned_rooms = cleaned_rooms

    def next_state(self, action, board):

        state = None

        if action in [
            Agent.MOVE_UP,
            Agent.MOVE_DOWN,
            Agent.MOVE_LEFT,
            Agent.MOVE_RIGHT,
        ]:

            if action == Agent.MOVE_LEFT:
                next_pos = [self.position[0] - 1, self.position[1]]
            elif action == Agent.MOVE_RIGHT:
                next_pos = [self.position[0] + 1, self.position[1]]
            elif action == Agent.MOVE_DOWN:
                next_pos = [self.position[0], self.position[1] + 1]
            else:
                next_pos = [self.position[0], self.position[1] - 1]

            if (
                next_pos in self.cleaned_rooms
                or board[next_pos[0]][next_pos[1]] == Board.NOTHING
            ):
                next_room_state = Board.NOTHING
            else:
                next_room_state = board[next_pos[0]][next_pos[1]]

            state = State(
                next_pos, self.dirt_number, next_room_state, self.cleaned_rooms
            )

        elif action == Agent.CLEAN:

            next_dirt_number = self.dirt_number
            next_cleaned_rooms = self.cleaned_rooms.copy()
            if self.room_state != Board.NOTHING:
                next_dirt_number = next_dirt_number - 1
                next_cleaned_rooms.append(self.position)

            state = State(
                self.position, next_dirt_number, Board.NOTHING, next_cleaned_rooms
            )

        else:  # action == Agent.TAKE

            next_dirt_number = self.dirt_number
            next_cleaned_rooms = self.cleaned_rooms.copy()
            next_room_state = self.room_state

            if self.room_state == Board.JEWEL:
                next_dirt_number = next_dirt_number - 1
                next_cleaned_rooms.append(self.position)
                next_room_state = Board.NOTHING
            elif self.room_state == Board.BOTH:
                next_room_state = Board.DUST

            state = State(
                self.position, next_dirt_number, next_room_state, next_cleaned_rooms
            )

        return state
