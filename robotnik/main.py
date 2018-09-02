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
import random

playback_start = 0
last_update = 0

ugfx_helper.init()
ugfx.clear()


# Clear LEDs
leds = Neopix()
YELLOW = 0xffff00
RED = 0xff0000
BLACK = 0x000000

CURRENT = YELLOW, RED

db = ugfx.html_color(0x843c06)
lb = ugfx.html_color(0xe1962d)


PACKETSIZE = 1024
SPEED = 0

def setup_audio():
    with open('robotnik/robotnik.amr', 'rb') as wavefile:
        print("Writing audio")
        print(sim800.fsrm('C:\\ROBOTNIK.AMR'))
        print(sim800.fswrite('C:\\ROBOTNIK.AMR', wavefile.read(), truncate=True))
        print("Saved audio")

ugfx.orientation(90)
ugfx.display_image(0, 0, "robotnik/start.png")
setup_audio()
while 1:
    if playback_start + 15000 < utime.ticks_ms() and sim800.command('AT+CMEDPLAY?')[1][-1]=='0':
        leds.display([0, 0])
        if playback_start + 300000 < utime.ticks_ms():
            playback_start = utime.ticks_ms()
            last_update = playback_start + 1200
            print(sim800.command('AT+CMEDPLAY=1,C:\\REC\\2.AMR,0,100'))
            CURRENT = (YELLOW, RED)
            ugfx.orientation(90)
            try:
                ugfx.clear(db)
                col_i = 0
                cols = [ugfx.RED, ugfx.GREEN]
                for x in range(9):
                    for y in range(11):
                        col_i += 1
                        if col_i % 2:
                            ugfx.area(x*30, y*30, 30, 30, lb)
                x = (utime.ticks_ms() % 200) - 50
                y = random.randint(-50, 150)
                print("Robotnik at %d,%d" % (x, y))
                ugfx.display_image(x, y, "robotnik/robotnik.png")
            except:
                raise
                ugfx.clear()
            SPEED = 600
            time.sleep(1500)
        else:
            if SPEED < 1000:
                SPEED = 99999999999999
                leds.display([BLACK, BLACK])
                ugfx.display_image(0, 0, "robotnik/start.png")
            sleep.wfi()

    if playback_start + 10700 < utime.ticks_ms() < playback_start + 11100:
        last_udate = 0
    if last_update + SPEED < utime.ticks_ms():
        leds.display(CURRENT)
        if playback_start + 10700 > utime.ticks_ms():
            if CURRENT == (YELLOW, RED):
                CURRENT = RED, YELLOW
            else:
                CURRENT = YELLOW, RED
        else:
            if YELLOW in CURRENT:
                last_update = 0
                CURRENT = (BLACK, BLACK)
            elif CURRENT == (RED, RED):
                CURRENT = (BLACK, BLACK)
            else:
                CURRENT = (RED, RED)
        last_update = utime.ticks_ms()
    if Buttons.is_pressed(Buttons.BTN_Menu):
        break
    if Buttons.is_pressed(Buttons.BTN_A) or Buttons.is_pressed(Buttons.BTN_B):
        playback_start = -400000
    

def force_start():
    global playback_start
    playback_start = 0 

Buttons.enable_interrupt(
    Buttons.BTN_B,
    lambda button_id: force_start(),
    on_press=True,
    on_release=False
)

Buttons.enable_interrupt(
    Buttons.BTN_A,
    lambda button_id: force_start(),
    on_press=True,
    on_release=False
)

app.restart_to_default()
