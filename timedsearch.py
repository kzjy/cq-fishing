from imagesearch import imagesearcharea
import time

def timedsearch(image, timesample, x1, y1, x2, y2, precision=0.8):
    pos = imagesearcharea(image, x1, y1, x2, y2, precision)
    start = time.time()
    while pos[0] == -1:
        time.sleep(timesample)
        pos = imagesearcharea(image, x1, y1, x2, y2, precision)
        if time.time() - start >= 1.5:
            break;
    return pos
