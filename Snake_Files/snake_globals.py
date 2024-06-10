import random
import numpy as np

# Assigning global game variables

GLOBAL_BOARD_X = 50
GLOBAL_BOARD_Y = 50

GRID_PADDING = 100  # Padding around the grid
REFRESH_RATE = 0.1

# Defined colors for convenience
RED = (255, 0, 0)
BLACK = (5, 5, 5)
GREY = (20, 20, 20)
GREEN = (0, 255, 0)

# Used for translating binary board to screen based on colors
COLOR_MAP = {
    0: (0, 0, 0),  # Black
    1: (0, 255, 0),  # Green
    2: (255, 0, 0),  # Red
    3: (20, 20, 20),  # Grey
}

BLOCK_MAP = {}
BINARY_CONVERT = {
    1: 0,
    0: 1,
}


# Position class defined for each block shown on screen
# If snake on block, it is not empty
class Block:
    def __init__(self, x, y, direction, cost):
        self.x = x
        self.y = y
        self.visited = False
        self.direction = direction
        self.cost = cost


# Class used for defining snake movement directions for convenience
class Direction:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Direction):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))


GLOBAL_BOARD_TRINARY = np.empty((GLOBAL_BOARD_Y, GLOBAL_BOARD_X), dtype=int)
GLOBAL_BOARD_BLOCKS = np.empty((GLOBAL_BOARD_Y, GLOBAL_BOARD_X), dtype=Block)
# Initialize game board of blocks for pygame to print, all blocks initialized as empty
def globalInitBoards():
    for x in range(GLOBAL_BOARD_X):
        for y in range(GLOBAL_BOARD_Y):
            GLOBAL_BOARD_TRINARY[y, x] = 0
            GLOBAL_BOARD_BLOCKS[y, x] = Block(x, y, Direction(0, 0), 0)


# Used to initialize a block mapping which takes into account a direction and adjusts block size
# Essentially allows for spacing between the body of the snake to happen based on the direction of movement
# Dynamically adjusts to screen size
def globalInitBlockMap(width, height, directions):
    BLOCK_MAP[directions[0]] = [width, height, [0, 0]]
    BLOCK_MAP[directions[1]] = [width, height - 2, [1, 1]]
    BLOCK_MAP[directions[2]] = [width, height - 2, [-1, 1]]
    BLOCK_MAP[directions[3]] = [width - 2, height, [1, 1]]
    BLOCK_MAP[directions[4]] = [width - 2, height, [1, -1]]


# Calculates the cell info for drawing using the block map defined globally
# Adjusts current cell depending on if there is fruit or snake or blank
def globalCellInfo(cell_x, cell_y, direction):
    cell_width = BLOCK_MAP[direction][0]
    cell_height = BLOCK_MAP[direction][1]
    cell_info = (cell_x + BLOCK_MAP[direction][2][0], cell_y + BLOCK_MAP[direction][2][1], cell_width, cell_height)
    return cell_info


# The main body of the snake object defined with appropriate position and direction
# The body list consists of all the blocks the snake is currently
class Snake:
    def __init__(self, direction):
        x = random.randint(0, round(GLOBAL_BOARD_X / 2)) + round(GLOBAL_BOARD_X / 4)
        y = random.randint(0, round(GLOBAL_BOARD_Y / 2)) + round(GLOBAL_BOARD_Y / 4)
        self.head = Block(x, y, direction, 0)
        self.direction = direction
        self.body = [Block(x, y, self.direction, 0)]

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
        return GLOBAL_BOARD_TRINARY[newY, newX]

    # Updates all three parallel structs
    def updatePos(self, extend, newBlock):
        self.body.append(newBlock)
        self.head = newBlock
        if (not extend):
            lastX = self.body[0].x
            lastY = self.body[0].y
            self.body.pop(0)
            GLOBAL_BOARD_TRINARY[lastY, lastX] = 0
            GLOBAL_BOARD_BLOCKS[lastY, lastX].direction = Direction(0, 0)

        GLOBAL_BOARD_TRINARY[newBlock.y, newBlock.x] = 1
        GLOBAL_BOARD_BLOCKS[newBlock.y, newBlock.x].direction = self.direction