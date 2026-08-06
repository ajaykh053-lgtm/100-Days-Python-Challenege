from turtle import Screen
from snake import Snake
from food import Food
from Scoreboard import Scoreboard
import time
import turtle

screen = Screen()
image = "C:/Users/ajayk/OneDrive/ドキュメント/Python/day20and21/SnakeGame/snakebg.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("Snake game bulit by Ajay 🐍😁")
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
    # Transfer the snake to other sides _x to +x
    if snake.head.ycor() > 350:
        snake.Transfer_postive_side()
    elif snake.head.ycor() < -350:
        snake.Transfer_negative_side()
    snake.move()
    # Detect collision with the food.
    if snake.head.distance(food) < 15:
        # refresh the food after detection
        food.refresh()
        # Add another part to the snake
        snake.Extend()
        # Increases the score by 1 each time collision with the food
        score.increase_score()
    # Detect collision with the All four sides of dimensions wall
    if snake.head.xcor() > 350 or snake.head.xcor() < -350:
        game_is_on = False
        score.game_over()
        score.Max_Score()
    # Detect collision tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
            score.Max_Score()
screen.exitonclick()
