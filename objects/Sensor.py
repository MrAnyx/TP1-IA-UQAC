class Sensor :
    """
    La classe Sensor permet de représenter les capteurs.
    Ici, son unique but est de renvoyer l'état de l'environnement.
    """

    def __init__(self, board):
        self.board = board

    def observe_environment(self):
        return self.board.get_board().copy(), self.board.get_performance_metric()