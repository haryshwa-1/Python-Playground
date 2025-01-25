from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 50, "normal")

class Scoreboard(Turtle):
    def __init__(self, x):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(x*50,250)
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.write(f"{self.score}", align= ALIGNMENT, font= FONT)
        self.score += 1

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)