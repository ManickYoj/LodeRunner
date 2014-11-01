

from graphics import *
from drawable import Drawable
from tiles import Tile
from characters import Player
import config

# class Baddie (Character):
#     def __init__ (self,x,y,window,level,player):
#         Character.__init__(self,'red.gif',x,y,window,level)
#         self._player = player

def lost (window):
    t = Text(Point(WINDOW_WIDTH/2+10,WINDOW_HEIGHT/2+10),'YOU LOST!')
    t.setSize(36)
    t.setTextColor('red')
    t.draw(window)
    window.getKey()
    exit(0)

def won (window):
    t = Text(Point(config.WINDOW_WIDTH/2+10, config.WINDOW_HEIGHT/2+10),'YOU WON!')
    t.setSize(36)
    t.setTextColor('red')
    t.draw(window)
    window.getKey()
    exit(0)


KEYMAP = {
    'Left':     'Player.main.move(-1, 0)',
    'Right':    'Player.main.move(1, 0)',
    'Up':       'Player.main.move(0, -1)',
    'Down':     'Player.main.move(0, 1)',
    'a':        'Player.main.dig(-1)',
    'z':        'Player.main.dig(1)',
    'q':        'exit(0)'
}


def main():
    Tile.load_level(1)

    # TODO: Make this occur as part of load level
    Player(10, 18)

    # baddie1 = Baddie(5,1,window,level,p)
    # baddie2 = Baddie(10,1,window,level,p)
    # baddie3 = Baddie(15,1,window,level,p)

    while not Player.main.at_exit():
        key = Drawable._window.checkKey()

        if key in KEYMAP:
            eval(KEYMAP[key])

        # baddies should probably move here


    won(Drawable._window)

if __name__ == '__main__':
    main()
