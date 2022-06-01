import unittest

from grocery import GroceryStore


class TestGroceryStore(unittest.TestCase):
    def test_total_value(self):
        grocery = GroceryStore()
        self.assertEqual(0, grocery.total_value())

    def test_value_increases(self):
        grocery = GroceryStore()
        grocery.add_item('bread', 1, 2)
        self.assertEqual(2, grocery.total_value())
        grocery.add_item('12-pack of eggs', 1, 2)
        self.assertEqual(4, grocery.total_value())
        grocery.add_item('milk (1L)', 4, 8)
        self.assertEqual(12, grocery.total_value())

    def test_item_count_increases(self):
        grocery = GroceryStore()
        self.assertEqual(0, grocery.item_count())
        grocery.add_item('bread', 1, 2)
        self.assertEqual(1, grocery.item_count())

    def test_read_ros_file(self):
        grocery = GroceryStore()
        ros_data = """
            bread, 1, 2
            12-pack of eggs, 1, 2
            milk (1L), 4, 8
            coca cola (33cl), 10, 10
            chicken clubs (frozen), 1, 4
            carrots, 4, 1
            apples (red, 1Kg bag), 1, 2
            butter (500 g), 3, 6
            cheese (1Kg), 1, 7
            bacon ("tasty" brand, 3 pack), 2, 7
            orange juice (1L), 2, 3
            cheese (gouda, 1Kg), 1, 5
            bottled water (1.5L), 5, 5
            twixies (1 whole box, 3 rows, 5 per row), 1, 20
            sirloin (100g), 1, 30
            tomatoes, 12, 3
            bananas, 3, 1
        """
        grocery.read_ros_file(ros_data)
        self.assertEqual(116, grocery.total_value())
        self.assertEqual(53, grocery.item_count())
