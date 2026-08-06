from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5
CAR_STARTING_POSITION_X = 620
random_y_pos = [-205, -135 , -60 , 15 , 70 , 149, 221]


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1,12)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=4, stretch_wid=1.5)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.choice(random_y_pos)
            new_car.goto(x=CAR_STARTING_POSITION_X, y=random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
