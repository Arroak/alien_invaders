import pygame as pm


class Ship:
    """user ship class"""

    def __init__(self, al_game):
        """ship attributes"""
        self.screen = al_game.screen
        self.screen_rect = al_game.screen.get_rect()
        self.settings = al_game.settings
        # load te ship imae and et the rectangle
        self.image = pm.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()


        # start new ship at the bottom corner of the screen 
        self.rect.midbottom = self.screen_rect.midbottom

        # store decimal value for the ship orizontal position
        self.x = float(self.rect.x)
        # movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """update the ship position based on movement flag"""
        # update ship x value not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0 :
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x
            
    
    def blitme(self):
        """draw thhe ship at its current location"""
        self.screen.blit(self.image,self.rect)


    




