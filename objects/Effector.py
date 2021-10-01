class Effector:
    """
    La classe Effector permet de représenter un effecteur.
    Cette classe permet à l'agent d'agir sur l'environnement.
    """

    def __init__(self, board):
        self.board = board

    def clean(self, goal):
        """
        Aspire les élements de la pièce, poussière et bijoux.
        """
        self.board.clean(goal)

    def take(self, goal):
        """
        Ramasse un bijou s'il y en a.
        """
        self.board.take(goal)
