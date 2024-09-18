from turtle import Screen, Turtle


class SnakeTile(Turtle):
    def __init__(self, shape: str = "square", color: str = 'white', x: int = 0, y: int = 0) -> None:
        super().__init__(shape)
        self.width = 20
        self.color(color)
        if x and y:
            self.goto(x, y)
        elif x or y:
            if x:
                self.goto(x, 0)
            if y:
                self.goto(y, 0)


class Snake:
    def __init__(self) -> None:
        self.segments = list[SnakeTile] = [
            SnakeTile(),
            SnakeTile(x=-20),
            SnakeTile(x=-40),
        ]


class Board():
    def __init__(self) -> None:
        self._screen = Screen()
        self._screen.setup(width=600, height=600)
        self._screen.bgcolor('black')
        self._screen.title("Snake Game")

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._screen.exitonclick()


def main():
    with Board() as board:  # noqa
        snake = Snake()  # noqa


if __name__ == "__main__":
    main()
