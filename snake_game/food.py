from turtle import  Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.change_location()

    def change_location(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)

