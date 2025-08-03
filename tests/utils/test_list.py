from utils.list import sorted_nested


def test_sorted_nested() -> None:
    assert sorted_nested([]) == []
    assert sorted_nested([[2], [3], [1]]) == [[1], [2], [3]]
    assert sorted_nested([[3, 2], [3, 2, 1]]) == [[1, 2, 3], [2, 3]]
    # Only 2 deep:
    assert sorted_nested([[[5, 4], [3, 2]]]) == [[[3, 2], [5, 4]]]
