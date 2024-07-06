import random
from turtle import Turtle, Screen

class Ball:
    """
    A class to handle the ball's behavior in the Pong game.
    """

    def __init__(self, screen):
        self.screen = screen
        self.ball = Turtle(shape='square')
        self.ball.color('white')
        self.ball.shapesize(stretch_wid=0.5, stretch_len=None, outline=None)
        self.ball.penup()
        self.angle = random.choice([45, 135, 225, 315])
        self.ball_speed = 20

    def move(self):
        """
        Moves the ball forward in the current heading direction.
        """
        self.ball.setheading(self.angle)
        self.ball.fd(self.ball_speed)

    def collision_with_walls(self):
        """
        Checks for collision with the walls and updates the angle accordingly.

        Returns:
            str: 'right' if the ball goes past the right wall, 'left' if past the left wall, None otherwise.
        """
        if self.ball.ycor() > 290 or self.ball.ycor() < -290:
            self.angle = -self.angle
            return None
        elif self.ball.xcor() > (self.screen.window_width() / 2 + 10):
            self.angle = random.choice([135, 225])
            return 'right'
        elif self.ball.xcor() < -(self.screen.window_width() / 2 + 10):
            self.angle = random.choice([45, 315])
            return 'left'

    def reset_position(self):
        """
        Resets the ball's position to the center of the screen and gives it a random angle.
        """
        self.ball.goto(0, 0)
        self.angle = random.choice([45, 135, 225, 315])


if __name__ == '__main__':
    wn = Screen()
    wn.title("Pong Game")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    ball = Ball(wn)
    wn.mainloop()
