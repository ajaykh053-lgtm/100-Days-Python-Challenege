from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 24, "bold")

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.creating_turtle()

    def creating_turtle(self):
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def finish_line_y(self):
        self.creating_turtle()
    
    
