class RPGEngine:
    def __init__(self):
        self.num_players = 0
        self._players = []

    def add_player(self, player_name):
        self.num_players += 1
        self._players.append(Player(player_name))

    def get_players(self):
        return self._players

class Player:
    def __init__(self, name):
        self.name = name
