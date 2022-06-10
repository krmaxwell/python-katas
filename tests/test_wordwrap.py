import unittest

from word_wrap.wordwrap import wrap


class TestWordWrap(unittest.TestCase):
    def test_wrap_empty_line(self):
        self.assertEqual("", wrap("", 100))


    def test_wrap_single_line(self):
        self.assertEqual("One line", wrap("One line", 80))


    def test_wrap_two_lines(self):
        self.assertEqual("Two\nlines", wrap("Two lines", 5))


    def test_wrap_longer_line(self):
        self.assertEqual("Still two\nlines", wrap("Still two lines", 12))

    def test_long_word(self):
        self.assertEqual("Pyth\non", wrap("Python", 4))