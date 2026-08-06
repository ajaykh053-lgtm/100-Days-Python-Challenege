import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from desing import Desing
screen = Screen()
screen.setup(width=1200, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
desing=Desing()
desing.Road()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.go_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 35:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() == 290:
        player.finish_line_y()
        car_manager.level_up()
        scoreboard.level_increase()
screen.exitonclick()
