from Arena import Arena
from Rover import Rover
from random import randint, choice
from Hole import Hole
from Rock import Rock
from Bullet import Bullet
from Alien import Alien
from Tank import Tank
from Background import Background
from time import time,gmtime,strftime
import Constants

class MoonPatrolGame():
    def __init__(self):
        self._arena = Arena((509, 400))
        Background(self._arena,(Constants.BLUE_MOUNTAIN_X, Constants.BLUE_MOUNTAIN_Y,Constants.BACKGROUND_WIDTH,Constants.BLUE_MOUNTAIN_HEIGHT),(0,0),Constants.BLUE_MOUNTAIN_SPEED)
        Background(self._arena,(Constants.BLUE_MOUNTAIN_X, Constants.BLUE_MOUNTAIN_Y,Constants.BACKGROUND_WIDTH,Constants.BLUE_MOUNTAIN_HEIGHT),(self._arena.size()[0],0),Constants.BLUE_MOUNTAIN_SPEED)
        Background(self._arena,(Constants.GREEN_MOUNTAIN_X, Constants.GREEN_MOUNTAIN_Y,Constants.BACKGROUND_WIDTH,Constants.GREEN_MOUNTAIN_HEIGHT),(0,Constants.GREEN_MOUNTAINS_MARGIN_TOP),Constants.GREEN_MOUNTAINS_SPEED)
        Background(self._arena,(Constants.GREEN_MOUNTAIN_X, Constants.GREEN_MOUNTAIN_Y,Constants.BACKGROUND_WIDTH,Constants.GREEN_MOUNTAIN_HEIGHT),(self._arena.size()[0],Constants.GREEN_MOUNTAINS_MARGIN_TOP),Constants.GREEN_MOUNTAINS_SPEED)
        Background(self._arena,(Constants.TERRAIN_X, Constants.TERRAIN_Y,Constants.BACKGROUND_WIDTH,Constants.TERRAIN_HEIGHT),(0,self._arena.size()[1]-Constants.TERRAIN_HEIGHT),Constants.TERRAIN_SPEED)
        Background(self._arena,(Constants.TERRAIN_X, Constants.TERRAIN_Y,Constants.BACKGROUND_WIDTH,Constants.TERRAIN_HEIGHT),(self._arena.size()[0],self._arena.size()[1]-Constants.TERRAIN_HEIGHT),Constants.TERRAIN_SPEED)
        self._player_one = Rover(self._arena)
        self._player_two = None
        self._elapsed_time = time()

    def spawn_rover(self):
        self._player_two = Rover(self._arena)

    def player_shoot(self,player):
        if player == Constants.PLAYER_ONE:
            self._player_one.shoot()
        elif player == Constants.PLAYER_TWO and self._player_two != None:
            self._player_two.shoot()
    
    def player_move(self, player, direction):
        if player == Constants.PLAYER_ONE:
            if direction == Constants.RIGHT: self._player_one.go_right()
            elif direction == Constants.LEFT: self._player_one.go_left()
            elif direction == Constants.UP: self._player_one.go_up()
            elif direction == Constants.DOWN: pass
            else: self._player_one.stay()
        elif player == Constants.PLAYER_TWO and self._player_two != None:
            if direction == Constants.RIGHT: self._player_two.go_right()
            elif direction == Constants.LEFT: self._player_two.go_left()
            elif direction == Constants.UP: self._player_two.go_up()
            elif direction == Constants.DOWN: pass
            else: self._player_two.stay()
    
    def player_points(self, player):
        if player == Constants.PLAYER_ONE:
            return self._player_one.get_points()
        elif player == Constants.PLAYER_TWO and self._player_two != None:
            return self._player_two.get_points()
        return 0
    
    def is_player_alive(self,player):
        if player == Constants.PLAYER_ONE:
            return self._player_one.is_alive()
        elif player == Constants.PLAYER_TWO and self._player_two != None:
            return self._player_two.is_alive()

    def spawn_obstacle(self):
        switch = choice(range(Constants.OBSTACLE_PROBABILITY)) #to increment the probability restrict the interval
        if switch == 0:
            Rock(self._arena,self._arena.size()[0])
        elif switch == 1:
            Hole(self._arena,self._arena.size()[0])

    def spawn_enemy(self):
        switch = choice(range(Constants.ENEMY_PROBABILITY)) #to increment the probability restrict the interval
        if switch == 0:
            Alien(self._arena)
        elif switch == 1:
            Tank(self._arena)

    def get_arena_size(self):
        return self._arena.size()

    def move_all_actors(self):
        self._arena.move_all()

    def get_all_actors(self):
        return self._arena.actors()

    def is_background(self, obj):
        return isinstance(obj,Background)

    def game_over(self):
        Tank.tank_counter = 0
        Alien.alien_counter = 0
        return not self._player_one.is_alive() and (self._player_two == None or not self._player_two.is_alive())

    def get_elapsed_time(self):
        return strftime("%H:%M:%S", gmtime((time() - self._elapsed_time)))

