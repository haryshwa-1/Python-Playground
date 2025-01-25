from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


paddle1 = Paddle(-1)  # Left paddle
paddle2 = Paddle(1)  # Right paddle
ball = Ball()
score1 = Scoreboard(1)
score2 = Scoreboard(-1)

screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with paddles
    if (ball.distance(paddle1) < 50 and ball.xcor() < -330) or (ball.distance(paddle2) < 50 and ball.xcor() > 330):
        ball.x = -ball.x  # Reverse the x direction
        ball.increase_speed()
        print(ball.speed())

    # Detect if ball goes out of bounds on the left or right
    if ball.xcor() > 380 :
        score2.increase_score()
        ball.move_speed = 0.1
        ball.goto(0, 0)  # Reset the ball to the center
        ball.x = -ball.x
        time.sleep(1)# Reverse direction


    if ball.xcor() < -380:
        score1.increase_score()
        ball.move_speed = 0.1
        ball.goto(0, 0)  # Reset the ball to the center
        ball.x = -ball.x
        time.sleep(1)# Reverse direction

    if score1.score == 8 or score2.score == 8:
        ball.remove()
        score1.game_over()
        game_is_on = False

screen.exitonclick()