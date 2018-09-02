"""Dr Robotnik"""

___name___         = "DrRobotnik"
___license___      = "MIT"
___dependencies___ = ["sleep", "app"]
___categories___   = ["Sound"]
___bootstrapped___ = False

import ugfx_helper, os, wifi, ugfx, http, time, sleep, app
import sim800
from tilda import Buttons
from machine import Neopix
import utime

playback_start = 0
last_update = 0

ugfx_helper.init()
ugfx.clear()


# Clear LEDs
leds = Neopix()
YELLOW = 0xffff00
RED = 0xff0000

CURRENT = YELLOW, RED

try:
    ugfx.display_image(0, 0, "robotnik/robotnik.png")
except:
    ugfx.clear()
    


while 1:
    if sim800.startplayback(2):
        playback_start = utime.ticks_ms()
        last_update = playback_start
    if last_update + 80 < utime.ticks_ms():
        leds.display(CURRENT)
        if CURRENT == YELLOW, RED:
            CURRENT = RED, YELLOW
        else:
            CURRENT = YELLOW, RED
        last_update = utime.ticks_ms()
    if Buttons.is_pressed(Buttons.BTN_A) or Buttons.is_pressed(Buttons.BTN_Menu) or Buttons.is_pressed(Buttons.BTN_A):
        break

app.restart_to_default()
