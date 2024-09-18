from turtle import Screen, Turtle
from threading import Event
from typing import Callable
import time


class SnakeTile(Turtle):
    def __init__(self, shape: str = "square", color: str = 'white', x: int = 0, y: int = 0) -> None:
        super().__init__(shape)
        self.width = 20
        self.color(color)
        self.penup()
        if x and y:
            self.goto(x, y)
        elif x or y:
            if x:
                self.goto(x, 0)
            if y:
                self.goto(y, 0)


class Snake:
    def __init__(self, game_event: Event, delay_between_moves: float, update_cb: Callable[[], None]) -> None:
        self._segments: list[SnakeTile] = [
            SnakeTile(),
            SnakeTile(x=-20),
            SnakeTile(x=-40),
        ]
        self._game_event = game_event
        self._update_cb = update_cb
        self._delay_between_moves = delay_between_moves
        self._update_cb()

    def start(self):
        while not self._game_event.is_set():
            print(end='.', flush=True)
            for segment in self._segments:
                segment.forward(20)
            self._update_cb()
            time.sleep(self._delay_between_moves)


class Board():
    def __init__(self) -> None:
        self._screen = Screen()
        self._screen.setup(width=600, height=600)
        self._screen.bgcolor('black')
        self._screen.title("Snake Game")
        self._screen.tracer(0)
        self.game_ended = Event()

    def update(self):
        self._screen.update()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._screen.exitonclick()
        self.game_ended.set()


def main():
    with Board() as board:  # noqa
        snake = Snake(board.game_ended, .1, board.update)  # noqa
        snake.start()


if __name__ == "__main__":
    main()
