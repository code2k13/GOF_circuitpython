import board
import busio
from time import sleep
from adafruit_st7735r import ST7735R
import displayio
import terminalio
from adafruit_display_text import label
import random

mosi_pin = board.GP11
clk_pin = board.GP10
reset_pin = board.GP17
cs_pin = board.GP18
dc_pin = board.GP16

scale = 4
width = 128 // scale
height = 160 // scale

displayio.release_displays()
spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)
display_bus = displayio.FourWire(
    spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin
)
display = ST7735R(display_bus, width=128, height=160, bgr=True)

splash = displayio.Group(scale=scale)
display.show(splash)

color_palette = displayio.Palette(3)
color_palette[0] = 0x000000
color_palette[1] = 0xFFFFFF


game_canvas = displayio.Bitmap(width, height, 2)
bg_sprite = displayio.TileGrid(game_canvas, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

for x in range(0, width):
    for y in range(0, height):
        game_canvas[x, y] = random.choice([0, 0, 0, 0, 0, 0, 0, 1])


def is_in_range(xd, yd):
    if xd < 0 or xd > width - 1:
        return False
    if yd < 0 or yd > height - 1:
        return False
    return True


def get_neighbors(canvas, x, y):
    nbrs = []
    for xd in range(x - 1, x + 2):
        for yd in range(y - 1, y + 2):
            if xd == x and yd == y:
                continue
            if is_in_range(xd, yd):
                nbrs.append(canvas[xd, yd])
    return nbrs


next_generation = displayio.Bitmap(width, height, 2)

while True:

    for x in range(0, width):
        for y in range(0, height):
            cur_val = game_canvas[x, y]
            nbrs = get_neighbors(game_canvas, x, y)
            live_nbrs = len([n for n in nbrs if n == 1])
            if cur_val == 0 and live_nbrs == 3:
                next_generation[x, y] = 1
            elif cur_val == 1 and live_nbrs <= 1:
                next_generation[x, y] = 0
            elif cur_val == 1 and live_nbrs >= 4:
                next_generation[x, y] = 0
            elif cur_val == 1 and (live_nbrs == 3 or live_nbrs == 2):
                next_generation[x, y] = 1
            else:
                next_generation[x, y] = 0

    for x in range(0, width):
        for y in range(0, height):
            game_canvas[x, y] = next_generation[x, y]
    sleep(0.001)
