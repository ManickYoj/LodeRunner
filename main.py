"""
LodeRunner Clone
----------------
By: Bonnie Ishiguro and Nick Francisci
for Game Programming: Level 4
"""

import config, time
from graphics import *
from drawable import Drawable
from tiles import Tile, Gold, HiddenLadder
from characters import Player
from event import Event


# TODO: Move these somewhere more appropriate (drawable?)
def lost(window):
    t = Text(Point(WINDOW_WIDTH/2+10, WINDOW_HEIGHT/2+10), 'YOU LOST!')
    t.setSize(36)
    t.setTextColor('red')
    t.draw(window)
    window.getKey()
    exit(0)


def won(window):
    t = Text(Point(config.WINDOW_WIDTH/2+10, config.WINDOW_HEIGHT/2+10), 'YOU WON!')
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
    Tile.load_level(2)
    hidden_flag = False

    # TODO: Make this occur as part of load level
    Player(10, 18)
    # baddie1 = Baddie(5,1,window,level,p)
    # baddie2 = Baddie(10,1,window,level,p)
    # baddie3 = Baddie(15,1,window,level,p)
    frame_duration = 1.0/60.0

    while not Player.main.at_exit():
        frame_start_time = time.time()

        key = Drawable._window.checkKey()

        if key in KEYMAP:
            eval(KEYMAP[key])

        Event.update()

        if not hidden_flag:
            if Gold.all_taken():
                HiddenLadder.showAll()
                Player.main.redraw()
                hidden_flag = True

        # baddies should probably move here

        frame_time = time.time() - frame_start_time
        if frame_time < frame_duration:
            time.sleep(frame_duration - frame_time)
    won(Drawable._window)

if __name__ == '__main__':
    main()
