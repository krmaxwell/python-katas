import contextlib
import io
import unittest

from rpg_inc.engine import Player, RPGEngine


class TestRPGEngine(unittest.TestCase):
    def setUp(self) -> None:
        # Name, Speed, Health, Weapon, Damage
        self.combat_rpg_file = """
        'Mark The Fister', 4, 8, 'Iron Fist', 4
        'John The Bagger', 1, 7, 'Small Bag', 1
        """
        self.engine = RPGEngine()

    def test_init(self):
        self.assertIsInstance(self.engine, RPGEngine)

    def test_add_players(self):
        self.assertEqual(0, self.engine.num_players)

        self.engine.add_player("player1")
        self.assertEqual(1, self.engine.num_players)
        self.assertIsInstance(self.engine.get_players()[0], Player)
        self.assertEqual("player1", self.engine.get_players()[0].name)

        self.engine.add_player("player2")
        self.assertEqual(2, self.engine.num_players)
        self.assertIsInstance(self.engine.get_players()[1], Player)
        self.assertEqual("player2", self.engine.get_players()[1].name)

    def test_combat_rpg_file(self):
        self.engine.process_combat_rpg_file(self.combat_rpg_file)
        self.assertEqual(2, self.engine.num_players)

        player0 = self.engine.get_players()[0]
        self.assertEqual("'Mark The Fister'", player0.name)
        self.assertEqual(4, player0.speed)
        self.assertEqual(8, player0.health)
        self.assertEqual("'Iron Fist'", player0.weapon)
        self.assertEqual(4, player0.damage)

        player1 = self.engine.get_players()[1]
        self.assertEqual(1, player1.speed)
        self.assertEqual(7, player1.health)
        self.assertEqual("'Small Bag'", player1.weapon)
        self.assertEqual(1, player1.damage)

    def test_single_tick(self):
        self.engine.process_combat_rpg_file(self.combat_rpg_file)
        self.assertEqual(0, self.engine.ticks)
        self.engine.do_tick()
        self.assertEqual(1, self.engine.ticks)

        player0 = self.engine.get_players()[0]
        self.assertEqual(7, player0.health)
        player1 = self.engine.get_players()[1]
        self.assertEqual(7, player1.health)

    def test_tick_until_player_dies(self):
        self.engine.process_combat_rpg_file(self.combat_rpg_file)
        player0 = self.engine.get_players()[0]
        player1 = self.engine.get_players()[1]

        while player0.health > 0 and player1.health > 0:
            self.engine.do_tick()
        self.assertTrue(player0.health <= 0 or player1.health <= 0)
        self.assertEqual(8, self.engine.ticks)

    def test_result_rpg_file(self):
        self.engine.process_combat_rpg_file(self.combat_rpg_file)
        player0 = self.engine.get_players()[0]
        player1 = self.engine.get_players()[1]
        with contextlib.redirect_stdout(io.StringIO()) as output:
            self.engine.do_tick()
            # output: Tick, Attacker, Defender, Weapon, Damage, Attacker Health, Defender Health
            self.assertEqual(
                "1,'John The Bagger','Mark The Fister','Small Bag',1,7,7\n",
                output.getvalue(),
            )
            while player0.health > 0 and player1.health > 0:
                self.engine.do_tick()
            log = output.getvalue()
            
        print(log)
        self.assertEqual(10, len(log.split("\n")))

