from Actor import Actor
from random import randint
import Constants


class Hole(Actor):
    def __init__(self, arena, x):
        self._x = x
        self._w, self._h = Constants.BIG_HOLE_WIDTH, Constants.BIG_HOLE_HEIGH
        self._dx = Constants.HOLE_SPEED
        self._arena = arena
        self._size = randint(Constants.SMALL, Constants.MEDIUM)
        arena.add(self)

    def move(self):
        self._x += self._dx

    def is_out_of_canvas(self) -> bool:
        return self._x < (0 - self._w)

    def collide(self, other):
        pass #holes can't be removed from the arena...

    def position(self) -> (int,int,int,int):
        return self._x, self._arena.size()[1]-Constants.TERRAIN_HEIGHT-1, self._w, self._h

    def get_size(self) -> int:
        '''
        returns
        0 - small hole
        1 - big hole
        2 - medium hole
        '''
        return self._size

    def symbol(self) -> (int,int,int,int):
        if self._size == Constants.BIG: #sprite for big hole
            self._w, self._h = Constants.BIG_HOLE_WIDTH, Constants.BIG_HOLE_HEIGH
            return Constants.BIG_HOLE_x, Constants.BIG_HOLE_Y, self._w, self._h
        elif self._size == Constants.MEDIUM: #sprite for medium hole
            self._w, self._h = Constants.MEDIUM_HOLE_WIDTH, Constants.MEDIUM_HOLE_HEIGHT
            return Constants.MEDIUM_HOLE_X, Constants.MEDIUM_HOLE_Y, self._w, self._h
        self._w, self._h = Constants.SMALL_HOLE_WIDTH, Constants.SMALL_HOLE_HEIGHT 
        return Constants.SMALL_HOLE_x, Constants.SMALL_HOLE_Y, self._w, self._h #sprite for small hole
