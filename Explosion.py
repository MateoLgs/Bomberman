import pygame
import time

class Explosion():
    def __init__(self, puissance, coordonneX, coordonneY, displayForExplosion):
        self._puissance = puissance+1 #int / puissance de la bombe du joueur / min = 2
        self._coordonneX = coordonneX #int / coordonnées X et Y de la bombe = origine de l'explosion
        self._coordonneY = coordonneY #int / coordonnées X et Y de la bombe = origine de l'explosion
        self._display = displayForExplosion #Surface / permet l'affichage de l'explosion
        self._imageExplosion = pygame.image.load("images/explosion.png") #Surface / image de l'explosion

    def explosionBombe(self):
        #affichage de l'explosion au coordonnés de la bombe
        self._display.blit(self._imageExplosion, (self._coordonneX, self._coordonneY))
        for i in range(0, self._puissance):
            #affichages de l'explosion dans les quatres directions
            self._display.blit(self._imageExplosion, (self._coordonneX+i*40, self._coordonneY))
            self._display.blit(self._imageExplosion, (self._coordonneX-i*40, self._coordonneY))
            self._display.blit(self._imageExplosion, (self._coordonneX, self._coordonneY+i*40))
            self._display.blit(self._imageExplosion, (self._coordonneX, self._coordonneY-i*40))
        
        # Fait disparaitre la bombe au bout d'un certain temps : (well this doesn't work)
        # pygame.time.wait(5)
        # self.kill()