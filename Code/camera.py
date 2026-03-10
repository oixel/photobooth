from pycamera import camera
import time
import os
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
    
    
def main():
    cam = camera.Camera(0) # Choosing a camera
    photo_list = []
    seconds = 5

    # 4 iterations of photos!
    for photo_iteration in range(4):
        timer(seconds,photo_iteration)
        # take photo
        
        # THIS REDUCE THE TIME TOO LONG but the sound effect does work 
        # playsound("flash.mp3")
        
        photo_iteration = cam.snap() # Snapping a picture from that camera
        image = photo_iteration.to_pillow()  # Convert pycamera image to Pillow image
        # change to the size of the printer
        new_size = (384,384)
        resized_image = image.resize(new_size)
        # append photo
        photo_list.append(resized_image)

    # saving images
    output_folder = "Code/images/"
    # go through images
    print(f"Current Working Directory: {os.getcwd()}")

    for photo_iteration, image in enumerate(photo_list):
        image.save(output_folder + f"output_{photo_iteration}.jpg")


if __name__ == "__main__":
    main()
