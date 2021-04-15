import pygame
from datetime import datetime, timedelta

class Bombe():
    def __init__(self, displayForBomb):
        self._display = displayForBomb
        self._coordonneX = 0
        self._coordonneY = 0
        self._imageBombe = pygame.image.load("images/bombe.png").convert() #Surface / image de la bombe
        self._imageExplosion = pygame.image.load("images/explosion.png").convert() #Surface / image de l'explosion
        self._time_created = datetime.now()
    
    def poseBombe(self, puissanceJoueur, coordonneX, coordonneY):
        self._display.blit(self._imageBombe, (coordonneX, coordonneY))
        self._time_created = datetime.now()
        return [puissanceJoueur, coordonneX, coordonneY]
    
    def explosion(self, listeVariable):
        if (timedelta(seconds=3) <= datetime.now() - self._time_created):
            # seulement si liste est différent de 0
            if(listeVariable[0] != 0):
                self._coordonneX = listeVariable[1]
                self._coordonneY = listeVariable[2]
                self._display.blit(self._imageExplosion, (self._coordonneX, self._coordonneY))
                for i in range(0, listeVariable[0]+1):
                    #affichages de l'explosion dans les quatres directions
                    self._display.blit(self._imageExplosion, (self._coordonneX+i*40, self._coordonneY))
                    self._display.blit(self._imageExplosion, (self._coordonneX-i*40, self._coordonneY))
                    self._display.blit(self._imageExplosion, (self._coordonneX, self._coordonneY+i*40))
                    self._display.blit(self._imageExplosion, (self._coordonneX, self._coordonneY-i*40))
                
                if(timedelta(seconds=4) <= datetime.now() - self._time_created):
                    self._coordonneX = 0
                    self._coordonneY = 0
                    self._display.blit(self._imageExplosion, (self._coordonneX, self._coordonneY))