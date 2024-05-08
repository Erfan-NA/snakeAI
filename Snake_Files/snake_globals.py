import snake_classes

# Assigning global game variables

GLOBAL_BOARD_X = 50
GLOBAL_BOARD_Y = 50
GLOBAL_BOARD_BINARY = [[0] * GLOBAL_BOARD_X] * GLOBAL_BOARD_Y
GLOBAL_BOARD_BLOCKS = [[]]


# Initialize game board of blocks for pygame to print, all blocks initialized as empty
def initializeBlockBoard():
    for x in range(GLOBAL_BOARD_X):
        for y in range(GLOBAL_BOARD_Y):
            GLOBAL_BOARD_BLOCKS[x].append(snake_classes.Block(x, y))


a = 1
