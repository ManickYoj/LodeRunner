from config import *


def index(x, y):
    return x + (y*LEVEL_WIDTH)


def coord(index):
    return index % LEVEL_WIDTH, index // LEVEL_WIDTH
