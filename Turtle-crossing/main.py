import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
score = Scoreboard()
car_manager = CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:a
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    if player.finish() is True:
        score.increase_level()
        car_manager.increase_speed()
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()


screen.exitonclick()