import unittest

from calcstats.calcstats import Stats


class TestStats(unittest.TestCase):
    def test_stats_min(self):
        # Test the min function from the stats class
        stats = Stats([6, 9, 15, -2, 92, 11])
        self.assertEqual(stats.min(), -2)

    def test_stats_max(self):
        # Test the max function from the stats class
        stats = Stats([6, 9, 15, -2, 92, 11])
        self.assertEqual(stats.max(), 92)

    def test_stats_length(self):
        # Test the length function from the stats class
        stats = Stats([6, 9, 15, -2, 92, 11])
        self.assertEqual(stats.length(), 6)

    def test_stats_mean(self):
        stats = Stats([6, 9, 15, -2, 92, 11])
        self.assertAlmostEqual(stats.mean(), 21.833333333333332)
