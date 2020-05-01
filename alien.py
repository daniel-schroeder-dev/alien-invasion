import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings):
        super().__init__()
        self.screen_width = ai_settings.screen_width
        self.ai_settings = ai_settings

        self.image = pygame.image.load('./images/alien.bmp')
        self.image = self.image.convert()
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        self.moving_right = True
        self.hit_left_edge = False
        self.hit_right_edge = False

    def update(self):

        self.rect.x += self.ai_settings.alien_fleet_direction * self.ai_settings.alien_speed_factor
