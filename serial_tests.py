import serial
from time import sleep

if __name__ == "__main__":
    port = serial.Serial("/dev/ttyUSB0", baudrate=9600)
    port.write_timeout = 5.0
    port.timeout = 5.0

    for i in range(100):
        port.write("hello".encode("ascii"))
        print(port.readline())
        
