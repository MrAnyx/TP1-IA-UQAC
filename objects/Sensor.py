class Sensor :
    """
    La classe Sensor permet de représenter les capteurs.
    Ici, son unique but est de renvoyer l'état de l'environnement.
    """

    def __init__(self, board):
        self.board = board

    def observe_environment(self):
        # Retourne une copie de board pour simuler la lecture à l'instant t
        # Evite qu'il y ait des modifications le temps de prendre une décision dessus
        return self.board.get_board().copy(), self.board.get_performance_metric()