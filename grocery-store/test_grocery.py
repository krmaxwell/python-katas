import unittest

from grocery import GroceryStore


class TestGroceryStore(unittest.TestCase):
    def test_total_value(self):
        grocery = GroceryStore()
        self.assertEqual(0, grocery.total_value())