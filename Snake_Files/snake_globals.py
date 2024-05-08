import snake_classes

# Assigning global game variables

GLOBAL_BOARD_X = 50
GLOBAL_BOARD_Y = 50
GLOBAL_BOARD_TRINARY = [[0] * GLOBAL_BOARD_X] * GLOBAL_BOARD_Y
GLOBAL_BOARD_BLOCKS = []

GRID_PADDING = 5  # Padding around the grid

# Defined colors for convenience
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREY = (20, 20, 20)
GREEN = (0, 255, 0)

# Used for translating binary board to screen based on colors
COLOR_MAP = {
    0: (0, 0, 0),       # Black
    1: (0, 255, 0),     # Green
    2: (255, 0, 0),      # Red
    3: (20, 20, 20),    # Grey
}


# Initialize game board of blocks for pygame to print, all blocks initialized as empty
def initializeBlockBoard():
    for x in range(GLOBAL_BOARD_X):
        row = []
        for y in range(GLOBAL_BOARD_Y):
            row.append(snake_classes.Block(x, y, snake_classes.Direction(0, 0)))
        GLOBAL_BOARD_BLOCKS.append(row)
