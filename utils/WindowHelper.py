class WindowHelper:
    """
    Cette classe permet de gérer plus facilement l'affichage du manoir et du robot dans la fenêtre
    Les méthodes de cette classe permettent notamment de mettre à jour uniquement les pièces qui changent d'état.
    De même pour le robot
    """

    @staticmethod
    def display_board(board, window, robot):
        """
        Cette fonction permet d'effectuer le premier affichage lorsque la fenêtre principale vient d'être affichée
        L'ensemble des pièces ainsi que la position initiale du robot sont utilisées pour gérer l'affichage
        """

        # On supprime tous les éléments précédemment affichés du canvas
        window.canvas.delete("all")

        color = None

        # Pour chaque pièce du manoir
        for i in range(5):
            for j in range(5):

                # On définie la couleur du rectangle qui sera affiché dans le canvas en fonction de l'état de la pièce
                # Poussière -> Marron
                # Bijou -> Bleu
                # Poussière ET Bijou -> Vert
                # Rien -> Gris
                if board.get_board()[i][j] == 0:
                    color = "#f3f3f3"  # Rien
                elif board.get_board()[i][j] == 1:
                    color = "#2288ba"  # Bijoux
                elif board.get_board()[i][j] == 2:
                    color = "#865f3e"  # Poussière
                elif board.get_board()[i][j] == 3:
                    color = "#8eba4f"  # Poussière + Bijoux

                # On crée un rectangle correspondant à la pièce actuelle
                _rect = window.canvas.create_rectangle(
                    i * 100,  # Position de l'angle supérieur gauche en X
                    j * 100,  # Position de l'angle supérieur gauche en Y
                    (i + 1) * 100,  # Position de l'angle inférieur droit en X
                    (j + 1) * 100,  # Position de l'angle inférieur droit en Y
                    fill=color,
                    tags=f"rect-{robot.processor.get_room_id_from_coords([i, j])}",
                )

                # On crée l'élément texte pour afficher l'indice de la pièce
                _text = window.canvas.create_text(
                    i * 100 + 50,  # Position en X
                    j * 100 + 50,  # Position en Y
                    text=robot.processor.get_room_id_from_coords([i, j]),
                    fill="black",
                    font=("Helivica 13 bold"),
                    tags=f"text-{robot.processor.get_room_id_from_coords([i, j])}",
                )

        # On affiche le robot au centre de la pièce ou il se trouve
        _rect = window.canvas.create_rectangle(
            robot.x * 100 + 25,
            robot.y * 100 + 25,
            (robot.x * 100) + 75,
            (robot.y * 100) + 75,
            fill="#888",
            tags=f"robot-{robot.processor.get_room_id_from_coords([robot.x, robot.y])}",
        )

        # On update le canvas pour que les nouvelles modifs soient prises en compte
        window.update()

    @staticmethod
    def display_updated_room(board, window, robot, new_state):
        """
        Cette fonction permet de mettre à jour l'affichage d'une seule pièce lorsque celle-ci change d'état
        Ainsi, il n'y aura qu'une seule pièce à mettre à jour plutôt que l'intégralité des pièces
        """

        # On supprime le précédent rectangle correspondant à la pièce qui a changé d'état
        window.canvas.delete(
            f"rect-{robot.processor.get_room_id_from_coords(new_state)}",
        )
        # On supprime le précédent texte correspondant à l'indice de la pièce qui a changé d'état
        window.canvas.delete(
            f"text-{robot.processor.get_room_id_from_coords(new_state)}",
        )

        color = None

        # On définie la couleur du rectangle qui sera affiché dans le canvas en fonction de l'état de la pièce
        # Poussière -> Marron
        # Bijou -> Bleu
        # Poussière ET Bijou -> Vert
        # Rien -> Gris
        if board.get_board()[new_state[0]][new_state[1]] == 0:
            color = "#f3f3f3"  # Rien
        elif board.get_board()[new_state[0]][new_state[1]] == 1:
            color = "#2288ba"  # Bijoux
        elif board.get_board()[new_state[0]][new_state[1]] == 2:
            color = "#865f3e"  # Poussière
        elif board.get_board()[new_state[0]][new_state[1]] == 3:
            color = "#8eba4f"  # Poussière + Bijoux

        # On crée un rectangle correspondant à la pièce actuelle
        _rect = window.canvas.create_rectangle(
            new_state[0] * 100,  # Position de l'angle supérieur gauche en X
            new_state[1] * 100,  # Position de l'angle supérieur gauche en Y
            (new_state[0] + 1) * 100,  # Position de l'angle inférieur droit en X
            (new_state[1] + 1) * 100,  # Position de l'angle inférieur droit en Y
            fill=color,
            tags=f"rect-{robot.processor.get_room_id_from_coords(new_state)}",
        )

        # On crée l'élément texte pour afficher l'indice de la pièce
        _text = window.canvas.create_text(
            new_state[0] * 100 + 50,  # Position en X
            new_state[1] * 100 + 50,  # Position en Y
            text=robot.processor.get_room_id_from_coords(new_state),
            fill="black",
            font=("Helivica 13 bold"),
            tags=f"text-{robot.processor.get_room_id_from_coords(new_state)}",
        )

        # Si le robot est situé dans la pièce qui a changé d'état, on affiche a nouveau le robot pour qu'il soit visible dans le canvas
        if [robot.x, robot.y] == new_state:

            # On supprime le précédent robot (à son ancienne position)
            window.canvas.delete(
                f"robot-{robot.processor.get_room_id_from_coords(new_state)}",
            )

            # On crée le rectangle correspondant au robot à sa nouvelle position
            _rect = window.canvas.create_rectangle(
                robot.x * 100 + 25,  # Position de l'angle supérieur gauche en X
                robot.y * 100 + 25,  # Position de l'angle supérieur gauche en Y
                (robot.x * 100) + 75,  # Position de l'angle inférieur droit en X
                (robot.y * 100) + 75,  # Position de l'angle inférieur droit en Y
                fill="#888",
                tags=f"robot-{robot.processor.get_room_id_from_coords([robot.x, robot.y])}",
            )

        # On update le canvas pour que les nouvelles modifs soient prises en compte
        window.update()

    @staticmethod
    def display_updated_robot_position(board, window, robot, prev_room, next_room):
        """
        Cette fonction permet de ne mettre que la position du robot indépendemment du reste pour éviter de supprimer puis d'afficher à nouveau tous les éléments
        """

        # On supprime le précédent robot (à son ancienne position)
        window.canvas.delete(
            f"robot-{robot.processor.get_room_id_from_coords(prev_room)}",
        )

        # On crée le rectangle correspondant au robot à sa nouvelle position
        _rect = window.canvas.create_rectangle(
            next_room[0] * 100 + 25,  # Position de l'angle supérieur gauche en X
            next_room[1] * 100 + 25,  # Position de l'angle supérieur gauche en Y
            (next_room[0] * 100) + 75,  # Position de l'angle inférieur droit en X
            (next_room[1] * 100) + 75,  # Position de l'angle inférieur droit en Y
            fill="#888",
            tags=f"robot-{robot.processor.get_room_id_from_coords(next_room)}",
        )

        # On update le canvas pour que les nouvelles modifs soient prises en compte
        window.update()
