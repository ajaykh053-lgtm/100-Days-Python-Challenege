from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.X_move = 10
        self.y_move = 10
        self.move_spped=0.1

    def move(self):
        new_x = self.xcor() + self.X_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def Bounce_x(self):
        self.X_move *= -1
        self.move_spped*=0.9

    def Bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.move_spped=0.1
        self.Bounce_x()
    

