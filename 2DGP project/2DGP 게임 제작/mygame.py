import game_framework
import pico2d

import start_state

# 한 타일당 가로 1미터 세로 1미터 50픽셀 = 1미터 1픽셀당 2cm

pico2d.open_canvas(1000, 700)
game_framework.run(start_state)
pico2d.close_canvas()