from Actor import Actor
from Bullet import Bullet
from Background import Background
import Constants

rover_count = 0

class Rover(Actor):
    def __init__(self, arena):
        global rover_count
        self._is_player_two = rover_count % 2
        self._arena = arena
        self._w, self._h = Constants.ROVER_WIDTH, Constants.ROVER_HEIGHT
        self._x, self._y = 0, self._arena.size()[1] - Constants.TERRAIN_HEIGHT - self._h
        self._speed = Constants.ROVER_SPEED
        self._dx, self._dy = 0, 0
        self._isAlive = True
        self._explosion_countdown = Constants.EXPLOSION_TIME
        self._points = 0
        arena.add(self)
        rover_count += 1

    def move(self):
        self._y += self._dy

        if self._y > self._arena.size()[1] - self._h - Constants.TERRAIN_HEIGHT:
            self._y = self._arena.size()[1] - self._h - Constants.TERRAIN_HEIGHT
            self._dy -= self._dy

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > self._arena.size()[0] - self._w:
            self._x = self._arena.size()[0] - self._w
        self._dy += Constants.G

        if not self._isAlive:
            self._explosion_countdown -=1
        if self._explosion_countdown <= 0:
            self._arena.remove(self)

    def is_out_of_canvas(self) -> bool:
        False

    def shoot(self):
        Bullet(self._arena, (self._x + self._w, self._y + self._h / 3), Constants.HORIZONTAL,self)
        Bullet(self._arena, (self._x, self._y - self._h), Constants.VERTICAL,self)

    def add_points(self,val):
        self._points += val

    def get_points(self):
        return self._points

    def go_left(self):
        self._dx, self._dy = -self._speed, 0

    def go_right(self):
        self._dx, self._dy = +self._speed, 0

    def go_up(self):
        if not (self._y == self._arena.size()[1]-Constants.TERRAIN_HEIGHT - Constants.ROVER_HEIGHT): #if the rover is already jumping
            return
        self._dx, self._dy = 0, - self._speed

    def go_down(self):
        self._dx, self._dy = 0, + self._speed

    def stay(self):
        self._dx, self._dy = 0, 0

    def collide(self, other):
        if isinstance(other,Rover) or isinstance(other,Background): return
        if(isinstance(other,Bullet) and isinstance(other.get_author(),Rover)): return
        self._isAlive = False
        self._speed = 0

    def position(self) -> (int,int,int,int):
        return self._x, self._y, self._w, self._h

    def is_jumping(self) -> bool:
        return self._y != self._arena.size()[1]-Constants.TERRAIN_HEIGHT - Constants.ROVER_HEIGHT and self._dy < 0

    def is_falling(self) -> bool:
        return self._y != self._arena.size()[1]-Constants.TERRAIN_HEIGHT - Constants.ROVER_HEIGHT and self._dy > 0

    def is_alive(self) -> bool:
        return self._isAlive 

    def symbol(self) -> (int,int,int,int): 
        if not self._isAlive: #explosion sprite
            return Constants.EXPLOSION_X, Constants.EXPLOSION_Y, Constants.EXPLOSION_WIDTH, Constants.EXPLOSION_HEIGHT
        elif(self.is_jumping() and not self._is_player_two): #jumping purple
            return Constants.ROVER_JUMPING_X, Constants.ROVER_JUMPING_Y, self._w, self._h
        elif(self.is_falling() and not self._is_player_two): #falling purple
            return Constants.ROVER_FALLING_X, Constants.ROVER_FALLING_Y, self._w, self._h
        elif(not self._is_player_two): #stay purple
            return Constants.ROVER_X, Constants.ROVER_Y, self._w, self._h
        elif(self.is_jumping() and self._is_player_two): #jumping red
            return Constants.ROVER_TWO_JUMPING_X, Constants.ROVER_TWO_JUMPING_Y, self._w, self._h
        elif(self.is_falling() and self._is_player_two): #falling red
            return Constants.ROVER_TWO_FALLING_X, Constants.ROVER_TWO_FALLING_Y, self._w, self._h
        elif (self._is_player_two): #stay red
            return Constants.ROVER_TWO_X, Constants.ROVER_TWO_Y, self._w, self._h
        
                
