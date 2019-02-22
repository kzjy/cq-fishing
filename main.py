# main python file for fishing script
import cv2
import numpy
from screen import get_screen
from imagesearch import imagesearcharea, imagesearch_region_loop
from timedsearch import timedsearch
import pyautogui
import keyboard
import time

# Get the click position for wheeling in
click_position = imagesearcharea("images/wheel_click.png", 0, 40, 840, 520)
if click_position[0] != -1:
    print("position : ", click_position[0], click_position[1])

while True:
    print("start")
    # Check if wheel is there, move to it if it is there
    pyautogui.moveTo(click_position[0] + 10, click_position[1] + 40)
    pyautogui.click(button="left")

    # Wait for blue bar to show up
    bar = imagesearch_region_loop("images/blue_bar.png", 0.35, 0, 40, 840, 520)
    if bar[0] != -1:
        print("found blue bar {}".format(bar[0]))
        sleep = (bar[0] - 240) * 0.0045
        if sleep > 0:
            time.sleep(sleep)
        pyautogui.click(button="left")

    # Wait for caught emotion
    caught = imagesearch_region_loop("images/found.png", 0.5, 0, 40, 840, 520, 0.9)
    if caught[0] != -1:
        print("found")
        pyautogui.click(button="left")

    # fish mini game
    time.sleep(2)
    finished = imagesearcharea("images/continue.png", 0, 40, 840, 520)

    while finished[0] == -1:
        finished = imagesearcharea("images/continue.png", 0, 40, 840, 520)
        if finished[0] != -1:
            continue

        pyautogui.mouseUp()
        need_fill = timedsearch("images/need_fill.png", 0.05, 0, 40, 840, 520, 0.98)
        if need_fill[0] != -1:
            print("down")
            pyautogui.mouseDown(click_position[0] + 10, click_position[1] + 40)

        # check for qte and swipe
        swipe = imagesearcharea("images/swipe.png", 0, 40, 840, 520)
        if swipe[0] != -1:
            pyautogui.drag(70, 0, button="left")

        # fail safe
        finished = imagesearcharea("images/continue.png", 0, 40, 840, 520)
        if finished[0] != -1:
            continue

        need_release = timedsearch("images/need_releasev2.png", 0.05, 0, 40, 840, 520, 0.98)
        if need_release[0] != -1:
            print("up")
            pyautogui.mouseUp()

        finished = imagesearcharea("images/continue.png", 0, 40, 840, 520)
    # finished finishing, click continue
    pyautogui.click()

    time.sleep(1.5)

    print("got here 1")
    # failsafe for breaking out of loop
    if keyboard.is_pressed('q'):
        break
