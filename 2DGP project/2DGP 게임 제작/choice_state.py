import game_framework
from pico2d import *
import map_stage_1
import map_stage_2
import map_stage_3
import stage_1


name = "TitleState"
image = None
image_stage_writting = None
image_white_blend = None


def enter():
    global image
    global image_stage_writting
    global image_white_blend
    image = load_image('choice_stage_background.png')

    image_stage_writting = load_image('stage.png')


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
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(stage_1)


def draw():
    clear_canvas()

    image.draw(500, 350, 1000, 700)

    image_stage_writting.draw(500,600,400,100)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






