from picamera2 import Picamera2 as Camera
from PIL import Image
import time
# from playsound3 import playsound

def timer(second_limit,photo_iteration):
# i can add it to show which specific photo its taking and to increase the pause time of the photo but let me know if you want that!
    for i in range(second_limit, 0, -1):
        # for first loop
        if photo_iteration==0:
            print(f"{i} seconds until photo", end="\r")
            time.sleep(1)
            continue
        # for other loops 
        else:
            print(f"{i} seconds until next photo", end="\r")
            time.sleep(1)