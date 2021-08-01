import sys
import pygame as pm
from pygame.constants import KEYDOWN
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall asset to manage game assets and behaviours"""

    def __init__(self):
        """initialize game and create game resources"""
        pm.init()
        self.settings = Settings()
        # set screen dimention
        self.screen = pm.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pm.display.set_caption("Alien Invasion")
        self.ship = Ship(self)


    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
    
    
    def _check_events(self):
        """watch for keyboard and mouse events"""
        for event in pm.event.get():
            if event.type == pm.QUIT:
                sys.exit()
            
            elif event.type == pm.KEYDOWN:
                if event.key == pm.K_RIGHT:
                    # move the ship to the right 
                    self.ship.moving_right = True
            
                elif event.key == pm.K_LEFT:
                    # move the ship to the left 
                    self.ship.moving_left = True

            elif event.type == pm.KEYUP:
                if event.key == pm.K_RIGHT:
                    # move the ship to the right 
                    self.ship.moving_right = False
            
                elif event.key == pm.K_LEFT:
                    # move the ship to the left 
                    self.ship.moving_left = False




    def _update_screen(self):
        """redraw the  screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # make screen visible
        pm.display.flip()


if __name__ == "__main__":
    # make the game instance and run
    al = AlienInvasion()
    al.run_game()