from wordwrap import wrap
import pytest


def test_wrap_empty_line():
    assert wrap("", 100) == ""


def test_wrap_single_line():
    assert wrap("One line", 80) == "One line"


def test_wrap_two_lines():
    assert wrap("Two lines", 5) == "Two\nlines"


def test_wrap_longer_line():
    assert wrap("Still two lines", 12) == "Still two\nlines"
