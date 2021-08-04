class Settings:
    """A class to9 store all settings"""

    def __init__(self):
        """initiallizing settings"""
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.ship_speed = 2.5
        self.ship_limit = 3
        # bullet settings
        self.bullet_speed = 1.5
        self.bullet_width =  3
        self.bullet_height = 15
        self.bullet_colour = (200,60,60)
        self.bullets_allowed = 50
        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 1
        #fleet direction 1 reps right and -1 reps left
        self.fleet_direction = 1
