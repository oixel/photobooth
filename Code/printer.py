from config import MAX_IMAGE_WIDTH, CHUNK_ROWS, PRINT_DATA_DELAY
from PIL import Image
from escpos.printer import Usb, File
import tempfile
from os import close
import time

class Printer:
    def __init__(self):
        # Connect to generic USB printer
        self.printer = Usb(0x28e9, 0x0289, profile='POS-5890', out_ep=0x03, in_ep=0x81)

    # Prints the image (Pillow.Image) passed in
    def print_image(self, image):
        ratio = MAX_IMAGE_WIDTH / image.width
        image = image.resize((MAX_IMAGE_WIDTH, int(image.height * ratio)), Image.LANCZOS)  # Resize image to max width using LANCZOS algorithm
        
        chunk_rows = CHUNK_ROWS
        for row in range(0, image.height, chunk_rows):
            chunk = image.crop((0, row, MAX_IMAGE_WIDTH, min(row + chunk_rows, image.height)))

            fd, temp_path = tempfile.mkstemp()  # Make a temporary path to store the image data
            close(fd)  # Close the unused file descriptor
            print_file = File(temp_path, profile="POS-5890")
            print_file.image(chunk)
            print_file._device.flush()
            print_file.close()

            with open(temp_path, 'rb') as file:
                data = file.read()

            self.printer._raw(data)
            time.sleep(PRINT_DATA_DELAY)  # Delay for a few milliseconds to prevent the printer from eating all the data instantly
    
    # Allows gaps to be printed
    def print_lines(self, line_count, height = None):
        self.printer.line_spacing(height)
        self.printer.ln(line_count)
        self.printer.line_spacing()  # Reset back to default