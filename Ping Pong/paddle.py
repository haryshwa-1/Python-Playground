from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setpos(x * 350, 0)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        if self.ycor() <= 240:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() >= -230:
            self.goto(self.xcor(), self.ycor() - 20)