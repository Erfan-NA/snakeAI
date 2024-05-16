import random
import snake_global_constants
from snake_global_constants import \
    GLOBAL_BOARD_X, GLOBAL_BOARD_Y, GLOBAL_BOARD_TRINARY, GLOBAL_BOARD_BLOCKS


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
    def __init__(self, direction):
        # x = random.randint(0, round(GLOBAL_BOARD_X / 2)) + round(GLOBAL_BOARD_X / 4)
        # y = random.randint(0, round(GLOBAL_BOARD_Y / 2)) + round(GLOBAL_BOARD_Y / 4)
        x = 2
        y = 2
        self.head = Block(x, y, direction)
        self.direction = direction
        self.body = [Block(x, y, self.direction)]


    # Self explanatory update direction
    def setDir(self, direction):
        self.direction.x = direction.x
        self.direction.y = direction.y

    # Self explanatory out of bounds check
    def outOfBounds(self):
        newX = self.head.x + self.direction.x
        newY = self.head.y + self.direction.y
        if (newX < 0 or newY < 0):
            return True

        elif (newX == GLOBAL_BOARD_X or newY == GLOBAL_BOARD_Y):
            return True
        return False

    # Checks what the snake collides with in the next frame
    def collisionCheck(self):
        newX = self.head.x + self.direction.x
        newY = self.head.y + self.direction.y
        return GLOBAL_BOARD_TRINARY[newY][newX]

    # Updates all three parallel structs
    def updatePos(self, extend, newBlock):
        self.body.append(newBlock)
        self.head = newBlock
        if (not extend):
            lastX = self.body[0].x
            lastY = self.body[0].y
            self.body.pop(0)
            GLOBAL_BOARD_TRINARY[lastY][lastX] = 0
            GLOBAL_BOARD_BLOCKS[lastY][lastX].direction = Direction(0, 0)

        GLOBAL_BOARD_TRINARY[newBlock.y][newBlock.x] = 1
        GLOBAL_BOARD_BLOCKS[newBlock.y][newBlock.x].direction = self.direction
