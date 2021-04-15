import pygame
from datetime import datetime, timedelta

class Bombe():
    def __init__(self, displayForBomb):
        self._display = displayForBomb
        self._imageBombe = pygame.image.load("images/bombe.png") #Surface / image de la bombe
        self._imageExplosion = pygame.image.load("images/explosion.png") #Surface / image de l'explosion
        self._time_created = datetime.now()
    
    def poseBombe(self, puissanceJoueur, coordonneX, coordonneY):
        self._display.blit(self._imageBombe, (coordonneX, coordonneY))
        self._time_created = datetime.now()
        return [puissanceJoueur, coordonneX, coordonneY]
    
    def explosion(self, listeVariable):
        if (timedelta(seconds=3) <= datetime.now() - self._time_created):
            # seulement si liste est différent de 0
            if(listeVariable[0] != 0):
                self._display.blit(self._imageExplosion, (listeVariable[1], listeVariable[2]))
                for i in range(0, listeVariable[0]+1):
                    #affichages de l'explosion dans les quatres directions
                    self._display.blit(self._imageExplosion, (listeVariable[1]+i*40, listeVariable[2]))
                    self._display.blit(self._imageExplosion, (listeVariable[1]-i*40, listeVariable[2]))
                    self._display.blit(self._imageExplosion, (listeVariable[1], listeVariable[2]+i*40))
                    self._display.blit(self._imageExplosion, (listeVariable[1], listeVariable[2]-i*40))
                
                # if(timedelta(seconds=4) <= datetime.now() - self._time_created):
                #     self._imageExplosion.kill()
                    # pygame.sprite.kill(self._imageBombe)