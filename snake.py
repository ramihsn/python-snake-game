from enum import IntEnum, auto
from turtle import Turtle


class Direction(IntEnum):
    UP = auto()
    LEFT = auto()
    DOWN = auto()
    RIGHT = auto()


class SnakeTile(Turtle):
    INDEX = 0

    def __init__(self, shape: str = "square", color: str = 'white', x: int = 0, y: int = 0, width: int = 20):
        super().__init__(shape)
        self.width = width
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
    def __init__(self, tile_width: int = 20) -> None:
        self.tile_width = tile_width
        self._segments: list[SnakeTile] = []
        self._current_direction = Direction.RIGHT
        self._waiting_for_move = False
        self.create_snake()

    def create_snake(self):
        self.head = SnakeTile(width=self.tile_width)
        self._segments.extend([
            self.head,
            SnakeTile(x=-20, width=self.tile_width),
            SnakeTile(x=-40, width=self.tile_width),
        ])

    def make_a_move(self, move_distance: int = 20):
        for segment_0, segment_1 in zip(self._segments[::-1], self._segments[-2::-1]):
            segment_0.goto(segment_1.xcor(), segment_1.ycor())

        self.head.forward(move_distance)
        self._waiting_for_move = False

    def _set_head_direction(self, direction: Direction, heading: int) -> None:
        self._current_direction = direction
        self.head.setheading(heading)

    def turn(self, direction: Direction):
        if self._waiting_for_move:
            return

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
            self._waiting_for_move = True
