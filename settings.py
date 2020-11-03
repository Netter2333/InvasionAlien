class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #Missile settings
        self.missile_speed = 0.8
        self.missile_width = 6
        self.missile_height = 30
        self.missile_color = (174, 59, 34)
        self.missiles_allowed = 1