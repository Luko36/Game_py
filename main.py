import time
import pygame
import random
from config import *
import sys

print(screensize)
pygame.init()

screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Pygame Test")


time.sleep(1)
running = True
while running == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(((32, 32, 32)))
    pygame.display.update()
pygame.quit()

