class RPGEngine:
    def __init__(self):
        self.num_players = 0
        self._players = []

    def add_player(self, player_name):
        self.num_players += 1
        self._players.append(Player(player_name))

    def get_players(self):
        return self._players

    def process_combat_rpg_file(self, data):
        for line in data.split("\n"):
            line = line.strip()
            if line:
                name = line.split(",")[0]
                self.add_player(name)

class Player:
    def __init__(self, name):
        self.name = name
