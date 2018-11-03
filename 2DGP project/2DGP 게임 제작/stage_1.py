
from pico2d import *
import game_framework
import game_world

from map_stage_1 import Tile
from map_stage_1 import Grass
from enemy_stage_1 import enemy


name = "Stage_1"

enemy_1 = None

count = 20

def enter():
    global enemy_1

    enemy_1 = [enemy(i * 30) for i in range(50)]
    grass = Grass()
    tile = Tile()

    game_world.add_object(grass, 0)
    game_world.add_object(tile, 0)
    for pig in enemy_1 :
        game_world.add_object(pig, 1)


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

    delay(0.05)
    # fill here


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()