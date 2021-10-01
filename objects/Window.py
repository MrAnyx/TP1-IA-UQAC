# Auteur : Robin Bidanchon

from tkinter import *


class Window:
    """
    La classe Window permet d'afficher le résultat de l'environement à un instant t
    L'affichage est géré avec Tkinter, une librairie permettant de créer et manipuler des fenêtres en Python
    """

    def __init__(self, width, height, resizable, title, board, robot):
        # On définie la taille de la fenêtre en nombre de pixels
        self.width = width
        self.height = height
        self.resizable = resizable
        self.title = title
        self.window = None
        self.canvas = None

        # On sauvegarde l'état du robot ainsi que le board (manoir) pour pouvoir les afficher dans la fenêtre
        self.board = board
        self.robot = robot

        # On lance la création de la fenêtre
        self.create_window()

        # On lance la création du canvas dans la fenêtre
        self.create_canvas()

    # Cette fonction permet de créer la fenêtre qui accueillera pa rla suite l'ensembe de l'expérience
    def create_window(self):

        # On crée l'objet Tkinter qui correspond à la fenêtre
        self.window = Tk()

        # On définie ses dimensions
        self.window.geometry(f"{self.width}x{self.height}")

        # On indique si la fenêtre est redimensionnable
        self.window.resizable(width=self.resizable, height=self.resizable)

        # On définine le titre de la fenêtre
        self.window.title(self.title)

    def create_canvas(self):
        """
        Cette fonction permet de créer le canvas dans la fenêtre
        Ce canvas contiendra l'ensemble des formes que l'on devra créer par la suite pour symboliser le robot, les pièces, ...
        """
        self.canvas = Canvas(self.window, height=self.height, width=self.width)
        self.canvas.pack()
        self.update()

    # Cette fonction permet de laisser la fenêtre affichée sur l'écran même lorsque le programme se termine
    def mainloop(self):
        self.window.mainloop()

    def update(self):
        """
        Cette fonction permet de mettre à jour le contenu du canvas
        Ainsi, lorsque l'on effectue des modifications dans le canvas lors du déplacement du robot par exemple, nous devrons appeler cette fonction pour que l'affiche de ce qu'il y a dans le canvas corresponde à l'état actuel de l'expérience
        """
        self.window.update()

    # Cette fonction permet de récuperer la propriété fenêtre sans avoir à faire Board.board
    def get_window(self):
        return self.window

    # Cette fonction permet de récuperer la propriété canvas
    def get_canvas(self):
        return self.canvas
