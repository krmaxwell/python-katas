from parens import balance_check


def test_simple_pairs():
    assert balance_check("()") is True
    assert balance_check("{}") is True
    assert balance_check("[]") is True


def test_single_symbols():
    assert balance_check("(") is False
    assert balance_check(")") is False
    assert balance_check("{") is False
    assert balance_check("}") is False
    assert balance_check("[") is False
    assert balance_check("]") is False


def test_balanced_pairs():
    assert balance_check("{{}}") is True
    assert balance_check("{}{}") is True
    assert balance_check("(())") is True
    assert balance_check("()()") is True
    assert balance_check("[[]]") is True
    assert balance_check("[][]") is True


def test_unbalanced_symbols():
    assert balance_check("()(") is False
    assert balance_check("(()") is False
    assert balance_check("((()") is False
    assert balance_check(")()") is False
    assert balance_check(")(") is False
    assert balance_check("{}}") is False
    assert balance_check("}}") is False
    assert balance_check("][") is False
    assert balance_check("[[[][]") is False


def test_mixed_balanced_pairs():
    assert balance_check("(){}") is True
    assert balance_check("({})") is True
    assert balance_check("()[{}]") is True


def test_mixed_unbalanced_pairs():
    assert balance_check("(}{)") is False
    assert balance_check("[]([)[") is False
    assert balance_check("[{)]") is False


def test_readme_cases():
    assert balance_check("{{)(}}") is False
    assert balance_check("({)}") is False
    assert balance_check("[({})]") is True
    assert balance_check("{}([])") is True
    assert balance_check("{()}[[{}]]") is True
