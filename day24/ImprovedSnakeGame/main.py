from turtle import Screen
from snake import Snake
from food import Food
from Scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("white")
screen.addshape("C:/Users/ajayk/OneDrive/ドキュメント/Python/day24/ImprovedSnakeGame/snakebg.gif")
screen.title("Snake game bulit by Ajay 🐍😁.")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")
screen.listen()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if snake.head.ycor() > 350:
        snake.Transfer_postive_side()
    elif snake.head.ycor() < -350:
        snake.Transfer_negative_side()
    snake.move()
    if snake.head.distance(food) < 15:
        score.increase_score()
        score.Update_scoreboard()
        food.refresh()
        snake.Extend()
    if snake.head.xcor() > 350 or snake.head.xcor() < -350:
        score.reset()
        
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            
            snake.reset()
screen.exitonclick()
