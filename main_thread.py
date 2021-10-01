# Auteur : Robin Bidanchon

from objects.Board import Board
from objects.Window import Window
from objects.Robot import Robot
import threading
import time
from utils.WindowHelper import WindowHelper
from utils.ProcessorHelper import ProcessorHelper


# Création des objets représentant l'expérience
b = Board()  # Correspond au manoir
r = Robot(b, Robot.INFORMED)  # Correspond à notre agent intelligent
w = Window(500, 500, False, "TP1 IA", b, r)  # Objet pour gérer notre fenêtre

# Premier affichage du manoir dans la fenêtre
WindowHelper.display_board(b, w, r)

# Fonction exécutée par le Thread lié à la gestion de l'environnement
def update_env():

    # On récupères la variables globales du robot et du board (manoir)
    global r, b

    while r.energy > 0:

        # On génère ajoute aléatoirement de la poussière ou un bijou dans une pièce
        # Si la pièce contient déjà de la poussière et qu'on ajoute un bijou, alors dans la pièce, il y aura de la poussière ET un bijou
        new_state = b.random_dust_jewel()

        # On met à jour l'affichage de la fenêtre en ne mettant à jour que la pièce qui a changé d'état
        WindowHelper.display_updated_room(b, w, r, new_state)

        # On répète l'opération toutes les 2 secondes
        time.sleep(2)


# Fonction exécutée par le Thread lié à la gestion du robot
def update_robot():

    # On récupères la variables globales du robot et du board (manoir)
    global r, b

    while r.energy > 0:

        # Si le robot soit faire une exploration
        if r.will_explore:

            # On explore
            # Cette fonction modifie l'état interne du robot en enregistrant le chemin à réaliser ainsi que le but
            r.explore()

        # On affiche l'état du robot :
        #  - Le chemin à suivre
        #  - Le but
        #  - La position courante
        #  - L'énergie actuelle
        r.display_current_state()

        # Si le robot a atteint on but
        if r.is_on_goal(r.goal):

            # On enlève la poussière ou on ramasse le bijou
            # On modifie ensuite l'état interne du robot en indiquant que la prochaine étate qu'il devra réaliser est une exploration car il n'a plus de but
            r.clean_or_take(r.position())

            # On met à jour l'affichage de la fenêtre en ne mettant à jour que la pièce qui a changé d'état
            WindowHelper.display_updated_room(b, w, r, r.position())

        # Si le robot doit suivre le chemin et qu'il possède un chemin à suivre dans son état interne
        if r.is_reaching_room and r.path:

            # On récupère la prochaine pièce à atteindre, c'est à dire la pièce du chemin de son état interne à l'indice 0
            next_room = ProcessorHelper.get_room_coords_from_id(r.path.pop(0))

            # On récupère son ancienne position
            prev_room = r.reach_selected_room(next_room)

            # On met à jour l'affichage du robot dans la fenêtre. On efface le robot à sa précédent position et on affiche sa nouvelle position
            WindowHelper.display_updated_robot_position(b, w, r, prev_room, next_room)

        # On répète ce processus toutes les secondes
        time.sleep(1)


# On crée deux threads :
#  - Un pour la gestion de l'environnement
#  - Un pour la gestion du robot
t1 = threading.Thread(target=update_env)
t2 = threading.Thread(target=update_robot)

# On lance les deux threads
t1.start()
t2.start()

# On laisse la fenêtre affichée dans le cas ou le programme se termine
w.mainloop()
