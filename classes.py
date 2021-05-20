import pygame
from pygame.locals import *
from variables import *
from datetime import datetime, timedelta


class Niveau:
    """class de l'ffichage du terrain"""
    def __init__(self, fichier):
        """initialisation des variables de la class"""
        self.fichier = fichier
        self.structure = [[]]

    def generer(self):
        """lecture du fichier du niveau"""
        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            for ligne in fichier:
                ligne_niveau = []
                for sprite in ligne:
                    if sprite != "\n":
                        ligne_niveau.append(sprite)
                structure_niveau.append(ligne_niveau)
            self.structure = structure_niveau

    def afficher(self, fenetre):
        """définition des images du niveau"""
        brick = pygame.image.load(image_brick)
        pillar = pygame.image.load(pilier)
        sol = pygame.image.load(imageSol)

        num_ligne = 0
        # parcours de la double liste du terrain
        for ligne in self.structure:
            num_case = 0
            for sprite in ligne:
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite

                if sprite == "p":
                    fenetre.blit(pillar, (x, y))
                elif sprite == "s":
                    fenetre.blit(sol, (x, y))
                elif sprite == "b":
                    fenetre.blit(brick, (x, y))
                num_case += 1
            num_ligne += 1

    def detruire(self, case_x, case_y):
        """destruction d'un bloc du terrain"""
        self.structure[int(case_x)][int(case_y)] = "s"


class Perso:
    """Classe permettant de créer un personage"""

    def __init__(self, droite, gauche, haut, bas, niveau):
        # initialisation des images et gestion de la transparance
        self.droite = pygame.image.load(droite).convert()
        self.droite.set_colorkey((255, 255, 255))
        self.gauche = pygame.image.load(gauche).convert()
        self.gauche.set_colorkey((255, 255, 255))
        self.haut = pygame.image.load(haut).convert()
        self.haut.set_colorkey((255, 255, 255))
        self.bas = pygame.image.load(bas).convert()
        self.bas.set_colorkey((255, 255, 255))
        # position de base du perso
        self.case_x = 1
        self.case_y = 1
        self.x = taille_sprite * self.case_x
        self.y = taille_sprite * self.case_y

        self.direction = self.droite
        self.niveau = niveau

    def deplacer(self, direction):
        """Methode de déplacement du personnage"""

        if direction == "droite":
            self.x +=5
            self.direction = self.droite
        if direction == "gauche":
            self.x -=5
            self.direction = self.gauche
        if direction == "haut":
            self.y -=5
            self.direction = self.haut
        if direction == "bas":
            self.y +=5
            self.direction = self.bas


class Perso2:
    def __init__(self, droite, gauche, haut, bas, niveau):
        # initialisation des images et gestion de la transparance
        self.droite = pygame.image.load(droite).convert()
        self.droite.set_colorkey((255, 255, 255))
        self.gauche = pygame.image.load(gauche).convert()
        self.gauche.set_colorkey((255, 255, 255))
        self.haut = pygame.image.load(haut).convert()
        self.haut.set_colorkey((255, 255, 255))
        self.bas = pygame.image.load(bas).convert()
        self.bas.set_colorkey((255, 255, 255))
        # position de base
        self.case_x = 14
        self.case_y = 14
        self.x = taille_sprite * self.case_x
        self.y = taille_sprite * self.case_y
        self.direction = self.haut
        self.niveau = niveau

    def deplacer(self, direction):
        if direction == "droite":
            self.x +=5
            self.direction = self.droite

        if direction == "gauche":
            self.x -=5
            self.direction = self.gauche
        if direction == "haut":
            self.y -=5
            self.direction = self.haut
        if direction == "bas":
            self.y +=5
            self.direction = self.bas




