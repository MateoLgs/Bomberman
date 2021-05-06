import pygame
from datetime import datetime, timedelta

class BombeCopy(pygame.sprite.Sprite):
    def __init__(self, displayForBomb, posX, posY, puissanceJoueur):
        super(BombeCopy, self)
        self._display = displayForBomb
        self._coordonneX = posX
        self._coordonneY = posY
        self._imageBombe = pygame.image.load("images/bombe.png").convert() #Surface / image de la bombe
        self._imageExplosion = pygame.image.load("images/explosion.png").convert() #Surface / image de l'explosion
        self._time_created = datetime.now()
        self._puissance = puissanceJoueur
        self.explosion()
    
    
    def explosion(self):
        if (timedelta(seconds=3) <= datetime.now() - self._time_created):
            # seulement si liste est différent de 0
            if(self._puissance != 0):
                self._display.blit(self._imageExplosion, (self._coordonneX, self._coordonneY))
                for i in range(0, self._puissance+1):
                    #affichages de l'explosion dans les quatres directions
                    self._display.blit(self._imageExplosion, (self._coordonneX+i*40, self._coordonneY))
                    self._display.blit(self._imageExplosion, (self._coordonneX-i*40, self._coordonneY))
                    self._display.blit(self._imageExplosion, (self._coordonneX, self._coordonneY+i*40))
                    self._display.blit(self._imageExplosion, (self._coordonneX, self._coordonneY-i*40))
                
                if(timedelta(seconds=4) <= datetime.now() - self._time_created):
                    self.kill()
                    print(self.kill())

# buttons = pygame.sprite.Group()
# buttons.add(
#     Button(pos=(50, 25), image=image),
#     Button(pos=(50, 75), image=image),
#     Button(pos=(50, 125), image=image)
# )