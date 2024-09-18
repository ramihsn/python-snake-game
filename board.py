from turtle import Screen
from typing import Callable


class Board():
    def __init__(self, width: int = 600, height: int = 600) -> None:
        self._screen = Screen()
        self._screen.setup(width=width, height=height)
        self._screen.bgcolor('black')
        self._screen.title("Snake Game")
        self._screen.tracer(0)

    def update(self):
        self._screen.update()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._screen.exitonclick()

    def bind(self, func: Callable[[], None], key: str) -> None:
        self._screen.onkey(func, key)
        self._screen.listen()
