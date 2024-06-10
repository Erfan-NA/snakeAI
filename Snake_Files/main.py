# This is the beginning of one hell of a grueling project I hope. May 6, 2024.
# Erfan Nazarian
import snake_globals
from snake_globals \
    import GRID_PADDING, GLOBAL_BOARD_X, GLOBAL_BOARD_Y, GLOBAL_BOARD_BLOCKS, \
    GLOBAL_BOARD_TRINARY, COLOR_MAP, BLOCK_MAP, REFRESH_RATE, Direction, Block, Snake
import pygame
import sys
import time
import random

# Global variables in main
GLOBAL_UP = Direction(0, -1)
GLOBAL_DOWN = Direction(0, 1)
GLOBAL_LEFT = Direction(-1, 0)
GLOBAL_RIGHT = Direction(1, 0)
GLOBAL_NO_DIR = Direction(0, 0)
directions = [GLOBAL_NO_DIR, GLOBAL_LEFT, GLOBAL_RIGHT, GLOBAL_UP, GLOBAL_DOWN]

# Map for translating user key inputs into direction type
GLOBAL_KEY_DIR_MAP = {
    pygame.K_w: GLOBAL_UP,          # W key = Up
    pygame.K_UP: GLOBAL_UP,         # Up arrow = Up
    pygame.K_a: GLOBAL_LEFT,        # A key = Left
    pygame.K_LEFT: GLOBAL_LEFT,     # Left arrow = Left
    pygame.K_s: GLOBAL_DOWN,        # S key = Down
    pygame.K_DOWN: GLOBAL_DOWN,     # Down arrow = Down
    pygame.K_d: GLOBAL_RIGHT,       # D key = Right
    pygame.K_RIGHT: GLOBAL_RIGHT,   # Right arrow = Right
}


# Self explanatory
GLOBAL_OPPOSITE_DIR_MAP = {
    GLOBAL_DOWN: GLOBAL_UP,
    GLOBAL_RIGHT: GLOBAL_LEFT,
    GLOBAL_UP: GLOBAL_DOWN,
    GLOBAL_LEFT: GLOBAL_RIGHT,
}

# Initialize pygame
pygame.init()

# Get display info
info = pygame.display.Info()

# Get the size of the screen (For now manually account for top of window)
screen_width = info.current_w
screen_height = info.current_h - 60

min_size = screen_width
if (screen_width > screen_height):
    min_size = screen_height

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Example")

# Set up the grid size
cell_width = ((min_size - GRID_PADDING) // GLOBAL_BOARD_X)
cell_height = ((min_size - GRID_PADDING) // GLOBAL_BOARD_Y)

# Global struct initializations
snake_globals.globalInitBoards()
snake_globals.globalInitBlockMap(cell_width, cell_height, directions)

# Instantiate player and update parallel boards
player = Snake(random.choice(list(GLOBAL_OPPOSITE_DIR_MAP.keys())))
GLOBAL_BOARD_TRINARY[player.head.y, player.head.x] = 1
GLOBAL_BOARD_BLOCKS[player.head.y, player.head.x] = player.head
GLOBAL_FREE_SPOTS = GLOBAL_BOARD_X * GLOBAL_BOARD_Y


# Randomly places apple in one of the spots where the snake is not present
def createApple(spots):
    newPos = random.randint(1, spots)
    counter = 0
    x = 0
    y = 0
    while (counter != newPos):
        counter += snake_globals.BINARY_CONVERT[GLOBAL_BOARD_TRINARY[y, x]]
        x += 1
        if (x == GLOBAL_BOARD_X):
            x = 0
            y += 1
            y = y % GLOBAL_BOARD_Y
    x -= 1
    GLOBAL_BOARD_TRINARY[y, x] = 2
    spots -= 1
    return (x, y)


a = 2


def main():
    # Game loop
    start_time = time.time()
    elapsed_time = REFRESH_RATE * 1.1
    APPLE = createApple(GLOBAL_FREE_SPOTS)
    running = snakeEventHandler()

    # Prev dir is used to stop player from input spam that causes snake to go into itself
    prevDir = player.direction
    while running:
        if (elapsed_time > REFRESH_RATE):
            start_time = time.time()
            if (GLOBAL_OPPOSITE_DIR_MAP[prevDir] == player.direction):
                player.direction = prevDir

            prevDir = player.direction
            # Clear the screen
            screen.fill(snake_globals.BLACK)  # Fill with black

            # Draw content in each cell (optional)
            for j in range(GLOBAL_BOARD_Y):
                for i in range(GLOBAL_BOARD_X):
                    # Draw something in each cell
                    cell_adjust = BLOCK_MAP[GLOBAL_BOARD_BLOCKS[j, i].direction]
                    cell_x = GRID_PADDING + (i * cell_width) + cell_adjust[2][0]
                    cell_y = GRID_PADDING + (j * cell_height) + cell_adjust[2][1]
                    cell_info = (cell_x, cell_y, cell_adjust[0], cell_adjust[1])
                    pygame.draw.rect(screen, COLOR_MAP.get(GLOBAL_BOARD_TRINARY[j, i]), cell_info)

            # Snake collision check for walls and self
            # If snake collides with empty block or apple, game handles it
            if (not player.outOfBounds()):
                newBlock = Block(player.head.x + player.direction.x, player.head.y + player.direction.y,
                                 player.direction, 0)
                collision = player.collisionCheck()
                if (collision == 0):
                    player.updatePos(False, newBlock)
                elif (collision == 2):
                    player.updatePos(True, newBlock)
                    APPLE = createApple(GLOBAL_FREE_SPOTS)
                else:
                    break

            else:
                break

            # Update the display
        elapsed_time = time.time() - start_time
        pygame.display.flip()
        running = snakeEventHandler()

    # Quit Pygame
    pygame.quit()
    sys.exit()


# Temp event handler for testing snake controls for eventual AI integration
def snakeEventHandler():
    # Handle events
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            return False
        elif (event.type == pygame.KEYDOWN):
            if (event.key in GLOBAL_KEY_DIR_MAP):
                player.direction = GLOBAL_KEY_DIR_MAP[event.key]
    return True


main()
