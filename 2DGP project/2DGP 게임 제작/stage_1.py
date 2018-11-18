
from pico2d import *
import game_framework
import game_world

from map_stage_1 import *

from enemy_stage_1 import enemy
from tower_white import tower_w
from tower_green import tower_g


name = "Stage_1"

enemy_1 = None

count = 20

tower_have = 0

get_tower = None

def enter():
    global enemy_1

    enemy_1 = [enemy(i * 30) for i in range(50)]
    grass = Grass()
    tile = Tile()
    UI_LEFT = Ui_Tower()

    game_world.add_object(grass, 0)
    game_world.add_object(UI_LEFT, 1)
    game_world.add_object(tile, 0)
    for pig in enemy_1 :
        game_world.add_object(pig, 2)



def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    global tower_have
    global get_tower
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if tower_have == 0:
                if (tile_rotate[int((700 - 1 - event.y) // 50)][int(event.x // 50)] > 7):
                    tower_have = tile_rotate[int((700 - 1 - event.y) // 50)][int(event.x // 50)]
                    if tower_have == 8:
                        get_tower = tower_w(event.x, 700 - 1 - event.y, False)
                        game_world.add_object(get_tower, 1)
                    elif tower_have == 10:
                        get_tower = tower_g(event.x, 700 - 1 - event.y, False)
                        game_world.add_object(get_tower, 1)
            else:
                if (tile_rotate[int((700 - 1 - event.y) // 50)][int(event.x // 50)] == 0):
                    get_tower.set = True
                    get_tower.x = int(event.x // 50) * 50 + 25
                    get_tower.y = int((700 - 1 - event.y) // 50) * 50 + 25
                    tower_have = 0


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.01)



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()