import pygame as pm


class Ship:
    """user ship class"""

    def __init__(self, al_game):
        """ship attributes"""
        self.screen = al_game.screen
        self.screen_rect = al_game.screen.get_rect()

        # load te ship imae and et the rectangle
        self.image = pm.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()


        # start new ship at the bottom corner of the screen 
        self.rect.midbottom = self.screen_rect.midbottom

        # movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """update the ship position based on movement flag"""
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1
            
    
    def blitme(self):
        """draw thhe ship at its current location"""
        self.screen.blit(self.image,self.rect)


    




