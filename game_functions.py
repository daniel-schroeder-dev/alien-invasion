import sys
from time import sleep

import pygame
from pygame.sprite import Group

from bullet import Bullet
from alien import Alien

def alien_reach_bottom(aliens, screen):
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen.get_rect().bottom:
            return True
    return False

def change_alien_fleet_direction(ai_settings, aliens):
    ai_settings.alien_fleet_direction *= -1
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_vertical_speed_factor

def check_events(ai_settings, bullets, button, scoreboard,
        screen, ship, stats):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ai_settings, bullets, event,
                    scoreboard, screen, ship, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(button, mouse_x, mouse_y, scoreboard, stats)

def check_keydown_events(ai_settings, bullets, event, scoreboard,
        screen, ship, stats):
    """Handle keydown events."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, bullets, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(scoreboard, stats)

def check_keyup_events(event, ship):
    """Handle keyup events."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_play_button(button, mouse_x, mouse_y, scoreboard, stats):
    if button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        start_game(scoreboard, stats)

def create_alien(ai_settings, alien_num, row_num):
    alien = Alien(ai_settings)
    alien.rect.x = alien.rect.width  + alien.rect.width * 2 * alien_num
    alien.rect.y = alien.rect.height + alien.rect.height * 2 * row_num
    alien.start_x = alien.rect.x
    alien.start_y = alien.rect.y
    return alien

def create_alien_fleet(aliens, screen, ai_settings, ship_height):
    num_aliens = get_num_aliens(ai_settings, screen)
    num_rows = get_num_rows(ai_settings, ship_height)
    aliens.empty()
    for row_num in range(num_rows):
        for alien_num in range(num_aliens):
            aliens.add(create_alien(ai_settings, alien_num, row_num))

def detect_edge_collision(aliens, screen):
    for alien in aliens.sprites():
        if alien.rect.right >= screen.get_rect().right:
            return True
        elif alien.rect.left <= 0:
            return True
    return False

def fire_bullet(ai_settings, bullets, screen, ship):
    if len(bullets) < ai_settings.bullets_allowed:
        bullet = Bullet(ai_settings, screen, ship)
        bullets.add(bullet)

def get_num_aliens(ai_settings, screen):
    alien_width = Alien(ai_settings).rect.width
    available_screen_width = ai_settings.screen_width - (2 * alien_width)
    return int(available_screen_width / (2 * alien_width))

def get_num_rows(ai_settings, ship_height):
    alien_height = Alien(ai_settings).rect.height
    avail_screen_height = (
        ai_settings.screen_height -
        (ship_height + alien_height * 3))
    return int(avail_screen_height / (alien_height * 2))

def reset_game(ai_settings, aliens, bullets, screen, ship, stats):
    stats.ships_left -= 1
    aliens.empty()
    bullets.empty()
    ship.center_ship()
    ai_settings.initialize_dynamic_settings()
    create_alien_fleet(aliens, screen, ai_settings, ship.rect.height)
    sleep(0.5)
    if not stats.ships_left:
        stats.game_active = False
        stats.level = 1
        pygame.mouse.set_visible(True)

def start_game(scoreboard, stats):
    stats.game_active = True
    stats.reset_stats()
    scoreboard.prep_level()
    scoreboard.prep_score()
    scoreboard.prep_high_score()
    pygame.mouse.set_visible(False)

def update_screen(ai_settings, aliens, bullets, button,
        scoreboard, screen, ship, stats):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    scoreboard.show_score()

    if not stats.game_active:
        button.draw()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(ai_settings, aliens, bullets, scoreboard, stats):
    """Update position of bullets and remove old bullets."""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            scoreboard.prep_score()
        if stats.score > stats.high_score:
            stats.high_score = stats.score
            scoreboard.prep_high_score()

