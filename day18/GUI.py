from turtle import Turtle, Screen
import turtle
import random

tim = Turtle()
screen = Screen()
# drawing diffrent shape with doffrent colors
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
tim.speed("fastest")


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.fd(100)
        tim.rt(angle)


for shape_sides in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_sides)
screen.clear()
tim.penup()
tim.home()

# create Turtle using object and method
tim.shape("turtle")

# draw circle of 100 radius
tim.color("black")
tim.pencolor("black")
tim.circle(100)
screen.clear()
tim.penup()
tim.home()


# create dotted line using dot method
tim.dot(10)
tim.fd(25)
tim.dot(10, "purple")
tim.fd(50)
tim.dot(10, "red")
screen.clear()
tim.penup()
tim.home()
# challenge: draw the square
# 1
tim.shape("square")
tim.shapesize(10)
tim.color("red")
tim.pencolor("black")
screen.clear()
tim.penup()
tim.home()

# 2
tim.shape("arrow")
tim.color("black")
tim.pencolor("black")
for i in range(0, 4):
    tim.rt(90)
    tim.fd(100)
screen.clear()
tim.penup()
tim.home()


# #draw dashed line

pen = 0
while pen <= 25:
    tim.fd(10)
    tim.penup()
    tim.fd(10)
    tim.pendown()
    pen += 1
screen.clear()
tim.penup()
tim.home()

# Draw a radom walk

turtle.colormode(255)

tim = Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


direction = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")
for _ in range(100):
    tim.color(random_color())
    tim.fd(50)
    tim.setheading(random.choice(direction))
screen.clear()
tim.penup()
tim.home()
screen.exitonclick()
