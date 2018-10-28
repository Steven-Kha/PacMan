class GameStats:
    def __init__(self, pac_settings):
        self.pac_settings = pac_settings
        self.reset_stats()
        self.game_active = False
        self.score = 0
        self.level = 1

    def reset_stats(self):
        self.score = 0
        self.level = 0
