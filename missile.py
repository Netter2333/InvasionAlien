import pygame
from pygame.sprite import Sprite


class Missile(Sprite):
    """A class to manage missiles fired from the ship."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.missile_color

        # Create a missile rect at (0,0) then correct position.
        self.rect = pygame.Rect(0, 0,
                                self.settings.missile_width,
                                self.settings.missile_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the missile position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the missile up the screen."""
        # Update decimal position of the missile.
        self.y -= self.settings.missile_speed  # minus since y goes 'down' as you look 'up' the screen.
        # Update the rect position.
        self.rect.y = self.y

    def draw_missile(self):
        """Draw the missile to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
