import serial
import time
import random

link = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

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

# Tileset the game uses to seed the randomizer for both systems
def send_tiles():
    for i in range(256):
        link.write(random.choice(tiles))

# Similar to the SPI.transfer() function on arduino (just worse this time!)
def transfer(x):
    link.write(x)
    time.sleep(0.05)
    data = link.readline()
    return data

send_tiles()
while True:
    num = input("Send: ")
    value = transfer(num.encode())
    print("Read: " + value.decode())
    send_tiles()