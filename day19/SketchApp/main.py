# tim=Turtle()
# screen=Screen()
# def move_fd():
#     tim.fd(10)
# screen.listen()
# screen.onkey(move_fd,key="space")
# #when we pass functio as an input to another function
# # we only pass function name without paranthesis
# screen.exitonclick()
# #fuction which takes funtions as input higher order function
from turtle import Turtle, Screen
import random

colors = [
    "black",
    "red",
    "blue",
    "green",
    "purple",
    "orange",
    "brown",
    "dark green",
    "dark blue",
    "maroon",
    "indigo",
]
fun = Turtle()
screen = Screen()
screen.setup(height=700, width=1000)
title = screen.title("Sketch Book 📖")


class Functions:

    def forword(self):
        fun.pendown()
        fun.forward(20)

    def backword(self):
        fun.pendown()
        fun.backward(20)

    def anticlockwoserotation(self):
        newheading = fun.heading() + 20
        fun.setheading(newheading)

    def clockwiserotation(self):
        newheading = fun.heading() - 20
        fun.setheading(newheading)

    def circle(self):
        radius = screen.numinput(title="Creating Circle ", prompt="Enter the Radius ")
        if radius:
            fun.color(random.choice(colors))
            fun.pendown()
            fun.circle(radius)
            fun.penup()
            fun.home()
            fun.setheading(0)
            fun.pendown()

    def square(self):
        sides = screen.numinput(title="Creating Square ", prompt="Enter the Sides ")
        if sides:
            fun.color(random.choice(colors))
            fun.pendown()
            for _ in range(4):
                fun.forward(sides)
                fun.right(90)
            fun.penup()
            fun.home()
            fun.setheading(0)
            fun.pendown()

    def triangle(self):
        length = screen.numinput(title="Creating Triangle ", prompt="Enter the length ")
        angle = screen.numinput(title="Creating Triangle ", prompt="Enter the angle ")
        if length and angle:
            fun.color(random.choice(colors))
            fun.pendown()
            for _ in range(3):
                fun.forward(length)
                fun.right(angle)
            fun.penup()
            fun.home()
            fun.setheading(0)
            fun.pendown()

    def rectangle(self):
        length = screen.numinput(
            title="Creating Rectangle ", prompt="Enter the length "
        )
        width = screen.numinput(title="Creating Rectangle ", prompt="Enter the width ")
        if length and width:
            fun.color(random.choice(colors))
            fun.pendown()
            for _ in range(2):
                fun.forward(length)
                fun.right(90)
                fun.forward(width)
                fun.right(90)
            fun.penup()
            fun.home()
            fun.setheading(0)
            fun.pendown()

    def clear_and_return(self):
        fun.reset()
        fun.penup()
        fun.home()
        fun.pendown()


funcs = Functions()

screen.listen()

screen.onkeypress(funcs.circle, key="C")
screen.onkeypress(funcs.square, key="S")
screen.onkeypress(funcs.triangle, key="T")
screen.onkeypress(funcs.rectangle, key="R")
screen.onkeypress(funcs.forword, key="Right")
screen.onkeypress(funcs.backword, key="Left")
screen.onkeypress(funcs.anticlockwoserotation, key="Up")
screen.onkeypress(funcs.clockwiserotation, key="Down")
screen.onkeypress(funcs.clear_and_return, key="Z")

screen.exitonclick()
