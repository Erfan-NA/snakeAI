import random
import snake_globals


# Position class defined for each block shown on screen
# If snake on block, it is not empty
class Block:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.empty = False
        self.direction = direction


# Class used for defining snake movement directions for convenience
class Direction:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# The main body of the snake object defined with appropriate position and direction
# The body list consists of all the blocks the snake is currently
class Snake:
    def __init__(self, head, direction):
        self.head = head
        self.x = random.randint(0, round(snake_globals.GLOBAL_BOARD_X / 2)) + round(snake_globals.GLOBAL_BOARD_X / 4)
        self.y = random.randint(0, round(snake_globals.GLOBAL_BOARD_Y / 2)) + round(snake_globals.GLOBAL_BOARD_Y / 4)
        self.direction = direction
        self.body = [Block(self.x, self.y, self.direction)]

    def setDir(self, direction):
        self.direction.x = direction.x
        self.direction.y = direction.y

    # Self explanatory out of bounds check
    def outOfBounds(self):
        newX = self.x + self.direction.x
        newY = self.y + self.direction.y
        if (newX < 0 or newY < 0):
            return True
        elif (newX == snake_globals.GLOBAL_BOARD_X or newY == snake_globals.GLOBAL_BOARD_Y):
            return True
        return False

    # Checks what the snake collides with in the next frame
    def collisionCheck(self):
        newX = self.x + self.direction.x
        newY = self.y + self.direction.y
        return snake_globals.GLOBAL_BOARD_TRINARY[newX][newY]
