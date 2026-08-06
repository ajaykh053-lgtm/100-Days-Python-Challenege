from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")
FONT1 = ("Helvetica", 20, "bold")
Score_list = []

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("C:/Users/ajayk/OneDrive/ドキュメント/Desktop/data.txt") as data:
            self.high_score = int(data.read())
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=330)
        self.Update_scoreboard()

    def Update_scoreboard(self):
        self.clear()
        self.write(
            f"Score = {self.score} High Score : {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(
                "C:/Users/ajayk/OneDrive/ドキュメント/Desktop/data.txt", mode="w"
            ) as data:
                data.write(f"{self.score}")
        self.score = 0
        self.Update_scoreboard()

    def increase_score(self):
        self.score += 1
        
