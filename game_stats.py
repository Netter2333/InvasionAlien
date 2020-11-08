class GameStats:
    """Track statistics for Invasion Alien."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start the game in an inactive state.
        self.game_active = False
        self.high_score = 0

        # High score should never be reset.
        high_score_file = 'text_files/high_score.txt'
        try:
            with open(high_score_file, 'r') as f:
                for line in f:
                    line = line.split()
                    high_scores = [int(i) for i in line]
                    if line:
                        self.high_score = high_scores[0]
        except FileNotFoundError:
            with open(high_score_file, 'w') as f:
                f.write(f"{self.high_score}")

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
