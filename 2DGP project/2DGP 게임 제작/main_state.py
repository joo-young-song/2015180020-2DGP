
from pico2d import *
import game_framework
import game_world

from map_stage_1 import Tile
from map_stage_1 import Grass
from enemy_stage_1 import enemy


name = "MainState"

enemy_1 = None

def enter():
    global enemy_1

    grass = Grass()
    tile = Tile()
    enemy_1 = enemy()

    game_world.add_object(grass, 0)
    game_world.add_object(tile, 1)
    game_world.add_object(enemy_1, 1)


def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    # fill here


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






