import sys

import pygame
from pygame.sprite import Group

from bullet import Bullet
from alien import Alien

def check_events(ai_settings, bullets, screen, ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ai_settings, bullets, event, screen, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(ai_settings, bullets, event, screen, ship):
    """Handle keydown events."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, bullets, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """Handle keyup events."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def create_alien(alien_num):
    alien = Alien()
    alien.rect.x = alien.rect.width + alien.rect.width * 2 * alien_num
    return alien

def create_alien_fleet(screen, screen_width):
    num_aliens = get_num_aliens(screen, screen_width)
    aliens = Group()
    for alien_num in range(num_aliens):
        aliens.add(create_alien(alien_num))
    return aliens

def fire_bullet(ai_settings, bullets, screen, ship):
    if len(bullets) < ai_settings.bullets_allowed:
        bullet = Bullet(ai_settings, screen, ship)
        bullets.add(bullet)

def get_num_aliens(screen, screen_width):
    alien_width = Alien().rect.width
    available_screen_width = screen_width - (2 * alien_width)
    return int(available_screen_width / (2 * alien_width))

def update_screen(ai_settings, aliens, bullets, screen, ship):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and remove old bullets."""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

