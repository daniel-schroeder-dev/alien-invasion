class Settings:
    """Settings for Alien Invasion."""

    def __init__(self):
        """Initialize game settings."""
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        self.ship_speed_factor = 3
        self.ships_limit = 2

        self.bullet_speed_factor = 2
        self.bullet_width = 3 
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        self.alien_speed_factor = 2
        self.alien_vertical_speed_factor = 10

        RIGHT = 1
        LEFT = -1

        self.alien_fleet_direction = RIGHT
