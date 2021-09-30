class WindowHelper:
    @staticmethod
    def display_board(board, window, robot):
        window.canvas.delete("all")
        color = None
        for i in range(5):
            for j in range(5):
                if board.get_board()[i][j] == 0:
                    color = "#f3f3f3"  # Rien
                elif board.get_board()[i][j] == 1:
                    color = "#2288ba"  # Bijoux
                elif board.get_board()[i][j] == 2:
                    color = "#865f3e"  # Poussière
                elif board.get_board()[i][j] == 3:
                    color = "#8eba4f"  # Poussière + Bijoux

                _rect = window.canvas.create_rectangle(
                    i * 100,
                    j * 100,
                    (i + 1) * 100,
                    (j + 1) * 100,
                    fill=color,
                    tags=f"rect-{robot.processor.get_room_id_from_coords([i, j])}",
                )

                _text = window.canvas.create_text(
                    i * 100 + 50,
                    j * 100 + 50,
                    text=i + 5 * j,
                    fill="black",
                    font=("Helivica 13 bold"),
                    tags=f"text-{robot.processor.get_room_id_from_coords([i, j])}",
                )

        # On affiche le robot
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
        window.canvas.delete(
            f"rect-{robot.processor.get_room_id_from_coords(new_state)}",
        )
        window.canvas.delete(
            f"text-{robot.processor.get_room_id_from_coords(new_state)}",
        )

        color = None
        if board.get_board()[new_state[0]][new_state[1]] == 0:
            color = "#f3f3f3"  # Rien
        elif board.get_board()[new_state[0]][new_state[1]] == 1:
            color = "#2288ba"  # Bijoux
        elif board.get_board()[new_state[0]][new_state[1]] == 2:
            color = "#865f3e"  # Poussière
        elif board.get_board()[new_state[0]][new_state[1]] == 3:
            color = "#8eba4f"  # Poussière + Bijoux

        _rect = window.canvas.create_rectangle(
            new_state[0] * 100,
            new_state[1] * 100,
            (new_state[0] + 1) * 100,
            (new_state[1] + 1) * 100,
            fill=color,
            tags=f"rect-{robot.processor.get_room_id_from_coords(new_state)}",
        )

        _text = window.canvas.create_text(
            new_state[0] * 100 + 50,
            new_state[1] * 100 + 50,
            text=new_state[0] + 5 * new_state[1],
            fill="black",
            font=("Helivica 13 bold"),
            tags=f"text-{robot.processor.get_room_id_from_coords(new_state)}",
        )

        if [robot.x, robot.y] == new_state:
            window.canvas.delete(
                f"robot-{robot.processor.get_room_id_from_coords(new_state)}",
            )
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
    def display_updated_robot_position(board, window, robot, prev_room, next_room):
        window.canvas.delete(
            f"robot-{robot.processor.get_room_id_from_coords(prev_room)}",
        )

        _rect = window.canvas.create_rectangle(
            next_room[0] * 100 + 25,
            next_room[1] * 100 + 25,
            (next_room[0] * 100) + 75,
            (next_room[1] * 100) + 75,
            fill="#888",
            tags=f"robot-{robot.processor.get_room_id_from_coords(next_room)}",
        )

        # On update le canvas pour que les nouvelles modifs soient prises en compte
        window.update()
