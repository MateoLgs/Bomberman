# import pygame
# https://fr.wikibooks.org/wiki/Pygame/Introduction_%C3%A0_Pygame <-- into pygame en français
import sys, time, pygame
from Explosion import Explosion
pygame.init()

size = width, height = 1280, 720

screen = pygame.display.set_mode(size)

test = Explosion(1, 640, 360, screen)
test.explosionBombe()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    time.sleep(0.01)
    pygame.display.flip()