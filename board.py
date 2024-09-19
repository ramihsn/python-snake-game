from turtle import Turtle, Screen
from typing import Callable

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__(shape='blank')
        self.hideturtle()
        self.color('white')
        self._score = -1
        self.penup()
        self.goto(0, 260)

        self.add_to_score()

    def add_to_score(self):
        self._score += 1
        self.clear()
        self.write(f"Score: {self._score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.write(f"Game Over - Score: {self._score}", align=ALIGNMENT, font=FONT)


class Board():
    def __init__(self, width: int = 600, height: int = 600) -> None:
        self._screen = Screen()
        self._screen.setup(width=width, height=height)
        self._screen.bgcolor('black')
        self._screen.title("Snake Game")
        self._screen.tracer(0)
        self._score = ScoreBoard()

    def update(self):
        self._screen.update()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._screen.exitonclick()

    def bind(self, func: Callable[[], None], key: str) -> None:
        self._screen.onkey(func, key)
        self._screen.listen()

    def add_to_score(self):
        self._score.add_to_score()

    def game_over(self):
        self._score.game_over()
