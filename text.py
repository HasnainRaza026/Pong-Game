from turtle import Turtle, Screen

class Text:
    """
    A class to handle text elements like the border and scoreboard in the Pong game.
    """

    def __init__(self):
        self.border = []
        self.__set_border__()
        self.scoreboard = []
        self.score = [0, 0]
        self.__set_scoreboard__()

    def __set_border__(self):
        """
        Creates and sets the border for the game.
        """
        y_position = -280
        for _ in range(20):
            border_segment = Turtle(shape='square')
            border_segment.speed(0)
            border_segment.color('white')
            border_segment.shapesize(stretch_wid=1, stretch_len=0.25, outline=None)
            border_segment.penup()
            border_segment.goto(0, y_position)
            y_position += 40
            self.border.append(border_segment)

    def __set_scoreboard__(self):
        """
        Creates and sets the scoreboard for the game.
        """
        i = 0
        for _ in range(2):
            player_scoreboard = Turtle(shape="square")
            player_scoreboard.color("white")
            player_scoreboard.speed(0)
            player_scoreboard.penup()
            player_scoreboard.hideturtle()
            player_scoreboard.goto(-100 + i, 200)
            i += 200
            self.scoreboard.append(player_scoreboard)
        self.update_score()

    def update_score(self):
        """
        Updates the scoreboard with the current scores.
        """
        for i in range(2):
            self.scoreboard[i].clear()
            self.scoreboard[i].write(f"{self.score[i]}", align="center", font=('Courier', 50, 'normal'))


if __name__ == "__main__":
    wn = Screen()
    wn.title("Pong Game")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    text = Text()
    wn.mainloop()
