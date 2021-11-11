import saddlepoint as sp

array_without_sp = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 1],
    [3, 4, 5, 1, 2],
    [4, 5, 1, 2, 3],
    [5, 1, 2, 3, 4],
]

array_with_sp = [
    [5, 5, 5, 5, 5],
    [1, 3, 1, 1, 1],
    [5, 5, 5, 5, 5],
    [1, 5, 5, 5, 5],
    [5, 5, 5, 5, 5],
]

array_small = [[1, 3, 1], [1, 2, 1], [1, 3, 1]]


def test_get_column():
    assert sp.get_column(array_small, 0) == [1, 1, 1]


def test_saddlepoint():
    assert sp.sp(array_small) == (1, 1)
