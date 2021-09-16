import random
import math

# Todo: Inclure un état dans le robot pour déterminer si, dans le cas ou on a deux pièces à la même distance, choisir qu'il préfère la poussière ou le bijou plutot que les deux
# Todo: Ajouter le fait que le robot peut aller plus loin mais faire de la poussière ou un bijou.
class Robot:
    """
    La classe Robot représent l'agent intelligent qui peut intéragir et parcourir son environnement.
    Il possède des coordonnées x et y afin de pouvoir le localiser.
    Il possède également un compteur car, chacune des actions qu'il fait lui coût un point d'énergie
    Enfin, pour se déplacer et prendre des décisions, il doit connaitre son environnement
    """

    def __init__(self, board, energy=50):
        self.x = random.randint(0, 4)
        self.y = random.randint(0, 4)
        self.energy = energy
        self.board = board
        self.room_cleaned = 0

    def move_up(self):
        self.y = self.y - 1

    def move_down(self):
        self.y = self.y + 1

    def move_right(self):
        self.x = self.x + 1

    def move_left(self):
        self.x = self.x - 1

    def __get_not_empty_room(self):
        not_empty_room = []
        for i in range(5):
            for j in range(5):
                if(self.board.get_board()[i][j] != 0):  # Si la pièce n'est pas vide
                    not_empty_room.append([i, j])

        return not_empty_room

    def select_nearest_not_empty_room(self):
        not_empty_room = self.__get_not_empty_room()
        if(len(not_empty_room) == 0): return -1
        else:
            for idx, room in enumerate(not_empty_room):
                _min = math.sqrt(math.pow(room[0] - self.x, 2) + math.pow(room[1] - self.y, 2))
                if(idx == 0 or _min < min): 
                    min = _min
                    index = idx

        return not_empty_room[index]

    def reach_selected_room(self, room_coord):
        if(room_coord == [self.x, self.y] or room_coord == -1): return
        else:
            if(room_coord[1] < self.y): self.move_up()
            elif(room_coord[1] > self.y): self.move_down()
            elif(room_coord[0] < self.x): self.move_left()
            elif(room_coord[0] > self.x): self.move_right()

            self.energy -= 1
    
    def is_on_goal(self, goal):
        if([self.x, self.y] == goal): return True
        return False

    def clean_or_take(self, goal):
        if(goal == -1): return # Il n'y a pas poussière à nettoyer ou de bijou à ramasser
        
        current_room_state = self.board.get_board()[goal[0]][goal[1]]

        if(current_room_state in [1, 2]):
            self.energy -= 1
        elif(current_room_state == 3):
            self.energy -= 2

        self.room_cleaned += 1
        self.board.get_board()[goal[0]][goal[1]] = 0

    def display_current_energy(self):
        if(self.energy > 10):
            print(f"Current energy of the robot : {self.energy}")
        elif(self.energy > 0 and self.energy <= 10):
            print(f"I'm running out of energy, i will die soon : {self.energy}")
        else:
            print(f"Oops, i died ☠. I cleaned {self.room_cleaned} rooms")
