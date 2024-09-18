from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, board_width: int, board_height: int, snake_width: int, shape: str = "circle"):
        super().__init__(shape)
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color('blue')
        self.speed('fastest')

        self._board_width = board_width
        self._board_height = board_height
        self._snake_width = snake_width

        self.refresh()

    def refresh(self):
        max_x = ((self._board_width // 2) - self._snake_width) // self._snake_width
        rand_x = random.randint(-max_x, max_x)

        max_y = ((self._board_height // 2) - self._snake_width) // self._snake_width
        rand_y = random.randint(-max_y, max_y)

        self.goto(rand_x * self._snake_width, rand_y * self._snake_width)
