from turtle import Turtle, Screen


class Players:
    """
    A class to handle player paddles in the Pong game.
    """

    def __init__(self, screen):
        self.screen = screen
        self.player1 = []
        self.player2 = []
        self.__make_players__()

    def __make_players__(self):
        """
        Creates and sets the initial positions of the player paddles.
        """
        positions = [(-self.screen.window_width() // 2 + 20),
                     (self.screen.window_width() // 2 - 20)]
        for j, player in enumerate([self.player1, self.player2]):
            for _ in range(3):
                player_body = Turtle(shape='square')
                player_body.speed(0)
                player_body.color('white')
                player_body.penup()
                player.append(player_body)
            self.set_player_position(player, positions[j])

    def set_player_position(self, player, x_pos):
        """
        Sets the position of the player paddle.

        Args:
            player (list): List of turtle objects representing the player paddle.
            x_pos (int): The x-coordinate to position the paddle.
        """
        y_position = 0
        for player_body in player:
            player_body.goto(x_pos, y_position)
            y_position -= 20

    def move_up(self, player):
        """
        Moves the player paddle up.

        Args:
            player (list): List of turtle objects representing the player paddle.
        """
        if player[0].ycor() < 280:
            for _, i in enumerate(player):
                i.sety(i.ycor() + 60)

    def move_down(self, player):
        """
        Moves the player paddle down.

        Args:
            player (list): List of turtle objects representing the player paddle.
        """
        if player[-1].ycor() > -280:
            for _, i in enumerate(player):
                i.sety(i.ycor() - 60)


if __name__ == "__main__":
    wn = Screen()
    wn.title("Pong Game")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    players = Players(wn)
    wn.listen()
    wn.onkey(lambda: players.move_up(players.player1), "w")
    wn.onkey(lambda: players.move_down(players.player1), "s")
    wn.onkey(lambda: players.move_up(players.player2), "Up")
    wn.onkey(lambda: players.move_down(players.player2), "Down")
    wn.mainloop()
