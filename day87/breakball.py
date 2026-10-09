from turtle import Turtle
import random


class Breakball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.speed("fastest")
        self.reset_ball(position)

    def reset_ball(self, position):
        self.goto(position)
        self.X_move = random.choice([-4, 4])
        self.Y_move = 5
        self.move_speed = 0.02

    def move(self):
        self.goto(self.xcor() + self.X_move, self.ycor() + self.Y_move)

    def reflect_x(self):
        self.X_move *= -1

    def reflect_y(self):
        self.Y_move *= -1

    def speed_up(self):
        self.move_speed = max(0.008, self.move_speed * 0.97)
