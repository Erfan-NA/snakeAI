import snake_classes

# Assigning global game variables

GLOBAL_BOARD_X = 50
GLOBAL_BOARD_Y = 50
GLOBAL_BOARD_TRINARY = []
GLOBAL_BOARD_BLOCKS = []

GRID_PADDING = 5  # Padding around the grid

# Defined colors for convenience
RED = (255, 0, 0)
BLACK = (0, 0, 0)
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


# Initialize game board of blocks for pygame to print, all blocks initialized as empty
def globalInitBoards():
    for x in range(GLOBAL_BOARD_X):
        row = []
        rowB = []
        for y in range(GLOBAL_BOARD_Y):
            rowB.append(0)
            row.append(snake_classes.Block(x, y, snake_classes.Direction(0, 0)))
        GLOBAL_BOARD_BLOCKS.append(row)
        GLOBAL_BOARD_TRINARY.append(rowB)


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
