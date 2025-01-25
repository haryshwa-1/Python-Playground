import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(600,600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_right, "d")
screen.onkey(snake.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.change_location()
        score.increase_score()
        snake.increase_snake_size()

    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score.game_over()
        game_is_on = False

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()