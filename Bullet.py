from Actor import Actor
from Hole import Hole
from Background import Background
import Constants


class Bullet(Actor):
    def __init__(self, arena, position, direction, author):
        self._x, self._y = position
        self._w, self._h = Constants.BULLET_WIDTH, Constants.BULLET_HEIGHT
        self._dx, self._dy = direction
        self._author = author
        self._arena = arena
        arena.add(self)

    def move(self):
        self._x += self._dx
        self._y -= self._dy
        self.terrain_collision()

    def is_out_of_canvas(self) -> bool:
        return self._x > self._arena.size()[0] or self._y < 0 - self._h

    def collide(self, other):
        if isinstance(other,Background): return
        self._arena.remove(self)

    def terrain_collision(self):
        if self._y >= self._arena.size()[1] - Constants.TERRAIN_HEIGHT:
            Hole(self._arena, self._x) #spawn an hole on terrain collision
            self._arena.remove(self)
    
    def get_author(self):
        return self._author

    def position(self) -> (int,int,int,int):
        return self._x, self._y, self._w, self._h

    def symbol(self) -> (int,int,int,int):
        return Constants.BULLET_X, Constants.BULLET_Y, self._w, self._h
