import time
from turtle import Terminator

from Pad import Pad, Screen
from Box import BrickWall
from breakball import Breakball
from Scoreboard import Scoreboard

PAD_Y = -260
WALL_X = 490    # ball centre can't go past this (ball radius is 10)
TOP_Y = 290

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=1000)
screen.title("Breakout Game")
screen.tracer(0)

paddle = Pad((0, PAD_Y))
ball = Breakball((0, PAD_Y + 25))
wall = BrickWall()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")


def serve():
    ball.reset_ball((paddle.xcor(), PAD_Y + 25))
    screen.update()
    time.sleep(1)


def play():
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        ball.move()

        # side walls
        if ball.xcor() > WALL_X or ball.xcor() < -WALL_X:
            ball.reflect_x()
        # ceiling
        if ball.ycor() > TOP_Y:
            ball.reflect_y()

        # paddle (only when ball is travelling down)
        if (ball.Y_move < 0 and ball.ycor() < PAD_Y + 20
                and abs(ball.xcor() - paddle.xcor()) < 70):
            offset = (ball.xcor() - paddle.xcor()) / 60
            ball.X_move = max(-7, min(7, offset * 7)) or 2
            ball.Y_move = abs(ball.Y_move)
            ball.sety(PAD_Y + 20)
            ball.speed_up()

        # bricks
        if wall.check_hit(ball):
            scoreboard.add_point()
            ball.speed_up()
            if wall.remaining() == 0:
                scoreboard.message("YOU WIN!")
                game_is_on = False

        # missed the ball
        if ball.ycor() < -280:
            scoreboard.lose_life()
            if scoreboard.lives == 0:
                scoreboard.message("GAME OVER")
                game_is_on = False
            else:
                serve()

        screen.update()


try:
    play()
    screen.update()
    screen.exitonclick()
except Terminator:
    pass  # window closed mid-game
