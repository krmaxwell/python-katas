import unittest

from grocery_store.grocery import ROS


class TestROS(unittest.TestCase):
    def setUp(self) -> None:
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

    def test_items_are_added(self):
        ros = ROS()
        self.assertEqual(len(ros.items), 0)
        ros.add_item("bread", 1, 2)
        self.assertEqual(len(ros.items), 1)
        ros.add_item("12-pack of eggs", 1, 2)
        ros.add_item("milk (1L)", 4, 8)
        self.assertEqual(len(ros.items), 3)

    def test_grand_total_income(self):
        ros = ROS()
        self.assertEqual(ros.total_income, 0)
        ros.add_item("bread", 1, 2)
        self.assertEqual(ros.total_income, 2)
        ros.add_item("12-pack of eggs", 1, 2)
        ros.add_item("milk (1L)", 4, 8)
        self.assertEqual(ros.total_income, 12)

        # full_ros = ROS()
        # full_ros.process_ros_file(self.ros_data)

    def test_create_categories(self):
        ros = ROS()
        self.assertEqual(len(ros.categories), 0)
        ros.add_category("bread", "wheat and pasta")
        self.assertEqual(len(ros.categories), 1)

        ros.add_category("eggs", "animal")
        ros.add_category("milk", "dairy")
        self.assertEqual(len(ros.categories), 3)
