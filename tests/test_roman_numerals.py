import unittest

from roman_numerals.roman_numerals import RomanNumeral


class TestRomanNumerals(unittest.TestCase):
    def test_single_digit(self):
        assert str(RomanNumeral(1)) == "I"
        assert str(RomanNumeral(2)) == "II"
        assert str(RomanNumeral(3)) == "III"
        assert str(RomanNumeral(4)) == "IV"
        assert str(RomanNumeral(5)) == "V"
        assert str(RomanNumeral(6)) == "VI"
        assert str(RomanNumeral(7)) == "VII"
        assert str(RomanNumeral(8)) == "VIII"
        assert str(RomanNumeral(9)) == "IX"

    def test_double_digits(self):
        assert str(RomanNumeral(47)) == "XLVII"
        assert str(RomanNumeral(99)) == "XCIX"

    def test_triple_digits(self):
        assert str(RomanNumeral(666)) == "DCLXVI"

    def test_quadruple_digits(self):
        assert str(RomanNumeral(1990)) == "MCMXC"
        assert str(RomanNumeral(2008)) == "MMVIII"

    """
    def test_non_int()"
        RomanNumeral("666") should throw a TypeError
    """
