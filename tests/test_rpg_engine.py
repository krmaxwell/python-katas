import unittest

from rpg_inc.engine import Player, RPGEngine


class TestRPGEngine(unittest.TestCase):
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
        combat_rpg_file = """
        'Mark the Fister', 4, 8, 'Iron Fist', 4
        'John the Bagger', 1, 7, 'Small Bag', 1
        """
        engine.process_combat_rpg_file(combat_rpg_file)
        self.assertEqual(2, engine.num_players)