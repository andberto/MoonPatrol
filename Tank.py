from Actor import Actor
from random import randint,choice
from Bullet import Bullet
from Rover import Rover
from Rock import Rock 
from Hole import Hole
import Constants

tank_counter = 0 #static counter for the number of instances

class Tank(Actor):
    def __init__(self, arena):
        global tank_counter
        if(tank_counter > Constants.MAX_TANK_NUMBER): return
        self._arena = arena
        self._life = Constants.TANK_LIFE
        self._x = self._arena.size()[0] - Constants.TANK_WIDTH
        self._y = arena.size()[1]-Constants.TERRAIN_HEIGHT - Constants.TANK_HEIGHT
        self._w, self._h = Constants.TANK_WIDTH, Constants.TANK_HEIGHT
        self._dx, self._dy = Constants.TANK_SPEED , Constants.TANK_SPEED
        tank_counter += 1
        arena.add(self)

    def move(self):
        if(self._x <= self._arena.size()[0]/2 or self._x >= (self._arena.size()[0] - self._w)): #change direction if border is touched
            self._dx *= -1
        if self._y > self._arena.size()[1] - self._h - Constants.TERRAIN_HEIGHT: 
            self._y = self._arena.size()[1] - self._h - Constants.TERRAIN_HEIGHT
            self._dy = 0
        if self.can_shot(): #maybe it's time to shoot...
            Bullet(self._arena, (self.position()[0] - self._w, self.position()[1]), Constants.HORIZONTAL_O,self)
        

        self._x += self._dx
        self._y += self._dy
        self._dy += Constants.G

    def is_out_of_canvas(self) -> bool:
        return False

    def collide(self, other):
        global tank_counter
        if(isinstance(other,Bullet) and isinstance(other.get_author(),Rover)):
            self._life -=1
            if(self._life <= 0):
                self._arena.remove(self)
                tank_counter -= 1
                other.get_author().add_points(Constants.TANK_POINTS)
        elif isinstance(other,Rock) or isinstance(other,Hole):
            self._dy = - Constants.TANK_JUMP_SPEED

    def can_shot(self) -> bool:
        '''
        returns true if the alien can shoot
        the probability is about 1/20
        '''
        return (choice(range(Constants.SHOOT_PROBABILITY))) == 36

    def position(self) -> (int,int,int,int):
        return self._x, self._y, self._w, self._h

    def symbol(self) -> (int,int,int,int):
        return Constants.TANK_X, Constants.TANK_Y, self._w, self._h
