class WindowHelper:
    @staticmethod
    def display_board(board, window, robot):
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
                    i * 100, j * 100, (i + 1) * 100, (j + 1) * 100, fill=color
                )

                _text = window.canvas.create_text(
                    i * 100 + 50,
                    j * 100 + 50,
                    text=i + 5 * j,
                    fill="black",
                    font=("Helivica 13 bold"),
                )

        # On affiche le robot
        _rect = window.canvas.create_rectangle(
            robot.x * 100 + 25,
            robot.y * 100 + 25,
            (robot.x * 100) + 75,
            (robot.y * 100) + 75,
            fill="#888",
        )

        # On update le canvas pour que les nouvelles modifs soient prises en compte
        window.update()
