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

        player0 = self._players[0]
        player0.remaining_ticks -= 1
        player1 = self._players[1]
        player1.remaining_ticks -= 1

        if player0.remaining_ticks <= 0:
            player0.attack(player1)
            print(
                "{},{},{},{},{},{},{}".format(
                    self.ticks,
                    player0.name,
                    player1.name,
                    player0.weapon,
                    player0.damage,
                    player0.health,
                    player1.health,
                )
            )

        if player1.remaining_ticks <= 0:
            player1.attack(player0)
            print(
                "{},{},{},{},{},{},{}".format(
                    self.ticks,
                    player1.name,
                    player0.name,
                    player1.weapon,
                    player1.damage,
                    player0.health,
                    player1.health,
                )
            )


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
        self.remaining_ticks = self.speed
