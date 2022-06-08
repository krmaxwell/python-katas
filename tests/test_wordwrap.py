import unittest

from word_wrap.wordwrap import wrap


class TestWordWrap(unittest.TestCase):
    def test_wrap_empty_line(self):
        assert wrap("", 100) == ""


    def test_wrap_single_line(self):
        assert wrap("One line", 80) == "One line"


    def test_wrap_two_lines(self):
        assert wrap("Two lines", 5) == "Two\nlines"


    def test_wrap_longer_line(self):
        assert wrap("Still two lines", 12) == "Still two\nlines"
