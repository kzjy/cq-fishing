# stuff
import numpy as np
from PIL import ImageGrab
import cv2

def get_screen():
    printscreen = np.array(ImageGrab.grab(bbox=(0, 40, 840, 520)))
    screen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB)

    return screen
def screen_record():
    while True:
        # 800x600 windowed mode
        screen = get_screen()
        cv2.imshow('window', screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    screen_record()
