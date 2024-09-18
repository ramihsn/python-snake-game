import time

from snake import Snake
from board import Board


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
