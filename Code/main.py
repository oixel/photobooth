from escpos.printer import Serial

if __name__ == "__main__":
    p = Serial(devfile='/dev/serial0',
           baudrate=9600,
           bytesize=8,
           parity='N',
           stopbits=1,
           timeout=1.00,
           dsrdtr=True)
    
    p.text("Hello World\n")