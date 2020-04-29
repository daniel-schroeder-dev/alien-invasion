import sys

import pygame

from settings import Settings

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Main game loop.
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()