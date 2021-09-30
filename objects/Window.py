from tkinter import *


class Window:
    """
    La classe Window permet d'afficher le résultat de l'environement à un instant t
    L'affichage est géré avec Tkinter, une librairie permettant de créer et manipuler des fenêtres en Python
    """

    def __init__(self, width, height, resizable, title, board, robot):
        self.width = width
        self.height = height
        self.resizable = resizable
        self.title = title or "TP1 IA"
        self.window = None
        self.canvas = None
        self.board = board
        self.robot = robot
        self.create_window()
        self.create_canvas()

    def create_window(self):
        self.window = Tk()
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(width=self.resizable, height=self.resizable)
        self.window.title(self.title)

    def create_canvas(self):
        self.canvas = Canvas(self.window, height=self.height, width=self.width)
        self.canvas.pack()
        self.update()

    def mainloop(self):
        self.window.mainloop()

    def update(self):
        self.window.update()

    def get_window(self):
        return self.window

    def get_canvas(self):
        return self.canvas
