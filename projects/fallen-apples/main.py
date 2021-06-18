import pygame as pyg 
import pymunk as pyk 
import sys

# Initializing pygame
pyg.init()
window = pyg.display.set_mode((600, 600))
clock = pyg.time.Clock()

while True:
    # Chking for user inputs 
    for event in pyg.event.get(): 
        if event.type == pyg.QUIT:
            pyg.quit()
            sys.exit()

    window.fill((217, 217, 217)) #BG color
    pyg.display.update() #Rendring the frame
    clock.tick(120) # limiting the frame to 120 seconds

