import game_framework
import game_world

from map_stage_2 import *

from enemy_stage_2 import enemy
from enemy_stage_2_2 import enemy as enemy_2
from enemy_stage_1_boss import enemy as enemy_3

from tower_white import tower_w
from tower_ice import tower_i
from tower_poison import tower_p


name = "Stage_2"

enemy_1 = None

count = 20

tower_have = 0

get_tower = None

def enter():
    global enemy_1

    enemy_1 = [enemy_2(i) for i in range(50)]
    grass = Grass()
    tile = Tile()

    UI_LEFT = Ui_Tower()
    UI_BUTTON = Ui_Button()


    game_world.add_object(grass, 0)
    game_world.add_object(tile, 0)
    game_world.add_object(UI_LEFT, 1)
    game_world.add_object(UI_BUTTON,1)
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
                        get_tower = tower_p(event.x, 700 - 1 - event.y, False)
                        game_world.add_object(get_tower, 1)
                    elif tower_have == 9:
                        get_tower = tower_i(event.x, 700 - 1 - event.y, False)
                        game_world.add_object(get_tower, 1)
                    elif tower_have == 10:
                        get_tower = tower_p(event.x, 700 - 1 - event.y, False)
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



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()