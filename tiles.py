import csv, util, os
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
    def load_level(num):
        with open(os.path.join('levels','level{}.csv').format(num), 'rb') as file_data:
            Tile.level = []
            for row in csv.reader(file_data):
                Tile.level.extend([Tile.tile_map[int(elem)]() for elem in row])

        for index, tile in enumerate(Tile.level):
            tile.draw(util.coord(index))

    @staticmethod
    def query(coord, property):
        tile = Tile.level[util.index(*coord)]
        return tile.properties[property]

    @staticmethod
    def tile_at(coord):
        return Tile.level[util.index(*coord)]

    @staticmethod
    def clear(coord):
        Tile.level[util.index(*coord)].undraw()
        Tile.level[util.index(*coord)] = Empty()

    def __init__(self, img_path=None, properties={}):
        super(Tile, self).__init__(img_path)

        # Set up tile properties
        self.properties = {'passable':  True,
                           'takable':   False,
                           'standable': False,
                           'climbable': False,
                           'grabbable': False,
                           'diggable':  False}

        for key in properties:
            if key in self.properties:
                self.properties[key] = properties[key]

    def take(self, coords):
        pass


class Empty(Tile):
    def __init__(self):
        super(Empty, self).__init__()


class Brick(Tile):
    def __init__(self):
        properties = {'passable':   False,
                      'standable':  True,
                      'diggable':   True}
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
    _num_gold = 0

    @staticmethod
    def all_taken():
        return Gold._num_gold <= 0

    def __init__(self):
        Gold._num_gold += 1
        properties = {'takable': True}
        super(Gold, self).__init__('gold.gif', properties)

    def take(self, coords):
        Gold._num_gold -= 1
        Tile.clear(coords)


Tile.tile_map = {0: Empty,
                 1: Brick,
                 2: Ladder,
                 3: Rope,
                 4: Gold}


if __name__ == "__main__":
    Tile.load_level(1)
