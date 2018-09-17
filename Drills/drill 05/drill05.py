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
    x ,y= 132,243
    frame = 0
    x3,y3 = (535 - 132)/10 , (470 - 243)/10
    i = 0
    while i < 10:
        clear_canvas_now()
        frame = (frame + 1) % 8
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        x = x + x3
        y = y + y3
        i += 1
        delay(0.05)

def move_character_3():
    x ,y= 535,470
    frame = 0
    x3,y3 = (477-535)/10 , (203 - 470)/10
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

def move_character_4():
    x ,y= 477,203
    frame = 0
    x3,y3 = (715-477)/10 , (136-203)/10
    i = 0
    while i < 10:
        clear_canvas_now()
        frame = (frame + 1) % 8
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        x = x + x3
        y = y + y3
        i += 1
        delay(0.05)
def move_character_5():
    x ,y= 715,136
    frame = 0
    x3,y3 = (316-715)/10 , (225-136)/10
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
def move_character_6():
    x ,y= 316,225
    frame = 0
    x3,y3 = (510-316)/10 , (92-225)/10
    i = 0
    while i < 10:
        clear_canvas_now()
        frame = (frame + 1) % 8
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        x = x + x3
        y = y + y3
        i += 1
        delay(0.05)
def move_character_7():
    x ,y= 510,92
    frame = 0
    x3,y3 = (692-510)/10 , (518-92)/10
    i = 0
    while i < 10:
        clear_canvas_now()
        frame = (frame + 1) % 8
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        x = x + x3
        y = y + y3
        i += 1
        delay(0.05)
def move_character_8():
    x ,y= 692,518
    frame = 0
    x3,y3 = (682-692)/10 , (336-518)/10
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
def move_character_9():
    x ,y= 682,336
    frame = 0
    x3,y3 = (712-682)/10 , (349-336)/10
    i = 0
    while i < 10:
        clear_canvas_now()
        frame = (frame + 1) % 8
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        x = x + x3
        y = y + y3
        i += 1
        delay(0.05)
def move_character_10():
    x ,y= 712,349
    frame = 0
    x3,y3 = (203-712)/10 , (535-349)/10
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


while True:
    #move_character_1()
    #move_character_2()
    #move_character_3()
    #move_character_4()
    #move_character_5()
    #move_character_6()
    #move_character_7()
    #move_character_8()
    #move_character_9()
    move_character_10()


    
close_canvas()
