from calcstats import Stats


def test_stats_min():
    # Test the min function from the stats class
    stats = Stats([6, 9, 15, -2, 92, 11])
    assert stats.min() == -2


def test_stats_max():
    # Test the max function from the stats class
    stats = Stats([6, 9, 15, -2, 92, 11])
    assert stats.max() == 92


def test_stats_length():
    # Test the length function from the stats class
    stats = Stats([6, 9, 15, -2, 92, 11])
    assert stats.length() == 6


def test_stats_mean():
    stats = Stats([6, 9, 15, -2, 92, 11])
    assert (
        stats.mean() == 21.833333333333332
    )  # TODO: implement float equality testing (epsilon / delta)
