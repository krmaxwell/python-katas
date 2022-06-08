import unittest

from saddlepoint import saddlepoint as sp


class TestSaddlepoint(unittest.TestCase):
    def setUp(self) -> None:

        self.array_without_sp = [
            [1, 2, 3, 4, 5],
            [2, 3, 4, 5, 1],
            [3, 4, 5, 1, 2],
            [4, 5, 1, 2, 3],
            [5, 1, 2, 3, 4],
        ]

        self.array_with_single_saddlepoint = [
            [5, 5, 5, 5, 5],
            [1, 3, 1, 1, 1],
            [5, 5, 5, 5, 5],
            [1, 5, 5, 5, 5],
            [5, 5, 5, 5, 5],
        ]

        self.array_with_two_saddlepoints = [
            [5, 5, 5, 5, 5],
            [1, 0, 0, 0, 0],
            [5, 5, 5, 5, 5],
            [1, 0, 0, 0, 0],
            [5, 5, 5, 5, 5],
        ]

        self.array_small = [[1, 3, 1], [1, 2, 1], [1, 3, 1]]

    def test_get_column(self):
        self.assertListEqual([1, 1, 1], sp.get_column(self.array_small, 0))
        self.assertListEqual([3, 4, 5, 1, 2], sp.get_column(self.array_without_sp, 2))

    def test_saddlepoint(self):
        self.assertListEqual([(1, 1)], sp.find_saddlepoints(self.array_small))
        self.assertListEqual(
            [(1, 1)], sp.find_saddlepoints(self.array_with_single_saddlepoint)
        )
        self.assertListEqual(
            [
                (1, 0),
                (3, 0),
            ],
            sp.find_saddlepoints(self.array_with_two_saddlepoints),
        )
        self.assertListEqual([], sp.find_saddlepoints(self.array_without_sp))
