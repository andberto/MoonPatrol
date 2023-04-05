from Actor import Actor

class Background(Actor):
    
    def __init__(self, arena, symbol, pos, speed):
        self._arena_w = arena.size()[0]
        self._symbol = symbol
        self._speed = speed
        self._x , self._y = pos
        arena.add(self)

    def move(self):
        if self._x + self._symbol[2] + self._speed <= 0: self._x = self._arena_w
        self._x += self._speed

    def collide(self, other: 'Actor'):
        pass

    def position(self) -> (int, int, int, int):
        return self._x, self._y, self._symbol[2], self._symbol[3]
    
    def is_out_of_canvas(self) -> bool:
        pass

    def symbol(self) -> (int, int, int, int):
        return self._symbol