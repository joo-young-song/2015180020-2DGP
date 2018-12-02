import game_framework
from pico2d import *
import map_stage_1
import map_stage_2
import map_stage_3
import stage_1
import stage_2
import stage_3
import game_world
import math


name = "TitleState"
image = None
image_stage_writting = None
image_white_blend = None
image_stage_1 = None
image_stage_2 = None
image_stage_3 = None

def enter():
    global image
    global image_stage_writting
    global image_white_blend
    global image_stage_1
    global image_stage_2
    global image_stage_3

    image = load_image('background_image//choice_stage_background.png')

    image_stage_writting = load_image('background_image//stage.png')

    image_stage_1 = load_image('background_image//stage1.png')

    image_stage_2 = load_image('background_image//stage2.png')

    image_stage_3 = load_image('background_image//stage3.png')

def exit():
    global image
    del (image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif event.type == SDL_MOUSEBUTTONDOWN:
                if math.sqrt((700 - 1 - event.y - 350) * (700 - 1 - event.y - 350) +  (event.x - 100) * (event.x - 100))  < 200:
                    game_world.objects = [[], [], []]
                    game_framework.change_state(stage_1, 100, 10)
                elif math.sqrt((700 - 1 - event.y - 350) * (700 - 1 - event.y - 350) +  (event.x - 500) * (event.x - 500))  < 200:
                    game_world.objects = [[], [], []]
                    game_framework.change_state(stage_2, 100, 10)
                elif math.sqrt((700 - 1 - event.y - 350) * (700 - 1 - event.y - 350) +  (event.x - 900) * (event.x - 900))  < 200:
                    game_world.objects = [[], [], []]
                    game_framework.change_state(stage_3, 200, 10)


def draw():
    clear_canvas()

    image.draw(500, 350, 1000, 700)

    image_stage_writting.draw(500,600,400,100)

    image_stage_1.draw(100, 350)

    image_stage_2.draw(500, 350)

    image_stage_3.draw(900, 350)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






