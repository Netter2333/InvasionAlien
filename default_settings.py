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

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Missile settings
        self.missile_speed = 0.8
        self.missile_width = 6
        self.missile_height = 30
        self.missile_color = (174, 59, 34)
        self.missiles_allowed = 1

        # Alien settings
        self.alien_speed = 0.7
        self.fleet_drop_speed = 4
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1