import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, ai_settings.ship_speed_factor)
    bullets = Group()

    # Main game loop.
    while True:
        gf.check_events(ai_settings, bullets, screen, ship)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, bullets, screen, ship)


run_game()
