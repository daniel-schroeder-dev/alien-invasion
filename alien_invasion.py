import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
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
    aliens = Group()
    gf.create_alien_fleet(aliens, screen, ai_settings, ship.rect.height)
    stats = GameStats(ai_settings)
    clock = pygame.time.Clock()
    button = Button("Play", screen)

    # Main game loop.
    while True:
        clock.tick(60)
        gf.check_events(ai_settings, bullets, button, screen, ship, stats)

        if stats.game_active:
            ship.update()
            gf.update_bullets(aliens, bullets)

            if len(aliens) is 0:
                bullets.empty()
                ai_settings.increase_speed()
                gf.create_alien_fleet(aliens, screen, ai_settings, ship.rect.height)

            aliens.update()

            if gf.detect_edge_collision(aliens, screen):
                gf.change_alien_fleet_direction(ai_settings, aliens)

            if pygame.sprite.spritecollideany(ship, aliens) or \
                    gf.alien_reach_bottom(aliens, screen):
                gf.reset_game(ai_settings, aliens,
                        bullets, screen, ship, stats)

        gf.update_screen(ai_settings, aliens, bullets,
                button, screen, ship, stats)

run_game()
