from turtle import Turtle, onkeypress, Screen

MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    screen = Screen()
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def increase_snake_size(self):
        n = len(self.snake)
        self.snake.append(Turtle("square"))
        self.snake[n].color("white")
        self.snake[n].penup()
        x, y = self.snake[n-1].pos()
        self.snake[n].setpos(x - 20, y)


    def create_snake(self):
        for _ in range(3):
            self.increase_snake_size()

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            x, y = self.snake[i - 1].pos()
            self.snake[i].setpos(x,y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)




