# import pygame
# https://fr.wikibooks.org/wiki/Pygame/Introduction_%C3%A0_Pygame <-- into pygame en français
import sys, time, pygame
from Bombe import Bombe
from pygame.locals import *
from datetime import datetime, timedelta
pygame.init()

size = width, height = 1280, 720

screen = pygame.display.set_mode(size)

bombeJoueur1 = Bombe(screen)
bombeJoueur2 = Bombe(screen)
listeBombeJoueur1 = [0, 0, 0]
listeBombeJoueur2 = [0, 0, 0]

# pygame.joystick.init
# print(pygame.joystick.Joystick.get_axis)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_e:
                listeBombeJoueur1 = bombeJoueur1.poseBombe(5, 640, 360)
                # listeBombeJoueur1 = bombeJoueur1.poseBombe(joueur.getPuissance(), positionXjoueur, positionYjoueur) <-- quand ce sera merge
            if event.key == K_SPACE:
                listeBombeJoueur2 = bombeJoueur2.poseBombe(2, 300, 400)
                # listeBombeJoueur2 = bombeJoueur2.poseBombe(joueur.getPuissance(), positionXjoueur, positionYjoueur) <-- quand ce sera merge
    
    bombeJoueur1.explosion(listeBombeJoueur1)
    bombeJoueur2.explosion(listeBombeJoueur2)

    time.sleep(0.01)
    pygame.display.flip()