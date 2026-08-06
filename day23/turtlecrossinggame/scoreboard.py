from turtle import Turtle, Screen

FONT = ("Courier", 15, "bold")
screen = Screen()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.Level = 1
        self.level()

    def level(self):
        self.penup()
        self.goto(-590, 270)
        self.write(f"Level = {self.Level}", align="left", font=(FONT))

    def level_increase(self):
        self.Level += 1
        self.clear()
        self.level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over !", align="center", font=(FONT))
