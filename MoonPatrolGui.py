import g2d
from MoonPatrolGame import MoonPatrolGame
import Constants

sprites = g2d.load_image(Constants.SPRITES_URI)
backgrounds = g2d.load_image(Constants.BACKGROUNDS_URI)
arrow_up_flag_one, arrow_up_flag_two = False, False

class MoonPatrolGui():
    def __init__(self, game_logic: MoonPatrolGame):
        self._game_logic = game_logic

    def tick(self):
        global arrow_up_flag_one,arrow_up_flag_two

        if self._game_logic.game_over():
            g2d.set_color((0,0,0))
            g2d.fill_rect((0,0,self._game_logic.get_arena_size()[0],self._game_logic.get_arena_size()[1]))
            g2d.set_color((255,255,255))
            g2d.draw_text_centered("GAME OVER!", (self._game_logic.get_arena_size()[0]/2,self._game_logic.get_arena_size()[1]/3),20)
            g2d.draw_text_centered("R TO RESTART!", (self._game_logic.get_arena_size()[0]/2,self._game_logic.get_arena_size()[1]/2),20)
            if g2d.key_pressed("r"):
                self._game_logic = MoonPatrolGame()
            return

        if g2d.key_pressed("Enter"):
            self._game_logic.spawn_rover()
        elif g2d.key_pressed("ArrowUp"):
            arrow_up_flag_one = True
        elif g2d.key_pressed("ArrowRight"):
            self._game_logic.player_move(Constants.PLAYER_ONE,Constants.RIGHT)
        elif g2d.key_pressed("ArrowLeft"):
            self._game_logic.player_move(Constants.PLAYER_ONE,Constants.LEFT)
        elif g2d.key_pressed("ArrowDown"):
            self._game_logic.player_move(Constants.PLAYER_ONE,Constants.DOWN)
        elif g2d.key_released("ArrowUp") and arrow_up_flag_one:
            self._game_logic.player_move(Constants.PLAYER_ONE,Constants.UP)
            arrow_up_flag_one = False
        elif g2d.key_pressed("Spacebar") and self._game_logic.is_player_alive(Constants.PLAYER_ONE):
            self._game_logic.player_shoot(Constants.PLAYER_ONE)
        elif g2d.key_pressed("w"):
            arrow_up_flag_two = True
        elif g2d.key_pressed("d"):
            self._game_logic.player_move(Constants.PLAYER_TWO,Constants.RIGHT)
        elif g2d.key_pressed("a"):
            self._game_logic.player_move(Constants.PLAYER_TWO,Constants.LEFT)
        elif g2d.key_released("w") and arrow_up_flag_two:
            self._game_logic.player_move(Constants.PLAYER_TWO,Constants.UP)
            arrow_up_flag_two = False
        elif g2d.key_pressed("s"):
            self._game_logic.player_move(Constants.PLAYER_TWO,Constants.DOWN)
        elif g2d.key_pressed("q") and self._game_logic.is_player_alive(Constants.PLAYER_TWO):
            self._game_logic.player_shoot(Constants.PLAYER_TWO)
        elif (g2d.key_released("ArrowUp") or
            g2d.key_released("ArrowRight") or
            g2d.key_released("ArrowLeft")):
                self._game_logic.player_move(Constants.PLAYER_ONE,Constants.STAY)
        elif (g2d.key_released("w") or
            g2d.key_released("d") or
            g2d.key_released("a")):
                self._game_logic.player_move(Constants.PLAYER_TWO,Constants.STAY)

        self._game_logic.move_all_actors()
        self._game_logic.spawn_obstacle()
        self._game_logic.spawn_enemy()

        g2d.clear_canvas()

        for actor in self._game_logic.get_all_actors():
            if actor.symbol() != (0, 0, 0, 0) and self._game_logic.is_background(actor):
                g2d.draw_image_clip(backgrounds, actor.symbol(), actor.position())  
            elif actor.symbol() != (0, 0, 0, 0) and not self._game_logic.is_background(actor):
                g2d.draw_image_clip(sprites, actor.symbol(), actor.position())
            else:
                g2d.fill_rect(actor.position())

        if not self._game_logic.is_player_alive(Constants.PLAYER_TWO): g2d.draw_text("PRESS ENTER TO JOIN", (0,0),15)
        g2d.draw_text(str("P1 POINTS: " + str(self._game_logic.player_points(Constants.PLAYER_ONE))), (0,15),15)
        g2d.draw_text(str("P2 POINTS: " + str(self._game_logic.player_points(Constants.PLAYER_TWO))), (0,30),15)
        g2d.draw_text("ELAPSED TIME: " + self._game_logic.get_elapsed_time(), (0,45),15)

def gui_play(game):
    g2d.init_canvas(game.get_arena_size())
    ui = MoonPatrolGui(game)
    g2d.main_loop(ui.tick, 60)