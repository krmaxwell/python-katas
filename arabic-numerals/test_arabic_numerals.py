from arabic_numerals import ArabicNumeral
import unittest


class TestArabicNumerals(unittest.TestCase):
    def test_blank_string(self):
        """Verify that ArabicNumeral() returns 0 for an empty string"""
        self.assertEqual(0, ArabicNumeral(""))

    def test_basic_symbols(self):
        """Verify that ArabicNumeral() handles basic Roman symbols I, X, C, and M"""
        self.assertEqual(1, ArabicNumeral("I"))
        self.assertEqual(10, ArabicNumeral("X"))
        self.assertEqual(100, ArabicNumeral("C"))

    def test_auxiliary_symbols(self):
        """Verify that ArabicNumeral() handles auxiliary Roman symbols V, L, and D"""
        self.assertEqual(5, ArabicNumeral("V"))
        self.assertEqual(50, ArabicNumeral("L"))
        self.assertEqual(500, ArabicNumeral("D"))

    def test_invalid_symbols(self):
        """Verify that ArabicNumera() throws an exception for invalid symbols"""
        with self.assertRaises(ValueError):
            ArabicNumeral("K")

    def test_number_following_greater_or_equal_value_is_postfixed(self):
        self.assertEqual(12, ArabicNumeral("XII"))
