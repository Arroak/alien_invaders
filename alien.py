import pygame as pm
from pygame.sprite import Sprite


class Alien(Sprite):
    """Alien model"""

    def __init__(self,al_game):
        """Initialize alien attributes and starting position"""
        super().__init__()
        self.screen = al_game.screen
        self.settings = al_game.settings
        # load alien image and set its attributes
        self.image = pm.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # start a new alien at top left corner 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact orizontal position
        self.x = float(self.rect.x)

    def update(self):
        """move alien left and right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """return True whemn te alien is at the edge of te screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True