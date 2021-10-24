import pygame
import sys
from config import screensize

# screen
pygame.init()
pozadie = pygame.image.load("asets/images/pozadieTest.png")
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Pygame Test")
pygame.mixer.music.load('MagioExpres_-_Pokus.mp3')
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()


player_first_y = (screensize[1]/3.22388)-(screensize[1]/21.6)
player_second_y = (screensize[1]/1.6)-(screensize[1]/21.6)
player_third_y = (screensize[1]/1.06404)-(screensize[1]/21.6)

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.blit(pozadie, [0, 0])
    pygame.draw.rect(screen, "red", pygame.Rect(0, 45, screensize[0], (screensize[1]/3.48387)))# (screensize[1]/3.48387) = 310px
    pygame.draw.rect(screen, "purple", pygame.Rect(0, 385, screensize[0], (screensize[1]/3.48387)))
    pygame.draw.rect(screen, "blue", pygame.Rect(0, 730, screensize[0], (screensize[1]/3.48387)))
    pygame.draw.rect(screen, "green", pygame.Rect((screensize[0]/3), player_first_y, (screensize[0]/38.4), (screensize[1]/21.6)))
    pygame.draw.rect(screen, "green", pygame.Rect((screensize[0]/3), player_second_y, (screensize[0]/38.4), (screensize[1]/21.6)))
    pygame.draw.rect(screen, "green", pygame.Rect((screensize[0]/3), player_third_y, (screensize[0]/38.4), (screensize[1]/21.6)))
    pygame.display.update()
    clock.tick(120)
pygame.quit()


"""
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
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(((32, 32, 32)))
    pygame.draw.rect(screen, "red", pygame.Rect(0, 45, screensize[0], 310))
    pygame.draw.rect(screen, "purple", pygame.Rect(0, 385, screensize[0], 310))
    pygame.draw.rect(screen, "blue", pygame.Rect(0, 730, screensize[0], 310))
    pygame.display.update()
    #screen.blit()
pygame.quit()
"""