class Bomb:

    def __init__(self, bomb, niveau, perso1, perso2):
        self.bomb = pygame.image.load(bomb).convert()
        self.x = 1000
        self.y = 1000
        self.case_x = 255
        self.case_y = 255
        self._time_created = datetime.now()
        self.niveau = niveau
        self.perso1 = perso1
        self.perso2 = perso2
        self.explosion = 0

    def poser(self, x, y, bomb):
        self.bomb = pygame.image.load(bomb).convert()
        self.bomb.set_colorkey((255, 255, 255))
        self.x = x
        self.y = y
        self.case_x = int(x / taille_sprite)
        self.case_y = int(y / taille_sprite)
        self._time_created = datetime.now()
        self.explosion = 0

    def exploser(self):

        if timedelta(seconds=3) <= datetime.now() - self._time_created:
            self.bomb = pygame.image.load(imageExplosion).convert()
            self.bomb.set_colorkey((255, 255, 255))
            self.explosion = 1

            try:
                if self.niveau.structure[self.case_y][self.case_x + 1] == "b":
                    self.niveau.detruire(self.case_y, self.case_x + 1)

                if self.niveau.structure[self.case_y][self.case_x - 1] == "b":
                    self.niveau.detruire(self.case_y, self.case_x - 1)

                if self.niveau.structure[self.case_y - 1][self.case_x] == "b":
                    self.niveau.detruire(self.case_y - 1, self.case_x)

                if self.niveau.structure[self.case_y + 1][self.case_x] == "b":
                    self.niveau.detruire(self.case_y + 1, self.case_x)

                
                #if self.case_x == self.perso1.case_x and self.case_y - 1 <= self.perso1.case_y <= self.case_y + 1:
                    #return 1
                #elif self.case_x - 1 <= self.perso1.case_x <= self.case_x + 1 and self.case_y == self.perso1.case_y:
                    #return 1

                #if self.case_x == self.perso2.case_x and self.case_y - 1 <= self.perso2.case_y <= self.case_y + 1:
                    #return 1
                #elif self.case_x - 1 <= self.perso2.case_x <= self.case_x + 1 and self.case_y == self.perso2.case_y:
                    #return 1

            except IndexError:
                pass

        if timedelta(milliseconds=3500) <= datetime.now() - self._time_created:
            self.x = 1000
            self.y = 1000
            self.case_x = 255
            self.case_y = 255
            self.explosion = 0


class Bomb2:

    def __init__(self, bomb, niveau, perso1, perso2):
        self.bomb = pygame.image.load(bomb).convert()
        self.x = 1000
        self.y = 1000
        self.case_x = 255
        self.case_y = 255
        self._time_created = datetime.now()
        self.niveau = niveau
        self.perso1 = perso1
        self.perso2 = perso2
        self.explosion = 0

    def poser(self, x, y, bomb):
        self.bomb = pygame.image.load(bomb).convert()
        self.bomb.set_colorkey((255, 255, 255))
        self.x = x
        self.y = y
        self.case_x = int(x / taille_sprite)
        self.case_y = int(y / taille_sprite)
        self._time_created = datetime.now()
        self.explosion = 0

    def exploser(self):

        if timedelta(seconds=3) <= datetime.now() - self._time_created:
            self.bomb = pygame.image.load(imageExplosion).convert()
            self.bomb.set_colorkey((255, 255, 255))
            self.explosion = 1

            try:
                if self.niveau.structure[self.case_y][self.case_x + 1] == "b":
                    self.niveau.detruire(self.case_y, self.case_x + 1)

                if self.niveau.structure[self.case_y][self.case_x - 1] == "b":
                    self.niveau.detruire(self.case_y, self.case_x - 1)

                if self.niveau.structure[self.case_y - 1][self.case_x] == "b":
                    self.niveau.detruire(self.case_y - 1, self.case_x)

                if self.niveau.structure[self.case_y + 1][self.case_x] == "b":
                    self.niveau.detruire(self.case_y + 1, self.case_x)

                #if self.case_x == self.perso1.case_x and self.case_y - 1 <= self.perso1.case_y <= self.case_y + 1:
                #    return 1
                #elif self.case_x - 1 <= self.perso1.case_x <= self.case_x + 1 and self.case_y == self.perso1.case_y:
                #    return 1

                #if self.case_x == self.perso2.case_x and self.case_y - 1 <= self.perso2.case_y <= self.case_y + 1:
               #     return 1
                #elif self.case_x - 1 <= self.perso2.case_x <= self.case_x + 1 and self.case_y == self.perso2.case_y:
                 #   return 1
            except IndexError:
                pass

        if timedelta(milliseconds=3500) <= datetime.now() - self._time_created:
            self.x = 1000
            self.y = 1000
            self.case_x = 255
            self.case_y = 255
            self.explosion = 0


class Flammes:
    def __init__(self, fflamme_d, fflamme_g, fflamme_h, fflamme_b):
        self.fflamme_d = pygame.image.load(fflamme_d).convert()
        self.fflamme_d.set_colorkey((255, 255, 255))
        self.fflamme_g = pygame.image.load(fflamme_g).convert()
        self.fflamme_g.set_colorkey((255, 255, 255))
        self.fflamme_h = pygame.image.load(fflamme_h).convert()
        self.fflamme_h.set_colorkey((255, 255, 255))
        self.fflamme_b = pygame.image.load(fflamme_b).convert()
        self.fflamme_b.set_colorkey((255, 255, 255))
