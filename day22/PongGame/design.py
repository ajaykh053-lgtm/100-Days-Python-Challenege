from turtle import Turtle

class Design():
    def middle_line(self):
        shape=Turtle("arrow")
        shape.color("white")
        shape.hideturtle()
        shape.penup()
        shape.pensize(5)
        shape.goto(0,350)
        shape.setheading(-90)
        for _ in  range(36):
            shape.pendown()
            shape.fd(20)
            shape.penup()
            shape.fd(20)
    def create_circle(self):
        shape=Turtle("circle")
        shape.color("white","black")
        shape.shapesize(20,20)
