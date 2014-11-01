from config import *


def index(x, y):
    return x + (y*LEVEL_WIDTH)


def coord(index):
    return index % LEVEL_WIDTH, index // LEVEL_WIDTH


def screen_pos(x, y):
    return (x*CELL_SIZE+10, y*CELL_SIZE+10)


def screen_pos_index(index):
    x = index % LEVEL_WIDTH
    y = (index - x) / LEVEL_WIDTH
    return screen_pos(x, y)
