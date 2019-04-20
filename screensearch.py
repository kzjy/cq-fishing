# stuff
import numpy as np
import time
import pyautogui
from PIL import ImageGrab
import cv2

"""
Get the screen with specified coordiantes 
"""
def get_screen():
    printscreen = np.array(ImageGrab.grab(bbox=(0, 40, 840, 520)))
    screen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB)

    return screen

"""
Output screen in real time
"""
def screen_record():
    while True:
        # 800x600 windowed mode
        screen = get_screen()
        cv2.imshow('window', screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

"""
Grab region tuple
"""
def grab_region(region):
    return pyautogui.screenshot(region=(region[0], region[1], region[2] - region[0], region[3] - region[1]))

"""
Search image from a region
"""
def search_image(image, region, precision=0.6, region_image=None):
    if region_image is None:
        region_image = grab_region(region=(region[0], region[1], region[2], region[3]))

    rgb = np.array(region_image)
    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc

"""
Continuously search image until it is found
"""
def search_image_until_found(image, interval, region, precision=0.6):
    position = search_image(image, region, precision)

    while position[0] == -1:
        time.sleep(interval)
        position = search_image(image, region, precision)

    return position

"""
Search image in region for a certain amount of time
"""
def timedsearch(image, duration, timesample, region, precision=0.8):
    pos = search_image(image, region, precision)
    start = time.time()
    while pos[0] == -1:
        time.sleep(timesample)
        pos = search_image(image, region, precision)
        if time.time() - start >= duration:
            break
    return pos

if __name__ == "__main__":
    screen_record()
