from functools import partial
import time

from snake import Snake, Direction
from board import Board


def main():
    with Board() as board:
        snake = Snake()

        board.bind(partial(snake.turn, Direction.UP), 'Up')
        board.bind(partial(snake.turn, Direction.LEFT), 'Left')
        board.bind(partial(snake.turn, Direction.RIGHT), 'Right')
        board.bind(partial(snake.turn, Direction.DOWN), 'Down')

        try:
            while True:
                snake.make_a_move()
                board.update()
                time.sleep(.3)
        except KeyboardInterrupt:
            ...


if __name__ == "__main__":
    main()
