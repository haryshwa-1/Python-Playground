from turtle import Turtle
import random



COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.x = 0

    def create_car(self):
        num = random.randint(1, 6)
        if num == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            car.goto(300, new_y)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE + self.x*MOVE_INCREMENT)

    def increase_speed(self):
        self.x += 1


