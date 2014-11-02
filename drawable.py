import config, os
from graphics import Image, Point, GraphWin


class Drawable(object):
    _window = GraphWin("LodeRunner", config.WINDOW_WIDTH+20, config.WINDOW_HEIGHT+20)

    def __init__(self, coords, img_path=None):
        if img_path:
            self._img = Image(Point((coords[0]+1)*config.CELL_SIZE-1, (coords[1]+1)*config.CELL_SIZE-1), os.path.join('graphics', img_path))
        else:
            self._img = None

    def draw(self):
        if self._img:
            self._img.draw(Drawable._window)

    def move_img(self, dx, dy):
        if self._img:
            self._img.move(dx * config.CELL_SIZE, dy * config.CELL_SIZE)

    def undraw(self):
        if self._img:
            self._img.undraw()

Drawable._window.setBackground('white')
