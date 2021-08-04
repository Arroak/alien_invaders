import sys
import pygame as pm
from pygame import sprite
import pygame
from pygame.constants import KEYDOWN
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats


class AlienInvasion:
    """Overall asset to manage game assets and behaviours"""

    def __init__(self):
        """initialize game and create game resources"""
        pm.init()
        self.settings = Settings()
        # set screen dimention
        self.screen = pm.display.set_mode((0,0),pm.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pm.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pm.sprite.Group()
        self.aliens = pm.sprite.Group()
        self._create_fleet()

    def _ship_hit(self):
        """Respond to the ship it by the alien"""
        if self.stats.ships_left > 0:
        #decreases ship left
            self.stats.ships_left -= 1

        # get rid of remainin aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

        # create a new fleet and center the ship 
            self._create_fleet()
            self.ship.center_ship()

        #pause
            sleep(0.5)
        else:  self.stats.game_active = False

    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

        
    def _check_events(self):
        """watch for keyboard and mouse events"""
        for event in pm.event.get():
            if event.type == pm.QUIT:
                sys.exit()
            
            elif event.type == pm.KEYDOWN:
                self._check_keydown_events(event)
            
            elif event.type == pm.KEYUP:
                self._check_keyup_events(event)
                
            

    def _update_screen(self):
        """redraw the  screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        # make screen visible
        pm.display.flip()

    def _check_keyup_events(self,event):
        if event.key == pm.K_RIGHT:
            # move the ship to the right 
            self.ship.moving_right = False
        elif event.key == pm.K_LEFT:
            # move the ship to the left 
            self.ship.moving_left = False


    def _check_keydown_events(self,event):
        if event.key == pm.K_RIGHT:
            # move the ship to the right 
            self.ship.moving_right = True
        
        elif event.key == pm.K_LEFT:
            # move the ship to the left 
            self.ship.moving_left = True
        elif event.key == pm.K_q :
            sys.exit()

        elif event.key == pm.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """update position of bullets and add to the bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """draw new bullets and delete old bullets"""
        self.bullets.update()
        # get rid of disappered bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()

        
    def _check_bullet_alien_collision(self):
        """check for any bullet that have hit aliens, and get rid of such alien and bullet"""
        collisions = pm.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if not self.aliens:
            #destroy existin bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()



    def _create_fleet(self):
        """create a fleet of aliens"""
        # create an alien and find the max number of aliens per row
        # space between two aliens is equal to the width of one row 
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_of_alien_x = available_space_x // (2 * alien_width)
        
        # determine the number of alien that fits into the screen 
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        row_numbers = available_space_y // (2 * alien_height) 
        #create full fleet of aliens
        for row_number in range(row_numbers):
        # create the first row of aliens  
            for alien_number in range(available_space_x):
            # create an alien and place it in a row 
                self._create_alien(alien_number,row_number)

    def _create_alien(self, alien_number,row_number):
        """create an alien on a row"""
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width  + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height  + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """check if the fleet is at an edge,
        then update the direction of all te aliens in that fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        #look for alien and ship collision
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        
        # look for aliens hitting the bottom
        self._check_aliens_bottom()


    def center_ship(self):
        """positions te ship to te center"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def _check_fleet_edges(self):
        """respond appropriately when an alien reaches the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Drop the entire fleet and chane fleet direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _check_aliens_bottom(self):
        """check if an alien as reaced thhe bottom of the ship"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #treat as ship ot hit
                self._ship_hit()
                break




if __name__ == "__main__":
    # make the game instance and run
    al = AlienInvasion()
    al.run_game()