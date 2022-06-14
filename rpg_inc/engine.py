class RPGEngine:
    def __init__(self):
        self.num_players = 0
        self._players = []

    def add_player(self, player_name):
        self.num_players += 1

