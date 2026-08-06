import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states Game")
image = "C:/Users/ajayk/OneDrive/ドキュメント/Python/day25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv(
    "C:/Users/ajayk/OneDrive/ドキュメント/Python/day25/csvfile/50_states.csv"
)
all_states = data["state"].to_list()
Guessed_state = []

while len(Guessed_state) < 50:
    answer_state = screen.textinput(
        title=f"{len(Guessed_state)}/50Guess the state",
        prompt="What's another state name?",
    ).title()
    if answer_state=="Exit":
        # Learned in day 26 lession and applying here
        missing_state=[state for state in all_states if state not in Guessed_state]
        # for state in all_states:
        #     if state not in Guessed_state:
        #         missing_state.append(state)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("missing_states_names.csv")
        break
    if answer_state in all_states:
        Guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(state_data["x"].item(), state_data["y"].item())
        t.write(answer_state)

screen.exitonclick()
