from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")
FONT1=("Helvetica", 20, "bold")
Score_list=[]

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=330)
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER !", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        Score_list.append(self.score)
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)
    
    def Max_Score(self):
        self.score=max(Score_list)
        self.goto(0,-100)
        self.write(f" Your Max is Score = {self.score}", align=ALIGNMENT, font=FONT1)
