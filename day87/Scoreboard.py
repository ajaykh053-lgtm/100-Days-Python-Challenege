from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.lives = 3
        self.update()

    def update(self):
        self.clear()
        self.goto(-480, 260)
        self.write(f"Score: {self.score}", align="left", font=FONT)
        self.goto(480, 260)
        self.write(f"Lives: {self.lives}", align="right", font=FONT)

    def add_point(self):
        self.score += 10
        self.update()

    def lose_life(self):
        self.lives -= 1
        self.update()

    def message(self, text):
        self.goto(0, -60)
        self.write(text, align="center", font=("Courier", 32, "bold"))
