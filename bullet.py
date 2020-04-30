import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Represents a bullet fired from the ship."""

    def __init__(self, ai_settings, screen, ship):
        """Initialize bullet's attributes and set initial position."""
        super().__init__()
        self.screen = screen
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

    def update(self):
        """Decreases a bullets y-value by the speed_factor."""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
