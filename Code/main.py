from escpos.printer import Serial
# temp to test
from escpos.printer import Usb
if __name__ == "__main__":
    # p = Serial(devfile='/dev/serial0',
    #        baudrate=9600,
    #        bytesize=8,
    #        parity='N',
    #        stopbitss=1,
    #        timeout=1.00,
    #        dsrdtr=True)

    p = Serial(devfile='COM3', baudrate=9600, 
           parity='N',
           stopbitss=1,
           timeout=1.00,
           dsrdtr=True)
    
    output_image = "C:/Users/mario/Coding/photobooth/Code/images/output.jpg"
    p.image(output_image)
