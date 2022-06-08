import unittest

from parens.parens import balance_check


class TestParens(unittest.TestCase):
    def test_simple_pairs(self):
        assert balance_check("()") is True
        assert balance_check("{}") is True
        assert balance_check("[]") is True

    def test_single_symbols(self):
        assert balance_check("(") is False
        assert balance_check(")") is False
        assert balance_check("{") is False
        assert balance_check("}") is False
        assert balance_check("[") is False
        assert balance_check("]") is False

    def test_balanced_pairs(self):
        assert balance_check("{{}}") is True
        assert balance_check("{}{}") is True
        assert balance_check("(())") is True
        assert balance_check("()()") is True
        assert balance_check("[[]]") is True
        assert balance_check("[][]") is True

    def test_unbalanced_symbols(self):
        assert balance_check("()(") is False
        assert balance_check("(()") is False
        assert balance_check("((()") is False
        assert balance_check(")()") is False
        assert balance_check(")(") is False
        assert balance_check("{}}") is False
        assert balance_check("}}") is False
        assert balance_check("][") is False
        assert balance_check("[[[][]") is False

    def test_mixed_balanced_pairs(self):
        assert balance_check("(){}") is True
        assert balance_check("({})") is True
        assert balance_check("()[{}]") is True

    def test_mixed_unbalanced_pairs(self):
        assert balance_check("(}{)") is False
        assert balance_check("[]([)[") is False
        assert balance_check("[{)]") is False

    def test_readme_cases(self):
        assert balance_check("{{)(}}") is False
        assert balance_check("({)}") is False
        assert balance_check("[({})]") is True
        assert balance_check("{}([])") is True
        assert balance_check("{()}[[{}]]") is True
