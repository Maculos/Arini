import serial
import time

link = serial.Serial(port='COM3', baudrate=19200, timeout=.1)


# Similar to the SPI.transfer() function on arduino (just worse this time!)
def transfer(x):
    link.write(x)
    time.sleep(0.01)
    data = link.readline().decode()
    return data




while True:
    num = int(input("Send: "))
    value = transfer(num)
    print("Read: " + value)