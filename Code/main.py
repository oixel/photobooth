from printer import Printer
from camera import Camera, Image, timer
import os

def main():
    # Initialize camera
    cam = Camera()
    cam.start()

    photo_list = []
    seconds = 5

    # 4 iterations of photos!
    for photo_iteration in range(4):
        timer(seconds,photo_iteration)
        # take photo
        
        # THIS REDUCE THE TIME TOO LONG but the sound effect does work 
        # playsound("flash.mp3")
        
        photo = cam.capture_array() # Snapping a picture from that camera
        image = Image.fromarray(photo)  # Convert pycamera image to Pillow image
        photo_list.append(image)
        
        # NOTE: Image resize handled at print to store highest quality image

    # path for saving images
    parent = os.path.dirname(os.getcwd())
    output_path = os.path.join(parent, "Images")
    os.makedirs(output_path, exist_ok=True)  # Create Images directory if one does not already exist
    print(f"Outputting images to: {output_path}")

    printer = Printer()

    # go through images and print / save
    for photo_iteration, image in enumerate(photo_list):
        image.save(output_path + f"output_{photo_iteration}.png")
        printer.print_image(image)
        printer.print_lines(5, 1)  # Create small gap after photo

if __name__ == "__main__":
    main()