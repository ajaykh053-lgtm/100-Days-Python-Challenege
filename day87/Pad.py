from turtle import Turtle, Screen

STEP = 40
LIMIT = 440  # keeps the paddle inside the 1000px-wide window


class Pad(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=6)  # 120px x 10px
        self.goto(position)

    def go_left(self):
        if self.xcor() - STEP >= -LIMIT:
            self.goto(self.xcor() - STEP, self.ycor())

    def go_right(self):
        if self.xcor() + STEP <= LIMIT:
            self.goto(self.xcor() + STEP, self.ycor())
