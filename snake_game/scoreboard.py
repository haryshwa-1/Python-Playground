from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 20, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.highscore = 0
        with open("highscore.txt") as file:
            num = int(file.read())
            self.highscore = num
        self.penup()
        self.setposition(0,270)
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highscore}", align= ALIGNMENT, font= FONT)
        self.score += 1

    def game_over(self):
        self.setposition(0, 0)
        if self.score > self.highscore :
            with open("../coffee_machine/highscore.txt", mode='w') as file:
                file.write(str(self.score - 1))
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)