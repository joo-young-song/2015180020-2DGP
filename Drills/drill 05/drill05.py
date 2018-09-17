from pico2d import *

open_canvas()

character = load_image("animation_sheet.png")



def move_character_1():
    x ,y= 203,535
    frame = 0
    x3,y3 = (132-203)/10 , (243-535)/10
    i = 0
    while i < 10:
        clear_canvas_now()
        frame = (frame + 1) % 8
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        x = x + x3
        y = y + y3
        i += 1
        delay(0.05)

    
def move_character_2():
    pass
def move_character_3():
    pass
def move_character_3():
    pass
def move_character_4():
    pass
def move_character_5():
    pass
def move_character_6():
    pass
def move_character_7():
    pass
def move_character_8():
    pass
def move_character_9():
    pass
def move_character_10():
    pass



while True:
    move_character_1()
    move_character_2()
    move_character_3()
    move_character_4()
    move_character_5()
    move_character_6()
    move_character_7()
    move_character_8()
    move_character_9()
    move_character_10()


    
close_canvas()
