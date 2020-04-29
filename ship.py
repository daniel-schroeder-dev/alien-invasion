import pygame

class Ship:
    """A Ship for Alien Invasion."""

    def __init__(self, ship_speed_factor, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ship_speed_factor = ship_speed_factor

        # Load the ship image and get its rect.
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom =  self.screen_rect.bottom

        # Store a decimal value for the ships center
        self.center = float(self.rect.centerx)

        # Determine if the ship should be moving to the right.
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the Ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the ship if the moving_(direction) flag is set."""
        if self.moving_right:
            self.center += self.ship_speed_factor
        # Use if instead of elif so no key gets priority if both are held down.
        if self.moving_left:
            self.center -= self.ship_speed_factor

        # The rect object only stores integers, so will truncate self.center.
        self.rect.centerx = self.center


