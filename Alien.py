from Actor import Actor
from random import randint, choice, random
from Bullet import Bullet
from Background import Background
from Rover import Rover
import Constants

alien_counter = 0 #static counter for the number of instances

class Alien(Actor):
    def __init__(self, arena):
        global alien_counter
        if(alien_counter > Constants.MAX_ALIEN_NUMBER): return #if there are already the maxium number of alien
        self._arena = arena
        self._x = randint(Constants.ALIEN_WIDTH, self._arena.size()[0]-Constants.ALIEN_WIDTH)
        self._y = randint(Constants.ALIEN_MIN_Y,Constants.ALIEN_MAX_Y)
        self._w, self._h = Constants.ALIEN_WIDTH, Constants.ALIEN_HEIGHT
        self._dx = Constants.ALIEN_SPEED
        alien_counter += 1
        arena.add(self)

    def move(self):
        if self._x + self._dx <= 0 or self._x + self._dx >= (self._arena.size()[0] - self._w): #change direction if border is touched
            self._dx *= -1
        if choice(range(Constants.CHANGE_DIRECTION_PROBABILITY)) == 0: #maybe it's time to change direction...
            self._dx *= -1
        if self.can_shoot(): #maybe it's time to shoot...
            Bullet(self._arena, (self.position()[0], self.position()[1] + Constants.BULLET_HEIGHT), Constants.VERTICAL_A,self)
            
        self._x += self._dx

    def is_out_of_canvas(self) -> bool:
        return False

    def collide(self, other):
        if isinstance(other,Background): return

        global alien_counter
        if(isinstance(other,Bullet)) and isinstance(other.get_author(),Rover):
            self._arena.remove(self)
            alien_counter -= 1

    def can_shoot(self) -> bool:
        '''
        returns true if the alien can shoot
        the probability is about 1/20
        '''
        return  (choice(range(Constants.SHOOT_PROBABILITY))) == 0

    def position(self)-> (int, int, int, int):
        return self._x, self._y, self._w, self._h

    def symbol(self) -> (int, int, int, int):
        return Constants.ALIEN_X, Constants.ALIEN_Y, self._w, self._h
