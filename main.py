# main python file for fishing script

import sys
from screensearch import *
import pyautogui
import time

region = (0, 40, 840, 520)

need_fill_picture = "images/need_fillv2.png"
need_release_picture = "images/need_releasev2.png"

if sys.argv[1] == "event":
    need_fill_picture = "images/need_fill_event_trial.png"
    need_release_picture = "images/need_release_event_trial.png"
    print('event picture changed')

# Get the click position for wheeling in
click_position = search_image_until_found("images/wheel_click.png", 1, region, 0.8)
if click_position[0] != -1:
    print("position : ", click_position[0], click_position[1])


def check_press():

    reg = grab_region(region)
    fill = search_image("images/need_fillv2.png", region, 0.98, reg)
    release = search_image("images/need_releasev2.png", region, 0.98, reg)

    if fill[0] != -1:
        # pyautogui.mouseDown(click_position[0] + 10, click_position[1] + 40)
        print("down {}".format(fill[0]))
    elif release[0] != -1:
        # pyautogui.mouseUp()
        print("up")
    else:
        m = search_image("images/m.png", region, 0.8, reg)
        if m[0] != -1 and m[0] <= 320:
            time.sleep(0.5)
            pyautogui.drag(-300, 0, 0.5, button="left")


while True:
    print("Start fishing ")

    # Check if wheel is there, move to it if it is there
    pyautogui.moveTo(click_position[0] + 10, click_position[1] + 40)
    pyautogui.click(button="left")

    # Detect pop quiz
    time.sleep(0.5)
    quiz = search_image("images/popquiz.png", region, 0.8)
    if quiz[0] != -1:
        print("Detected pop quiz")

    # Wait for blue bar to show up
    blue_bar = search_image_until_found("images/blue_bar.png", 0.35, region)
    if blue_bar[0] != -1:
        print("Blue bar located at x: {}".format(blue_bar[0]))
        bar = search_image("images/bar_event.png", region, 0.8)
        sleep = (blue_bar[0] - bar[0]) * 0.0045
        if sleep > 0:
            time.sleep(sleep)
        pyautogui.moveTo(click_position[0] + 10, click_position[1] + 40)
        pyautogui.click(button="left")

    # Wait for caught emotion
    caught = search_image_until_found("images/found.png", 0.5, region, 0.9)
    if caught[0] != -1:
        print("Fish found")
        pyautogui.moveTo(click_position[0] + 10, click_position[1] + 40)
        pyautogui.click(button="left")

    # fish mini game
    time.sleep(2)
    finished = search_image("images/continue.png", region)

    while finished[0] == -1:

        # time.sleep(0.1)
        # check_press()

        # Press down if bar needs to be filled
        # pyautogui.mouseUp()
        need_fill = timedsearch(need_fill_picture, 1.5, 0.2, region, 0.98)
        if need_fill[0] != -1:
            print("down")
            pyautogui.mouseDown(click_position[0] + 10, click_position[1] + 40)

        # # check if fish jumped
        # m = search_image("images/m.png", region, 0.8)
        # if m[0] != -1:
        #     if m[1] <= 320:
        #         print("Swipe detected")
        #         time.sleep(0.5)
        #         pyautogui.drag(-300, 0, 0.5, button="left")

        # release bar if too full
        # time.sleep(1)
        need_release = timedsearch(need_release_picture, 1.5, 0.2, region, 0.98)
        if need_release[0] != -1:
            print("up")
            pass
        pyautogui.mouseUp()

        finished = search_image("images/continue.png", region)

    # finished finishing, click continue
    pyautogui.click()
    print("Finished fishing")

    # prepare for next turn
    time.sleep(1.5)

