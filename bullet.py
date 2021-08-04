import pygame as pm
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullet modelling"""

    def __init__(self,al_game):
        """creating a bullet at the ship current location """
        super().__init__()
        self.screen = al_game.screen
        self.settings = al_game.settings
        self.colour = al_game.settings.bullet_colour

        # creating bullet at rect(0,0) and set correct position
        self.rect = pm.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = al_game.ship.rect.midtop

        # store bullet positio as decimal value 
        self.y = float(self.rect.y)

    def update(self):
        """move bullet up te screen"""
        # update te decimal position of the bullet 
        self.y -= self.settings.bullet_speed
        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pm.draw.rect(self.screen,self.colour,self.rect)
        