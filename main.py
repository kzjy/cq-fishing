# main python file for fishing script

from screensearch import search_image, search_image_until_found, timedsearch
import pyautogui
import time

region = (0, 40, 840, 520)

# quiz = timedsearch("images/popquiz.png", 1, 0.5, region, 0.8)
# if quiz[0] != -1:
#     print("quiz found")

# Get the click position for wheeling in
click_position = search_image_until_found("images/wheel_click.png", 1, region, 0.8)
# click_position = search_image("images/wheel_click.png", region, 0.8)
if click_position[0] != -1:
    print("position : ", click_position[0], click_position[1])

while True:
    print("start")

    # Check if wheel is there, move to it if it is there
    pyautogui.moveTo(click_position[0] + 10, click_position[1] + 40)
    pyautogui.click(button="left")

    # Detect pop quiz
    quiz = timedsearch("images/popquiz.png", 1, 0.5, region, 0.8)
    if quiz[0] != -1:
        print("quiz found")

    # Wait for blue bar to show up
    blue_bar = search_image_until_found("images/blue_bar.png", 0.35, region)
    if blue_bar[0] != -1:
        print("found blue bar {}".format(blue_bar[0]))
        bar = search_image("images/bar.png", region, 0.8)
        sleep = (blue_bar[0] - bar[0]) * 0.004
        if sleep > 0:
            time.sleep(sleep)
        pyautogui.moveTo(click_position[0] + 10, click_position[1] + 40)
        pyautogui.click(button="left")

    # Wait for caught emotion
    caught = search_image_until_found("images/found.png", 0.5, region, 0.9)
    if caught[0] != -1:
        print("found")
        pyautogui.moveTo(click_position[0] + 10, click_position[1] + 40)
        pyautogui.click(button="left")

    # fish mini game
    time.sleep(2)
    finished = search_image("images/continue.png", region)

    while finished[0] == -1:

        # Press down if bar needs to be filled
        pyautogui.mouseUp()
        need_fill = timedsearch("images/need_fillv2.png", 1.5, 0.05, region, 0.98)
        if need_fill[0] != -1:
            print("down")
            pyautogui.mouseDown(click_position[0] + 10, click_position[1] + 40)

        # check if fish jumped
        m = search_image("images/m.png", region, 0.8)
        if m[0] != -1:
            if m[1] <= 320:
                print("need to swipe")
                time.sleep(0.5)
                # swipe = timedsearch("images/swipe.png", 1.5, 0.1, region, 0.8)
                pyautogui.drag(200, 0, 0.5, button="left")

        # release bar if too full
        need_release = timedsearch("images/need_releasev2.png", 1.5, 0.05, region, 0.98)
        if need_release[0] != -1:
            print("up")
            pyautogui.mouseUp()

        finished = search_image("images/continue.png", region)

    # finished finishing, click continue
    pyautogui.click()

    # prepare for next turn
    time.sleep(1.5)

