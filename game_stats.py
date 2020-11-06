class GameStats:
    """Track statistics for Invasion Alien."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start the game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        high_score_file = 'text_files/high_score.txt'
        try:
            with open(high_score_file, 'r') as f:
                for line in f:
                    if line:
                        self.high_score = float(f.readline())
        except FileNotFoundError:
            with open(high_score_file, 'w') as f:
                self.high_score = 1
                f.write(f"{self.high_score}")

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
