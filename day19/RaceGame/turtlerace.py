from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=700, width=1000)
is_race_on = False
user_bet = screen.textinput(
    title="Make a bet", prompt="Which one will win the race? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []
for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    all_turtle.append(turtle)
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-490, y=y_position[turtle_index])
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 470:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.textinput(
                    title="Winner is",
                    prompt=f"You won the race. {winning_color} reached the final destination",
                )
            else:
                screen.textinput(
                    title="Winner is ",
                    prompt=f"You lose the race. {winning_color} reached the final destination",
                )
        turtle.speed("fastest")
        turtle.fd(random.randint(0, 10))
screen.exitonclick()
