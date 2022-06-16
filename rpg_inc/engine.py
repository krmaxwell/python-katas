class RPGEngine:
    def __init__(self):
        self.num_players = 0
        self._players = []
        self.ticks = 0

    def add_player(self, player_name: str, speed=0, health=1, weapon="", damage=0):
        self.num_players += 1
        self._players.append(Player(player_name, speed, health, weapon, damage))

    def get_players(self) -> list:
        return self._players

    def process_combat_rpg_file(self, data: str):
        for line in data.split("\n"):
            line = line.strip()
            if line:
                line_data = line.split(",")
                name = line_data[0]
                speed = int(line_data[1])
                health = int(line_data[2])
                weapon = line_data[3].strip()
                damage = int(line_data[4])
                self.add_player(name, speed, health, weapon, damage)

    def do_tick(self):
        self.ticks += 1
        print("Tick: {}".format(self.ticks))

        self._players[0].remaining_ticks -= 1
        self._players[1].remaining_ticks -= 1

        if self._players[0].remaining_ticks <= 0:
            self._players[0].attack(self._players[1])

        if self._players[1].remaining_ticks <= 0:
            self._players[1].attack(self._players[0])


class Player:
    def __init__(self, name, speed, health, weapon, damage):
        self.name = name
        self.speed = speed
        self.health = health
        self.weapon = weapon
        self.damage = damage
        self.remaining_ticks = self.speed

    def attack(self, defender):
        defender.health -= self.damage
        print("Reduce player1 health to {}".format(defender.health))
        self.remaining_ticks = self.speed
