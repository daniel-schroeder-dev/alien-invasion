class Settings:
    """Settings for Alien Invasion."""

    def __init__(self):
        """Initialize game settings."""
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        self.ship_speed_factor = 0.3

        self.bullet_speed_factor = 0.3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
