import game_framework
from pico2d import *
import explain_state_1


name = "TitleState"
image = None


def enter():
    global image
    image = load_image('background_image//title_image.jpg')


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
                game_framework.change_state(explain_state_1)


def draw():
    clear_canvas()
    image.draw(500, 350, 1000, 700)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






