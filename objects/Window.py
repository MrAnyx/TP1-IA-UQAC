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
      self.window.resizable(width = self.resizable, height = self.resizable)
      self.window.title(self.title)

   def create_canvas(self):
      self.canvas = Canvas(self.window, height=self.height, width=self.width)
      self.canvas.pack()
      self.update()

   def mainloop(self):
      self.window.mainloop()

   def update(self):
      self.window.update()

   def display_board(self):
      # self.canvas.delete("all")
      color = None
      for i in range(5):
         for j in range(5):
            if(self.board.get_board()[i][j] == 0): color = "#f3f3f3"    # Rien
            elif(self.board.get_board()[i][j] == 1): color = "#2288ba"  # Bijoux
            elif(self.board.get_board()[i][j] == 2): color = "#865f3e"  # Poussière
            elif(self.board.get_board()[i][j] == 3): color = "#8eba4f"  # Poussière + Bijoux

            _rect = self.canvas.create_rectangle(i*100, j*100, (i+1)*100, (j+1)*100, fill=color)
      
      # On affiche le robot
      _rect = self.canvas.create_rectangle(
         self.robot.x*100+25,
         self.robot.y*100+25,
         (self.robot.x*100)+75,
         (self.robot.y*100)+75,
         fill="#000"
      )

      # On update le canvas pour que les nouvelles modifs soient prises en compte
      self.update()

   def get_window(self):
      return self.window

   def get_canvas(self):
      return self.canvas