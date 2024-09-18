from enum import IntEnum, auto
from turtle import Turtle


class Direction(IntEnum):
    UP = auto()
    LEFT = auto()
    DOWN = auto()
    RIGHT = auto()


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
        self._segments: list[SnakeTile] = []
        self._current_direction = Direction.RIGHT
        self.create_snake()

    def create_snake(self):
        self._head = SnakeTile()
        self._segments.extend([
            self._head,
            SnakeTile(x=-20),
            SnakeTile(x=-40),
        ])

    def make_a_move(self, move_distance: int = 20):
        for segment_0, segment_1 in zip(self._segments[::-1], self._segments[-2::-1]):
            segment_0.goto(segment_1.xcor(), segment_1.ycor())

        self._head.forward(move_distance)

    def _set_head_direction(self, direction: Direction, heading: int) -> None:
        self._current_direction = direction
        self._head.setheading(heading)

    def turn(self, direction: Direction):
        heading = None

        if self._current_direction in (Direction.UP, Direction.DOWN):
            if direction == Direction.LEFT:
                heading = 180
            elif direction == Direction.RIGHT:
                heading = 0

        elif self._current_direction in (Direction.LEFT, Direction.RIGHT):
            if direction == Direction.UP:
                heading = 90
            elif direction == Direction.DOWN:
                heading = 270

        if heading is not None:
            self._set_head_direction(direction, heading)
