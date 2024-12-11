import pyautogui
from screeninfo import get_monitors
import math
import keyboard
import time

SCALE_FACTOR = 1.5
RESOLUTION = 10000
RADIUS = 4
OFFSET = 9

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

def points(offset_x, offset_y, n=RESOLUTION):
    r = 100 * RADIUS
    pi = math.pi
    return [(round(math.cos(2*pi/n*x)*r + offset_x), round(math.sin(2*pi/n*x)*r + offset_y)) for x in range(0,n+1)]


keyboard.wait('space')

center_x = int(((get_monitors()[0].width) / 2)  * (1/SCALE_FACTOR))
center_y = int(((get_monitors()[0].height) / 2) * (1/SCALE_FACTOR)) + OFFSET
points = points(center_x, center_y)

safety = 0
pyautogui.mouseDown(x=points[0][0], y=points[0][1], button='left')
for point in points:
    safety += 1
    if safety > RESOLUTION: break
    pyautogui.moveTo(point[0], point[1])
pyautogui.mouseUp(x=points[0][0], y=points[0][1], button='left')
