import snake_classes

# Assigning global game variables

GLOBAL_BOARD_X = 50
GLOBAL_BOARD_Y = 50
GLOBAL_BOARD_TRINARY = [[0] * GLOBAL_BOARD_X] * GLOBAL_BOARD_Y
GLOBAL_BOARD_BLOCKS = [[]]

GRID_PADDING = 5  # Padding around the grid
# Define colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

COLOR_MAP = {
    0: (20, 20, 20),     # Grey
    1: (0, 255, 0),     # Green
    2: (0, 0, 0)       # Black
    # Add more mappings as needed
}


# Initialize game board of blocks for pygame to print, all blocks initialized as empty
def initializeBlockBoard():
    for x in range(GLOBAL_BOARD_X):
        for y in range(GLOBAL_BOARD_Y):
            GLOBAL_BOARD_BLOCKS[x].append(snake_classes.Block(x, y))


a = 1
