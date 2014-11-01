import config
from graphics import Image, Point


class Drawable(object):
    _window = None

    def __init__(self, img_path=None):
        self._img_path = img_path
        self._img = None

    def draw(self, coords):
        if self._img_path:
            self._img = Image(Point((coords[0]+1)*config.CELL_SIZE-1, (coords[1]+1)*config.CELL_SIZE-1), self._img_path)
            self._img.draw(Drawable._window)

    def move(self, dx, dy):
        if self._img:
            self._img.move(dx, dy)

    def undraw(self):
        if self._img:
            self._img.undraw()
