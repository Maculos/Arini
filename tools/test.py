import serial
import time
import random

link = serial.Serial(port='COM3', baudrate=19200, timeout=.1)


ts = []
tiles = [
    0,
    4,
    8, # I Tile
    12, # Square Tile
    16, # Z Tile,
    20, # S Tile
    24  # T Tile
]
junk = [
    128,
    129,
    130,
    131,
    132,
    133,
    134,
    135,
    47
]

# Tileset the game uses to seed the randomizer for both systems
def send_tiles():
    for i in range(256):
        link.write(random.choice(tiles))

# Junk data for level select
def send_junk():
    for i in range(100):
        link.write(random.choice(junk))

# Similar to the SPI.transfer() function on arduino (just worse this time!)
def transfer(x):
    link.write(x)
    time.sleep(0.01)
    data = link.readline().decode()
    return data




while True:
    #num = int(input("Send: "))
    #value = transfer(num)
    #print("Read: " + value.decode())

    print("Moving stages...")

    print(transfer(41)) #Start
    time.sleep(.05)
    print(transfer(29)) #Music B

    time.sleep(2) 

    print(transfer(80)) #Move Screen
    time.sleep(.08)
    print(transfer(3)) # Level 3


    #Pain Time

    input("Press Enter Cumsock....")
    print(transfer(96))
    time.sleep(.005)
    print(transfer(41))
    time.sleep(.005)

    send_junk()
    time.sleep(.005)
    print(transfer(41))
    time.sleep(.005)
    send_tiles()

    print(transfer(48))
    time.sleep(.04)
    print(transfer(0))
    time.sleep(.04)
    print(transfer(2))
    time.sleep(.04)
    print(transfer(2))
    time.sleep(.04)
    print(transfer(32))
    time.sleep(.6)