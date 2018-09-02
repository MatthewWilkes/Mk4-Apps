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


ugfx_helper.init()
ugfx.clear()


# Clear LEDs
leds = Neopix()
YELLOW = 0xfee95a
RED = 0xdf2935

CURRENT = YELLOW, RED

try:
    image = http.get("https://i.imgur.com/HY52rF4.jpg").raise_for_status().content
    ugfx.display_image(0,0,bytearray(image))
except:
    ugfx.clear()
    ugfx.text(5, 5, "Couldn't download sponsors", ugfx.BLACK)



while 1:
    sim800.startplayback(2)
    leds.display(CURRENT)
    if CURRENT == YELLOW, RED:
        CURRENT = RED, YELLOW
    else:
        CURRENT = YELLOW, RED
    if Buttons.is_pressed(Buttons.BTN_A) or Buttons.is_pressed(Buttons.BTN_Menu) or Buttons.is_pressed(Buttons.BTN_A):
        break

ugfx.clear()
app.restart_to_default()
