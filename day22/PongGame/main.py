from paddle import Paddle, Screen
from ball import Ball
from Scoreboard import Scoreboard
from design import Design
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(height=700, width=1400)
screen.title(titlestring="Pong Game 🏓")
screen.tracer(0)

r_paddle = Paddle((650, 0))
l_paddle = Paddle((-650, 0))
desing = Design()
desing.middle_line()
desing.create_circle()
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_spped)
    screen.update()
    ball.move()

    # Detect collsion with wall
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.Bounce_y()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -600:
        ball.Bounce_x()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 600:
        ball.Bounce_x()

    # Detect L paddle misses
    if ball.xcor() < -660:
        ball.reset_position()
        scoreboard.r_point()

    # Detect R paddle misses
    if ball.xcor() > 660:
        ball.reset_position()
        scoreboard.l_point()

screen.exitonclick()
