class Effector :

    def __init__(self, board):
        self.board = board

    def clean(self, goal):
        self.board.clean(goal)

    def take(self, goal):
        self.board.take(goal)