from turtle import Turtle
ALLIGNMENT = "left"
FONT = ("]Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score:{self.score}", align=ALLIGNMENT, font=FONT)
        self.hideturtle()
    def update_scoreboard(self):
        self.write(f"Score:{self.score}", align=ALLIGNMENT, font=FONT)
    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)