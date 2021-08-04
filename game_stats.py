class  GameStats:
    """Tracks the game statistics"""

    def __init__(self,al_game):
        """Initialize statistics"""
        self.settings = al_game.settings
        self.reset_stats()
        self.game_active = True

    
    def reset_stats(self):
        """Initiallize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
