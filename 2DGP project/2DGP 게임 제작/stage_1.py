import game_framework
import game_world

from map_stage_1 import *

import game_clear_state

import game_over_state

from enemy_stage_1 import enemy
from enemy_stage_1_2 import enemy as enemy_2
from enemy_stage_1_boss import enemy as enemy_3

from tower_white import tower_w
from tower_green import tower_g
from tower_red import tower_r


name = "Stage_1"

enemy_1 = None

count = 20

tower_have = 0

get_tower = None

enemy3 = None

change = False
def enter():
    global enemy_1
    global enemy3
    enemy3 = enemy_3(80)
    enemy_1 = [enemy(i + 10) for i in range(50)] + [enemy_2(i + 50) for i in range(25)] + [enemy(i + 50) for i in range(25)] + [enemy3]
    grass = Grass()
    tile = Tile()
    UI_LEFT = Ui_Tower()
    UI_BUTTON = Ui_Button()
    UI_BACK = Ui_Back()

    game_world.add_object(UI_BACK, 0)
    game_world.add_object(grass, 0)
    game_world.add_object(UI_LEFT, 1)
    game_world.add_object(UI_BUTTON,1)
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
                    if tower_have == 8 and game_framework.GameState.money - 50 >= 0:
                        get_tower = tower_w(event.x, 700 - 1 - event.y, False)
                        game_world.add_object(get_tower, 1)
                        game_framework.GameState.money -= 50
                    elif tower_have == 9 and game_framework.GameState.money - 100 >= 0:
                        get_tower = tower_r(event.x, 700 - 1 - event.y, False)
                        game_world.add_object(get_tower, 1)
                        game_framework.GameState.money -= 100
                    elif tower_have == 10 and game_framework.GameState.money - 150 >= 0:
                        get_tower = tower_g(event.x, 700 - 1 - event.y, False)
                        game_world.add_object(get_tower, 1)
                        game_framework.GameState.money -= 150
                    else :
                        tower_have = 0
            else:
                if tile_rotate[int((700 - 1 - event.y) // 50)][int(event.x // 50)] == 0 :
                    get_tower.set = True
                    get_tower.x = int(event.x // 50) * 50 + 25
                    get_tower.y = int((700 - 1 - event.y) // 50) * 50 + 25
                    tower_have = 0
                elif tile_rotate[int((700 - 1 - event.y) // 50)][int(event.x // 50)] == 12 :
                    game_framework.GameState.money += (tower_have - 7) * 50
                    game_world.remove_object(get_tower)
                    tower_have = 0

        elif event.type == SDL_MOUSEMOTION:
            if tower_have != 0:
                get_tower.x = event.x
                get_tower.y = 700 - 1 - event.y


def update():
    global enemy3
    global change

    if enemy3.count == 0 and change == False:
        Grass().bgm.stop()
        enemy3.bgm.repeat_play()
        change = True
    for game_object in game_world.all_objects():
        game_object.update()
    if game_framework.GameState.life < 1 :
        game_framework.change_state(game_over_state)

    if enemy3.hp <= 0 :
        game_framework.change_state(game_clear_state)




def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    font = load_font('ENCR10B.TTF', 20)
    font.draw(925, 650, '%d' % game_framework.GameState.money, (255, 255, 255))
    font.draw(925, 550, '%d' % game_framework.GameState.life, (255, 255, 255))

    update_canvas()