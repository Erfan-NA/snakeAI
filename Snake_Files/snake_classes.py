import random
import snake_globals


# Position class defined for each block shown on screen
# If snake on block, it is not empty
class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.empty = False


# Class used for defining snake movement directions for convenience
class Direction:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# The main body of the snake object defined with appropriate position and direction
# The body list consists of all the blocks the snake is currently
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
