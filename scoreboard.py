import pygame

class Scoreboard():

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.ship_image = pygame.image.load('./images/ship.bmp')
        self.ship_image = self.ship_image.convert()

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True,
                self.text_color, self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_high_score(self):
        high_score_str = '{:,}'.format(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.ai_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def draw_ships(self):
        for ship_num in range(self.stats.ships_left):
            ship_rect = self.ship_image.get_rect()
            ship_rect.left = 10 + ship_num * ship_rect.width
            ship_rect.top = 10
            self.screen.blit(self.ship_image, ship_rect)

    def prep_score(self):
        score_str = '{:,}'.format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                self.ai_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.draw_ships()

