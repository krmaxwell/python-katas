from saddlepoint import saddlepoint as sp

array_without_sp = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 1],
    [3, 4, 5, 1, 2],
    [4, 5, 1, 2, 3],
    [5, 1, 2, 3, 4],
]

array_with_single_saddlepoint = [
    [5, 5, 5, 5, 5],
    [1, 3, 1, 1, 1],
    [5, 5, 5, 5, 5],
    [1, 5, 5, 5, 5],
    [5, 5, 5, 5, 5],
]

array_with_two_saddlepoints = [
    [5, 5, 5, 5, 5],
    [1, 0, 0, 0, 0],
    [5, 5, 5, 5, 5],
    [1, 0, 0, 0, 0],
    [5, 5, 5, 5, 5],
]

array_small = [[1, 3, 1], [1, 2, 1], [1, 3, 1]]


def test_get_column():
    assert sp.get_column(array_small, 0) == [1, 1, 1]
    assert sp.get_column(array_without_sp, 2) == [3, 4, 5, 1, 2]


def test_saddlepoint():
    assert sp.find_saddlepoints(array_small) == [(1, 1)]
    assert sp.find_saddlepoints(array_with_single_saddlepoint) == [(1, 1)]
    assert sp.find_saddlepoints(array_with_two_saddlepoints) == [(1, 0), (3, 0)]
    assert sp.find_saddlepoints(array_without_sp) == []
