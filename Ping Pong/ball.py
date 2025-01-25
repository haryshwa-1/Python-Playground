from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.move_speed = 0.1
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.x = 1
        self.y = 1

    def move(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.y = -self.y
        new_x = self.xcor() + self.x * 10
        new_y = self.ycor() + self.y * 10
        self.setpos(new_x, new_y)

    def remove(self):
        self.hideturtle()

    def increase_speed(self):
        self.move_speed *= 0.9
