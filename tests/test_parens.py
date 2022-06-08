import unittest

from parens.parens import balance_check


class TestParens(unittest.TestCase):
    def test_simple_pairs(self):
        self.assertTrue(balance_check("()"))
        self.assertTrue(balance_check("{}"))
        self.assertTrue(balance_check("[]"))

    def test_single_symbols(self):
        self.assertFalse(balance_check("("))
        self.assertFalse(balance_check(")"))
        self.assertFalse(balance_check("{"))
        self.assertFalse(balance_check("}"))
        self.assertFalse(balance_check("["))
        self.assertFalse(balance_check("]"))

    def test_balanced_pairs(self):
        self.assertTrue(balance_check("{{}}"))
        self.assertTrue(balance_check("{}{}"))
        self.assertTrue(balance_check("(())"))
        self.assertTrue(balance_check("()()"))
        self.assertTrue(balance_check("[[]]"))
        self.assertTrue(balance_check("[][]"))

    def test_unbalanced_symbols(self):
        self.assertFalse(balance_check("()("))
        self.assertFalse(balance_check("(()"))
        self.assertFalse(balance_check("((()"))
        self.assertFalse(balance_check(")()"))
        self.assertFalse(balance_check(")("))
        self.assertFalse(balance_check("{}}"))
        self.assertFalse(balance_check("}}"))
        self.assertFalse(balance_check("]["))
        self.assertFalse(balance_check("[[[][]"))

    def test_mixed_balanced_pairs(self):
        self.assertTrue(balance_check("(){}"))
        self.assertTrue(balance_check("({})"))
        self.assertTrue(balance_check("()[{}]"))

    def test_mixed_unbalanced_pairs(self):
        self.assertFalse(balance_check("(}{)"))
        self.assertFalse(balance_check("[]([)["))
        self.assertFalse(balance_check("[{)]"))

    def test_readme_cases(self):
        self.assertFalse(balance_check("{{)(}}"))
        self.assertFalse(balance_check("({)}"))
        self.assertTrue(balance_check("[({})]"))
        self.assertTrue(balance_check("{}([])"))
        self.assertTrue(balance_check("{()}[[{}]]"))
