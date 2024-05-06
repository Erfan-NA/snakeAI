import random
import snake_globals


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Direction:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self, head):
        self.head = head
        self.x = random.randint(0, round(snake_globals.GLOBAL_BOARD_X / 2)) + round(snake_globals.GLOBAL_BOARD_X / 4)
        self.y = random.randint(0, round(snake_globals.GLOBAL_BOARD_Y / 2)) + round(snake_globals.GLOBAL_BOARD_Y / 4)
        self.xDir = -1
        self.yDir = 0
        self.body = [Block(self.x, self.y)]

    def setDir(self, direction):
        self.xDir = direction.x
        self.yDir = direction.y
