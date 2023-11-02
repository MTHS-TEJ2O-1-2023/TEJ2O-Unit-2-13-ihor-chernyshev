"""
Created by: Ihor Chernyshev
Created on: Oct 2023
This program when you press the "A" button counts down from 4 to 0 at each number, and light up same number of neopixels
"""

# importing libraries
from microbit import *
import neopixel

# setup
display.clear()
np = neopixel.NeoPixel(pin16, 4)
np[0] = (0, 0, 0)
np[1] = (0, 0, 0)
np[2] = (0, 0, 0)
np[3] = (0, 0, 0)
np.clear()
display.show(Image.HAPPY)

# variables
loop_counter = 4

# turning on and off neopixels
while True:
    if button_a.was_pressed():
        np[0] = (255, 255, 255)
        np[1] = (255, 255, 255)
        np[2] = (255, 255, 255)
        np[3] = (255, 255, 255)
        print(np[0], np[1], np[2], np[3])
        np.show()
        while loop_counter >= 0:
            if loop_counter <= 3:
                np[loop_counter] = (0, 0, 0)
                print(np[loop_counter])
                np.show()
                display.show(loop_counter)
                loop_counter = loop_counter - 1
                sleep(1000)
            else:
                display.show(loop_counter)
                loop_counter = loop_counter - 1
                sleep(1000)
