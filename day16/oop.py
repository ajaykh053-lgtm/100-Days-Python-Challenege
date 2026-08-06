from turtle import Turtle, Screen

# Turtle graphic website
# https://docs.python.org/3/library/turtle.html#turtle.register_shape

timmy = Turtle()
print(timmy)

timmy.shape("turtle")
timmy.color("Green")
for i in range(4):
    timmy.fd(100)
    timmy.rt(90)

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
my_screen.exitonclick()
