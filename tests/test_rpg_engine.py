import unittest

from rpg_inc.engine import RPGEngine


class TestRPGEngine(unittest.TestCase):
    def test_init(self):
        engine = RPGEngine()
        self.assertIsInstance(engine, RPGEngine)

    def test_add_players(self):
        engine = RPGEngine()
        self.assertEqual(0, engine.num_players)
        engine.add_player('player1')
        self.assertEqual(1, engine.num_players)
        self.assertIn('player1', engine.get_players())