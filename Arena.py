from Actor import Actor


class Arena():
    '''A generic 2D game, with a given size in pixels and a list of actors
    '''

    def __init__(self, size: (int, int)):
        '''Create an arena, with given dimensions in pixels
        '''
        self._w, self._h = size
        self._actors = []

    def add(self, a: Actor):
        '''Register an actor into this arena.
        Actors are blitted in their order of registration
        '''
        if a not in self._actors:
            self._actors.append(a)

    def remove(self, a: Actor):
        '''Cancel an actor from this arena
        '''
        if a in self._actors:
            self._actors.remove(a)

    def move_all(self):
        '''Move all actors (through their own move method).
        After each single move, collisions are checked and eventually
        the `collide` methods of both colliding actors are called
        '''
        actors = list(reversed(self._actors))
        for a in actors:
            a.move()
            if a.is_out_of_canvas():
                self.remove(a)
            for other in actors:
                # reversed order, so actors drawn on top of others
                # (towards the end of the cycle) are checked first
                if other is not a and self.check_collision(a, other):
                    a.collide(other)
                    other.collide(a)

    def check_collision(self, a1: Actor, a2: Actor) -> bool:
        '''Check the two actors (args) for mutual collision (bounding-box
        collision detection). Return True if colliding, False otherwise
        '''
        x1, y1, w1, h1 = a1.position()
        x2, y2, w2, h2 = a2.position()
        return (y2 < y1 + h1 and y1 < y2 + h2
                and x2 < x1 + w1 and x1 < x2 + w2
                and a1 in self._actors and a2 in self._actors)

    def actors(self) -> list:
        '''Return a copy of the list of actors
        '''
        return list(self._actors)

    def size(self) -> (int, int):
        '''Return the size of the arena as a couple: (width, height)
        '''
        return (self._w, self._h)
