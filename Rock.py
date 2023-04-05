from Actor import Actor
from random import randint
from Background import Background
from Rover import Rover
from Bullet import Bullet
import Constants


class Rock(Actor):
    def __init__(self, arena, x):
        self._x = x
        self._w, self._h = Constants.BIG_ROCK_WIDTH, Constants.BIG_ROCK_HEIGHT
        self._dx = Constants.ROCK_SPEED
        self._arena = arena
        self._size = randint(Constants.SMALL, Constants.BIG)
        self._life = self._size + 1
        self._is_exploded = False
        self._explosion_countdown = Constants.EXPLOSION_TIME
        arena.add(self)

    def get_size(self) -> int:
        '''
        returns
        0 - small rock
        1 - big rock
        '''
        return self._size

    def is_exploding(self) -> bool:
        '''
        returns true if the rock is exloading
        '''
        return self._is_exploded

    def move(self):
        self._x += self._dx

        if self._is_exploded:
            self._explosion_countdown -=1
        if self._explosion_countdown <= 0: #if the explosion is finished
            self._arena.remove(self)

    def collide(self, other):
        if isinstance(other,Background): return
        if isinstance(other,Bullet) and isinstance(other.get_author(),Rover):
            if self._life > 1: 
                self._life -=1
            else:
                self._is_exploded = True
            
    def is_out_of_canvas(self) -> bool:
        return self._x < (0 - self._w)

    def position(self) -> (int,int,int,int):
        return self._x, self._arena.size()[1]-Constants.TERRAIN_HEIGHT-self._h, self._w, self._h

    def symbol(self) -> (int,int,int,int):
        if self._is_exploded: #explosion sprite
            self._w,self._h = Constants.ROCK_EXPLOSION_WIDTH,Constants.ROCK_EXPLOSION_HEIGHT
            return Constants.ROCK_EXPLOSION_X, Constants.ROCK_EXPLOSION_Y, self._w, self._h
        if self._size == Constants.BIG: #big rock sprite
            self._w, self._h = Constants.BIG_ROCK_WIDTH, Constants.BIG_ROCK_HEIGHT
            return Constants.BIG_ROCK_X, Constants.BIG_ROCK_Y, self._w, self._h
        self._w, self._h = Constants.SMALL_ROCK_WIDTH, Constants.SMALL_ROCK_HEIGHT
        return Constants.SMALL_ROCK_X, Constants.SMALL_ROCK_Y, self._w, self._h #small rock sprite
