import turtle
import time
from player import Players
from text import Text
from ball import Ball


def main():
    screen = turtle.Screen()
    screen.title("Pong Game")
    screen.bgcolor("black")
    screen.setup(width=1000, height=600)
    screen.tracer(0)  # Turns off the screen updates

    players = Players(screen)
    text = Text()
    ball = Ball(screen)

    screen.listen()
    screen.onkey(lambda: players.move_up(players.player1), "w")
    screen.onkey(lambda: players.move_up(players.player2), "Up")
    screen.onkey(lambda: players.move_down(players.player1), "s")
    screen.onkey(lambda: players.move_down(players.player2), "Down")

    while True:
        ball.move()

        # Collision with walls
        scored = ball.collision_with_walls()
        if scored == 'right':
            text.score[0] += 1
            text.update_score()
            ball.reset_position()
            players.set_player_position(
                players.player1, -screen.window_width() // 2 + 20)
            players.set_player_position(
                players.player2, screen.window_width() // 2 - 20)
            time.sleep(0.5)
        elif scored == 'left':
            text.score[1] += 1
            text.update_score()
            ball.reset_position()
            players.set_player_position(
                players.player1, -screen.window_width() // 2 + 20)
            players.set_player_position(
                players.player2, screen.window_width() // 2 - 20)
            time.sleep(0.5)

        # Collision with players
        for player in (players.player1, players.player2):
            for segment in player:
                if ball.ball.distance(segment) < 20:
                    ball.angle = 180 - ball.angle
                    break

        screen.update()
        time.sleep(0.02)


if __name__ == "__main__":
    main()
