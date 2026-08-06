from turtle import Turtle

class Desing():
    def Road(self):
        road=Turtle("arrow")
        road.color("black")
        y_pos=-240
        road.penup()
        road.goto(600,y_pos)
        road.setheading(180)
        for _ in range(4):
            road.pendown()
            road.forward(1200)
            road.right(90)
            road.forward(70)
            road.right(90)
            road.forward(1200)
            road.left(90)
            road.forward(70)
            road.left(90)
        