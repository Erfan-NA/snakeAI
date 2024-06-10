import snake_classes
import queue
from snake_classes \
    import Direction, Block, Snake
import snake_global_constants
from snake_global_constants \
    import GRID_PADDING, GLOBAL_BOARD_X, GLOBAL_BOARD_Y, GLOBAL_BOARD_BLOCKS, \
    GLOBAL_BOARD_TRINARY, COLOR_MAP, BLOCK_MAP, REFRESH_RATE
import pygame
import sys
import time
import random


# Eventually will replace with pathfinding algorithm (A* with longest distance and uses blocks accessible heuristic
def directionOutput(snake, apple):
    priority_queue = queue.PriorityQueue()
    priority_queue.put((snake.head.cost, snake.head))

    while priority_queue:
        cost, block = priority_queue.get()
        currX = block.x
        currY = block.y


    return snake_classes.Direction(-1, 0)


