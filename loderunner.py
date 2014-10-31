#
# MAZE
# 
# Example game
#
# Version without baddies running around
#


from graphics import *
import csv

LEVEL_WIDTH = 20
LEVEL_HEIGHT = 20

CELL_SIZE = 24
WINDOW_WIDTH = CELL_SIZE*LEVEL_WIDTH
WINDOW_HEIGHT = CELL_SIZE*LEVEL_HEIGHT

CELL_TYPE = {
  'EMPTY':  0,
  'BRICK':  1,
  'LADDER': 2,
  'ROPE':   3,
  'GOLD':   4,
  'BADDIE': 5
}

IMAGE_MAP = {
	1: 'brick.gif',
  	2: 'ladder.gif',
  	3: 'rope.gif',
  	4: 'gold.gif'
}

IMPASSABLE = [CELL_TYPE['BRICK']]
PASSABLE = [elem for elem in CELL_TYPE.values() if elem not in IMPASSABLE]
STANDABLE = [CELL_TYPE['LADDER'], CELL_TYPE['BRICK']]
GRABBABLE = [CELL_TYPE['ROPE']]
CLIMBABLE = [CELL_TYPE['LADDER']]
TAKEABLE = [CELL_TYPE['GOLD']]

def screen_pos (x,y):
    return (x*CELL_SIZE+10,y*CELL_SIZE+10)

def screen_pos_index (index):
    x = index % LEVEL_WIDTH
    y = (index - x) / LEVEL_WIDTH
    return screen_pos(x,y)

def index (x,y):
    return x + (y*LEVEL_WIDTH)

def coord(index):
    return index % LEVEL_WIDTH, index // LEVEL_WIDTH

class Character (object):
    def __init__ (self,pic,x,y,window,level):
        (sx,sy) = screen_pos(x,y)
        self._img = Image(Point(sx+CELL_SIZE/2,sy+CELL_SIZE/2+2),pic)
        self._window = window
        self._img.draw(window)
        self._x = x
        self._y = y
        self._level = level

    def pos(self):
        return self._x, self._y

    def same_loc (self,x,y):
        return (self._x == x and self._y == y)

    def move (self,dx,dy):
        tx = self._x + dx
        ty = self._y + dy
        if tx >= 0 and ty >= 0 and tx < LEVEL_WIDTH and ty < LEVEL_HEIGHT:
            if self._level[index(tx,ty)] in PASSABLE:
                if dx != 0:
                    self._x = tx
                    self._img.move(dx*CELL_SIZE, 0)

                if dy != 0 and self._level[index(self._x, self._y)] in CLIMBABLE:
                    self._y = ty
                    self._img.move(0, dy*CELL_SIZE)

                self.fall()

    def fall(self):
        cur_item = self._level[index(self._x, self._y)]
        next_item = self._level[index(self._x, self._y+1)]

        if not next_item in STANDABLE or cur_item in GRABBABLE:
            self._y += 1
            self._img.move(0, CELL_SIZE)
            self.fall()


class Player (Character):
    def __init__ (self,x,y,window,level):
        Character.__init__(self,'android.gif',x,y,window,level)

    def at_exit (self):
        return (self._y == 0)

    def take(self):
    	#print('Calling take.')
    	if self._level[index(self._x,self._y)] in TAKEABLE:
    		print('Taking.')
    		self._level[index(self._x,self._y)] = 0
    		

class Baddie (Character):
    def __init__ (self,x,y,window,level,player):
        Character.__init__(self,'red.gif',x,y,window,level)
        self._player = player


def lost (window):
    t = Text(Point(WINDOW_WIDTH/2+10,WINDOW_HEIGHT/2+10),'YOU LOST!')
    t.setSize(36)
    t.setTextColor('red')
    t.draw(window)
    window.getKey()
    exit(0)

def won (window):
    t = Text(Point(WINDOW_WIDTH/2+10,WINDOW_HEIGHT/2+10),'YOU WON!')
    t.setSize(36)
    t.setTextColor('red')
    t.draw(window)
    window.getKey()
    exit(0)


def create_level(num):
    with open('level{}.csv'.format(num), 'rb') as file_data:
        level = []
        for row in csv.reader(file_data):
            level.extend([int(elem) for elem in row])
        return level


def create_screen(level, window):
    def image(pos, img):
        return Image(Point((pos[0]+1)*CELL_SIZE-1, (pos[1]+1)*CELL_SIZE-1), img)

    for index, value in enumerate(level):
        if value in IMAGE_MAP:
            pos = coord(index)
            image(pos, IMAGE_MAP[value]).draw(window)


MOVE = {
    'Left': (-1,0),
    'Right': (1,0),
    'Up' : (0,-1),
    'Down' : (0,1)
}


def main ():

    window = GraphWin("LodeRunner", WINDOW_WIDTH+20, WINDOW_HEIGHT+20)
    rect = Rectangle(Point(5,5),Point(WINDOW_WIDTH+15,WINDOW_HEIGHT+15))
    rect.setFill('sienna')
    rect.setOutline('sienna')
    rect.draw(window)
    rect = Rectangle(Point(10,10),Point(WINDOW_WIDTH+10,WINDOW_HEIGHT+10))
    rect.setFill('white')
    rect.setOutline('white')
    rect.draw(window)

    level = create_level(1)
    screen = create_screen(level, window)

    p = Player(10,18,window,level)

    baddie1 = Baddie(5,1,window,level,p)
    baddie2 = Baddie(10,1,window,level,p)
    baddie3 = Baddie(15,1,window,level,p)

    while not p.at_exit():
        key = window.checkKey()
        if key == 'q':
            window.close()
            exit(0)
        if key in MOVE:
            (dx,dy) = MOVE[key]
            p.move(dx,dy)
        p.take()

        # baddies should probably move here




    won(window)

if __name__ == '__main__':
    main()