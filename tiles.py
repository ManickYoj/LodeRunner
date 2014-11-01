import csv, config, util
from graphics import GraphWin
from drawable import Drawable


class Tile(Drawable):
    level = []

    tile_map = {
        # 0: Empty,
        # 1: Brick,
        # 2: Ladder,
        # 3: Rope,
        # 4: Gold
    }

    @staticmethod
    def loadLevel(num):
        with open('level{}.csv'.format(num), 'rb') as file_data:
            Tile.level = []
            for row in csv.reader(file_data):
                Tile.level.extend([Tile.tile_map[int(elem)]() for elem in row])

        for index, tile in enumerate(Tile.level):
            tile.draw(util.coord(index))

    def __init__(self, img_path=None, properties={}):
        super(Tile, self).__init__(img_path)

        # Set up tile properties
        self.properties = {'passable':  True,
                           'takable':   False,
                           'standable': False,
                           'climbable': False,
                           'grabbable': False}

        for key in properties:
            if key in self.properties:
                self.properties[key] = properties[key]


class Empty(Tile):
    def __init__(self):
        super(Empty, self).__init__()


class Brick(Tile):
    def __init__(self):
        properties = {'passable':   False,
                      'standable':  True}
        super(Brick, self).__init__('brick.gif', properties)


class Ladder(Tile):
    def __init__(self):
        properties = {'standable':  True,
                      'climbable':  True,
                      'grabbable':  True}
        super(Ladder, self).__init__('ladder.gif', properties)


class Rope(Tile):
    def __init__(self):
        properties = {'grabbable':  True}
        super(Rope, self).__init__('rope.gif', properties)


class Gold(Tile):
    _numGold = 0

    def __init__(self):
        Gold._numGold += 1
        properties = {'takable': True}
        super(Gold, self).__init__('gold.gif', properties)

    def take(self, coords):
        self.undraw()
        Gold._numGold -= 1
        Tile.tile_map(util.index(coords))


Tile.tile_map = {0: Empty,
                 1: Brick,
                 2: Ladder,
                 3: Rope,
                 4: Gold}


if __name__ == "__main__":
    Drawable._window = GraphWin("LodeRunner", config.WINDOW_WIDTH+20, config.WINDOW_HEIGHT+20)
    Tile.loadLevel(1)
