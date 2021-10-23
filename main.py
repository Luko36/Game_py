import pygame
import random
from config import *
import sys


pygame.init()
pozadie = pygame.image.load("asets/images/pozadieTest.png")

print(screensize)


screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Pygame Test")

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(pozadie, [0,0])
   
    pygame.display.update()
pygame.quit()