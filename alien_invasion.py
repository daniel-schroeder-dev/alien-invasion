import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
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
    aliens = gf.create_alien_fleet(screen, ai_settings, ship.rect.height)
    stats = GameStats(ai_settings)

    it = 0

    # Main game loop.
    while True:
        it += 1
        gf.check_events(ai_settings, bullets, screen, ship)
        ship.update()
        gf.update_bullets(aliens, bullets)
        if len(aliens) is 0:
            aliens = gf.create_alien_fleet(screen, ai_settings, ship.rect.height)
            bullets.empty()
        if not (it % 3):
            aliens.update()
            if pygame.sprite.spritecollideany(ship, aliens):
                aliens = gf.reset_game(ai_settings, aliens, 
                        bullets, screen, ship, stats)
            if gf.detect_edge_collision(aliens, screen):
                gf.change_alien_fleet_direction(ai_settings, aliens)
            
        gf.update_screen(ai_settings, aliens, bullets, screen, ship)

run_game()
