from turtle import Screen, Turtle
import time


class SnakeTile(Turtle):
    INDEX = 0

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

        self._index = self.INDEX
        self._update_index()

    @classmethod
    def _update_index(cls):
        cls.INDEX += 1

    def __repr__(self):
        return f'{self.__class__.__name__}[{self._index:2}](x={self.xcor()}, y={self.ycor()})'


class Snake:
    def __init__(self) -> None:
        self._head = SnakeTile()
        self._segments: list[SnakeTile] = [
            self._head,
            SnakeTile(x=-20),
            SnakeTile(x=-40),
        ]

    def make_a_move(self):
        for segment_0, segment_1 in zip(self._segments[::-1], self._segments[-2::-1]):
            print(segment_0, segment_1)
            segment_0.goto(segment_1.xcor(), segment_1.ycor())

        self._head.forward(20)


class Board():
    def __init__(self) -> None:
        self._screen = Screen()
        self._screen.setup(width=600, height=600)
        self._screen.bgcolor('black')
        self._screen.title("Snake Game")
        self._screen.tracer(0)

    def update(self):
        self._screen.update()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._screen.exitonclick()


def main():
    with Board() as board:
        snake = Snake()
        try:
            while True:
                snake.make_a_move()
                board.update()
                time.sleep(.3)
        except KeyboardInterrupt:
            ...


if __name__ == "__main__":
    main()
