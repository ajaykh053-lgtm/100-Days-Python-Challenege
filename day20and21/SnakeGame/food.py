from turtle import Turtle
import random


class Food(Turtle):
    def refresh(self):
        self.goto(x=random.randint(-320, 320), y=random.randint(-320, 320))

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("black","red")
        self.dot_pos = self.refresh()
