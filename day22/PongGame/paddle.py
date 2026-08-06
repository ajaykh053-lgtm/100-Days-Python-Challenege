from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.goto(position)

    def go_up(self):
        y_pos = self.ycor()
        self.goto(x=self.xcor(), y=y_pos + 30)

    def go_down(self):
        y_pos = self.ycor()
        self.goto(x=self.xcor(), y=y_pos - 30)
    
