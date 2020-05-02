class GameStats:

    def __init__(self, ai_settings):
        super().__init__()
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.ai_settings.ships_limit