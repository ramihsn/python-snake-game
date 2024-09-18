from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, board_width: int, board_height: int, snake_width: int, shape: str = "circle"):
        super().__init__(shape)
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color('blue')
        self.speed('fastest')

        max_x = ((board_width // 2) - snake_width) // snake_width
        rand_x = random.randint(-max_x, max_x)

        max_y = ((board_height // 2) - snake_width) // snake_width
        rand_y = random.randint(-max_y, max_y)

        self.goto(rand_x * snake_width, rand_y * snake_width)
