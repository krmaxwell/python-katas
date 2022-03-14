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
        """Verify that ArabicNumeral() throws an exception for invalid symbols"""
        with self.assertRaises(ValueError):
            ArabicNumeral("K")

    def test_number_following_greater_or_equal_value_is_postfixed(self):
        """Verify that ArabicNumeral() handles numbers following greater-or-equal values"""
        self.assertEqual(2, ArabicNumeral("II"))
        self.assertEqual(11, ArabicNumeral("XI"))
        self.assertEqual(12, ArabicNumeral("XII"))
        self.assertEqual(13, ArabicNumeral("XIII"))
        self.assertEqual(110, ArabicNumeral("CX"))
        self.assertEqual(111, ArabicNumeral("CXI"))
        self.assertEqual(120, ArabicNumeral("CXX"))

    def test_number_preceded_by_less_or_equal_value_is_prefixed(self):
        """Verify that ArabicNumeral() handles numbers preceded by less-or-equal values"""
        self.assertEqual(4, ArabicNumeral("IV"))
        self.assertEqual(14, ArabicNumeral("XIV"))
        self.assertEqual(40, ArabicNumeral("XL"))
        self.assertEqual(90, ArabicNumeral("XC"))

    def test_cant_subtract_auxiliary_symbols(self):
        """Verify that ArabicNumeral() throws an exception for auxiliary symbols"""
        with self.assertRaises(ValueError):
            ArabicNumeral("VL")
        with self.assertRaises(ValueError):
            ArabicNumeral("LM")

    def test_cant_pass_non_string(self):
        """Verify that ArabicNumeral() throws an exception for non-strings"""
        with self.assertRaises(TypeError):
            ArabicNumeral(1)
        with self.assertRaises(TypeError):
            ArabicNumeral(1.0)
        with self.assertRaises(TypeError):
            ArabicNumeral(True)
        with self.assertRaises(TypeError):
            ArabicNumeral(None)
        with self.assertRaises(TypeError):
            ArabicNumeral([])
        with self.assertRaises(TypeError):
            ArabicNumeral({})
        with self.assertRaises(TypeError):
            ArabicNumeral(())
