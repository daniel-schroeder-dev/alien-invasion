import sys
import pygame

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Alien Invasion")

    bg_color = (230, 230, 230)

    # Main game loop.
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
