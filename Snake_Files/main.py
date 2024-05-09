# This is the beginning of one hell of a grueling project I hope. May 6, 2024.
# Erfan Nazarian

import snake_classes
import snake_global_constants
from snake_global_constants \
    import GRID_PADDING, GLOBAL_BOARD_X, GLOBAL_BOARD_Y, GLOBAL_BOARD_BLOCKS, \
    GLOBAL_BOARD_TRINARY, COLOR_MAP, BLOCK_MAP
import pygame
import sys

GLOBAL_UP = snake_classes.Direction(0, 1)
GLOBAL_DOWN = snake_classes.Direction(0, -1)
GLOBAL_LEFT = snake_classes.Direction(-1, 0)
GLOBAL_RIGHT = snake_classes.Direction(1, 0)
GLOBAL_NO_DIR = snake_classes.Direction(0, 0)
directions = [GLOBAL_NO_DIR, GLOBAL_LEFT, GLOBAL_RIGHT, GLOBAL_UP, GLOBAL_DOWN]

# Initialize Pygame
pygame.init()
# Get display info
info = pygame.display.Info()

# Get the size of the screen
screen_width = info.current_w
screen_height = info.current_h - 60
# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Example")

# Set up the grid size
cell_width = ((screen_width - GRID_PADDING) // GLOBAL_BOARD_X)
cell_height = ((screen_height - GRID_PADDING) // GLOBAL_BOARD_Y)

snake_global_constants.globalInitBlockBoard()
snake_global_constants.globalInitBlockMap(cell_width, cell_height, directions)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(snake_global_constants.BLACK)  # Fill with black

    # Draw content in each cell (optional)
    for i in range(GLOBAL_BOARD_X):
        for j in range(GLOBAL_BOARD_Y):
            # Draw something in each cell
            cell_direction = GLOBAL_BOARD_BLOCKS[i][j].direction
            cell_x = GRID_PADDING + (j * cell_width)
            cell_y = GRID_PADDING + (i * cell_height)
            cell_info = (cell_x, cell_y, cell_width, cell_height)
            pygame.draw.rect(screen, COLOR_MAP.get(GLOBAL_BOARD_TRINARY[i][j]), cell_info, 1)  # Example: Red outline

        cell_x = GRID_PADDING
        cell_y = GRID_PADDING + i * cell_height
        cell_info = (cell_x, cell_y, cell_width, cell_height)
        pygame.draw.rect(screen, COLOR_MAP.get(1), cell_info)  # Example: Red outline

    # Draw a blue rectangle
    # rect = pygame.Rect(100, 100, 200, 150)  # (x, y, width, height)
    # pygame.draw.rect(screen, snake_globals.BLUE, rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
