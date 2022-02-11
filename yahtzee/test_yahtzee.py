from yahtzee import Yahtzee
import unittest


class TestYahtzee(unittest.TestCase):
    def test_chance_scores_sum_of_all_dice(self):
        self.assertEqual(15, Yahtzee([2, 3, 4, 5, 1]).chance())
        self.assertEqual(16, Yahtzee([3, 3, 4, 5, 1]).chance())
        self.assertEqual(14, Yahtzee([1, 1, 3, 3, 6]).chance())
        self.assertEqual(21, Yahtzee([4, 5, 5, 6, 1]).chance())

    def test_yahtzee_scores_50(self):
        self.assertEqual(50, Yahtzee([4, 4, 4, 4, 4]).yahtzee())
        self.assertEqual(50, Yahtzee([6, 6, 6, 6, 6]).yahtzee())
        self.assertEqual(50, Yahtzee([1, 1, 1, 1, 1]).yahtzee())
        self.assertEqual(0, Yahtzee([6, 6, 6, 6, 3]).yahtzee())
        self.assertEqual(0, Yahtzee([1, 1, 1, 2, 1]).yahtzee())

    def test_ones_sum_of_dice_showing_1(self):
        self.assertEqual(1, Yahtzee([1, 2, 3, 4, 5]).ones())
        self.assertEqual(2, Yahtzee([1, 2, 1, 4, 5]).ones())
        self.assertEqual(0, Yahtzee([6, 2, 2, 4, 5]).ones())
        self.assertEqual(4, Yahtzee([1, 2, 1, 1, 1]).ones())

    def test_twos_sum_of_dice_showing_2(self):
        self.assertEqual(4, Yahtzee([1, 2, 3, 2, 6]).twos())
        self.assertEqual(10, Yahtzee([2, 2, 2, 2, 2]).twos())

    def test_threes_sum_of_dice_showing_3(self):
        self.assertEqual(6, Yahtzee([1, 2, 3, 2, 3]).threes())
        self.assertEqual(12, Yahtzee([2, 3, 3, 3, 3]).threes())

    def test_fours_sum_of_dice_showing_4(self):
        self.assertEqual(12, Yahtzee([4, 4, 4, 5, 5]).fours())
        self.assertEqual(8, Yahtzee([4, 4, 5, 5, 5]).fours())
        self.assertEqual(4, Yahtzee([4, 5, 5, 5, 5]).fours())

    def test_fives_sum_of_dice_showing_5(self):
        self.assertEqual(10, Yahtzee([4, 4, 4, 5, 5]).fives())
        self.assertEqual(15, Yahtzee([4, 4, 5, 5, 5]).fives())
        self.assertEqual(20, Yahtzee([4, 5, 5, 5, 5]).fives())

    def test_sixes_sum_of_dice_showing_6(self):
        self.assertEqual(0, Yahtzee([4, 4, 4, 5, 5]).sixes())
        self.assertEqual(6, Yahtzee([4, 4, 6, 5, 5]).sixes())
        self.assertEqual(18, Yahtzee([6, 5, 6, 6, 5]).sixes())

    def test_one_pair_score_sum_two_highest_matching_dice(self):
        self.assertEqual(6, Yahtzee([3, 4, 3, 5, 6]).score_pair())
        self.assertEqual(10, Yahtzee([5, 3, 3, 3, 5]).score_pair())
        self.assertEqual(12, Yahtzee([5, 3, 6, 6, 5]).score_pair())

    def test_two_pair_sum_of_two_matching_pairs(self):
        self.assertEqual(16, Yahtzee([3, 3, 5, 4, 5]).two_pair())
        self.assertEqual(0, Yahtzee([3, 3, 5, 5, 5]).two_pair())
        self.assertEqual(8, Yahtzee([1, 1, 2, 3, 3]).two_pair())

    def test_three_of_a_kind_sum_of_those_three(self):
        self.assertEqual(9, Yahtzee([3, 3, 3, 4, 5]).three_of_a_kind())
        self.assertEqual(15, Yahtzee([5, 3, 5, 4, 5]).three_of_a_kind())
        self.assertEqual(0, Yahtzee([3, 3, 3, 3, 5]).three_of_a_kind())
        self.assertEqual(0, Yahtzee([3, 3, 4, 5, 6]).three_of_a_kind())

    def test_four_of_a_kind_sum_of_those_four(self):
        self.assertEqual(12, Yahtzee([3, 3, 3, 3, 5]).four_of_a_kind())
        self.assertEqual(20, Yahtzee([5, 5, 5, 4, 5]).four_of_a_kind())
        self.assertEqual(0, Yahtzee([3, 3, 3, 3, 3]).four_of_a_kind())

    def test_small_straight_scores_15(self):
        self.assertEqual(15, Yahtzee([1, 2, 3, 4, 5]).small_straight())
        self.assertEqual(15, Yahtzee([2, 3, 4, 5, 1]).small_straight())
        self.assertEqual(0, Yahtzee([1, 2, 2, 4, 5]).small_straight())

    def test_large_straight_scores_20(self):
        self.assertEqual(20, Yahtzee([6, 2, 3, 4, 5]).large_straight())
        self.assertEqual(20, Yahtzee([2, 3, 4, 5, 6]).large_straight())
        self.assertEqual(0, Yahtzee([1, 2, 2, 4, 5]).large_straight())

    def test_full_house_scores_sum_of_all_dice(self):
        self.assertEqual(18, Yahtzee([6, 2, 2, 2, 6]).full_house())
        self.assertEqual(0, Yahtzee([2, 3, 4, 5, 6]).full_house())
        self.assertEqual(8, Yahtzee([1, 1, 2, 2, 2]).full_house())


if __name__ == "__main__":
    unittest.main()
