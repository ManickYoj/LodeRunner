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

    _hidden_tiles = []

    @staticmethod
    def load_level(num):
        with open(os.path.join('levels', 'level{}.csv').format(num), 'rb') as file_data:
            Tile.level = []
            row_num = 0
            for row in csv.reader(file_data):
                Tile.level.extend([Tile.tile_map[int(elem)]((index, row_num)) for index, elem in enumerate(row) if int(elem) in Tile.tile_map])
                row_num += 1

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
        Tile.level[util.index(*coord)] = Empty(coord)

    def __init__(self, coord, img_path=None, properties={}, hidden=False):
        super(Tile, self).__init__(coord, img_path)
        if not hidden:
            self.draw()

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

        self.coord = coord

        if hidden:
            self.hide()

    def hide(self):
        self.hidden_properties = self.properties
        self.properties = {'passable':  True,
                           'takable':   False,
                           'standable': False,
                           'climbable': False,
                           'grabbable': False,
                           'diggable':  False}
        self.undraw()

    def show(self):
        self.draw()
        self.properties = self.hidden_properties

    def take(self):
        pass


class Empty(Tile):
    def __init__(self, coord):
        super(Empty, self).__init__(coord)


class Brick(Tile):
    def __init__(self, coord):
        properties = {'passable':   False,
                      'standable':  True,
                      'diggable':   True}
        super(Brick, self).__init__(coord, 'brick.gif', properties)

class Ladder(Tile):
    def __init__(self, coord, hidden=False):
        properties = {'standable':  True,
                      'climbable':  True,
                      'grabbable':  True}
        super(Ladder, self).__init__(coord, 'ladder.gif', properties, hidden)


class Rope(Tile):
    def __init__(self, coord):
        properties = {'grabbable':  True}
        super(Rope, self).__init__(coord, 'rope.gif', properties)


class Gold(Tile):
    _num_gold = 0

    @staticmethod
    def all_taken():
        return Gold._num_gold <= 0

    def __init__(self, coord):
        Gold._num_gold += 1
        properties = {'takable': True}
        super(Gold, self).__init__(coord, 'gold.gif', properties)

    def take(self):
        Gold._num_gold -= 1
        Tile.clear(self.coord)


class HiddenLadder(Ladder):
    _hidden = []
    @staticmethod
    def showAll():
        for ladder in HiddenLadder._hidden:
            ladder.show()
        HiddenLadder._hidden = []

    def __init__(self, coord):
        super(HiddenLadder, self).__init__(coord, hidden=True)
        HiddenLadder._hidden.append(self)


Tile.tile_map = {0: Empty,
                 1: Brick,
                 2: Ladder,
                 3: Rope,
                 4: Gold,
                 5: HiddenLadder}


if __name__ == "__main__":
    Tile.load_level(1)
