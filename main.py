from argparse import ArgumentParser, Namespace
from functools import partial
import time

from snake import Snake, Direction
from board import Board
from food import Food


def _parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('--board-width', type=int, default=600)
    parser.add_argument('--board-height', type=int, default=600)
    parser.add_argument('--snake-width', type=int, default=20)
    return parser.parse_args()


def main():
    args = _parse_args()

    with Board(width=args.board_width, height=args.board_height) as board:
        snake = Snake(tile_width=args.snake_width)

        board.bind(partial(snake.turn, Direction.UP), 'Up')
        board.bind(partial(snake.turn, Direction.LEFT), 'Left')
        board.bind(partial(snake.turn, Direction.RIGHT), 'Right')
        board.bind(partial(snake.turn, Direction.DOWN), 'Down')

        try:
            food = Food(args.board_width, args.board_height, args.snake_width)
            while True:
                snake.make_a_move()
                board.update()
                time.sleep(.3)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
