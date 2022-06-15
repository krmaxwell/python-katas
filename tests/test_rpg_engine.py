import unittest

from rpg_inc.engine import Player, RPGEngine


class TestRPGEngine(unittest.TestCase):

    def setUp(self) -> None:
        self.combat_rpg_file = """
        'Mark the Fister', 4, 8, 'Iron Fist', 4
        'John the Bagger', 1, 7, 'Small Bag', 1
        """

    def test_init(self):
        engine = RPGEngine()
        self.assertIsInstance(engine, RPGEngine)

    def test_add_players(self):
        engine = RPGEngine()
        self.assertEqual(0, engine.num_players)
        engine.add_player("player1")
        self.assertEqual(1, engine.num_players)
        self.assertIsInstance(engine.get_players()[0], Player)
        self.assertEqual("player1", engine.get_players()[0].name)
        engine.add_player("player2")
        self.assertEqual(2, engine.num_players)
        self.assertIsInstance(engine.get_players()[1], Player)
        self.assertEqual("player2", engine.get_players()[1].name)

    def test_combat_rpg_file(self):
        engine = RPGEngine()
        engine.process_combat_rpg_file(self.combat_rpg_file)
        self.assertEqual(2, engine.num_players)
        player0 = engine.get_players()[0]
        self.assertEqual("'Mark the Fister'", player0.name)
        self.assertEqual(4, player0.speed)
        self.assertEqual(8, player0.health)
        self.assertEqual("'Iron Fist'", player0.weapon)
        self.assertEqual(4, player0.damage)
        player1 = engine.get_players()[1]
        self.assertEqual(1, player1.speed)
        self.assertEqual(7, player1.health)
        self.assertEqual("'Small Bag'", player1.weapon)
        self.assertEqual(1, player1.damage)

    def test_single_tick(self):
        engine = RPGEngine()
        engine.process_combat_rpg_file(self.combat_rpg_file)
        self.assertEqual(0, engine.ticks)
        engine.do_tick()
        player0 = engine.get_players()[0]
        self.assertEqual(1, engine.ticks)
        self.assertEqual(7, player0.health)
