from escpos.printer import Serial
if __name__ == "__main__":
    p = Serial(devfile='/dev/serial0',
           baudrate=9600,
           bytesize=8,
           parity='N',
           stopbitss=1,
           timeout=1.00,
           dsrdtr=True)

# doesnt work didnt want to change driver
    # p = Serial(devfile='COM3', baudrate=9600, 
    #        parity='N',
    #        stopbitss=1,
    #        timeout=1.00,
    #        dsrdtr=True)
    
    output_image = "C:/Users/mario/Coding/photobooth/Code/images/output.jpg"
    p.image(output_image)
