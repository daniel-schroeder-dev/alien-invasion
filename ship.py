import pygame

class Ship:
    """A Ship for Alien Invasion."""

    def __init__(self, screen, ship_speed_factor):
        """Initialize the ship and set its starting position."""
        self.ship_speed_factor = ship_speed_factor
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('./images/ship.bmp')
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom =  self.screen_rect.bottom

        # Store a decimal value for the ships center.
        self.center = float(self.rect.centerx)

        # Determine if the ship should be moving to the right or left.
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the Ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the ship if the moving_(direction) flag is set."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ship_speed_factor
        # Use if instead of elif so no key gets priority if both are held down.
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ship_speed_factor

        # The rect object only stores integers, so will truncate self.center.
        self.rect.centerx = self.center


