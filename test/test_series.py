from math_series.series import lucas, sum_series, fibonacci


# 0, 1, 1, 2, 3, 5, 8, 13, 21 ,34 ,55,89,144,233,377,610   fibonacci
# 2, 1, 3, 4, 7, 11, 18, 29, 47,76,123,199,322,521,843,1364    lucas


def test_fibonacci_for_type():
    assert type(fibonacci(3)) is int


def test_fibonacci():
    expected = 3
    actual = fibonacci(4)
    assert actual == expected


def test_fibonacci_two():
    expected = 8
    actual = fibonacci(6)
    assert actual == expected


def test_fibonacci_three():
    assert fibonacci(7) == 13


def test_fibonacci_four():
    expected = 89
    actual = fibonacci(11)
    assert actual == expected


def test_fibonacci_five():
    expected = 610
    actual = fibonacci(15)
    assert actual == expected


def test_lucas():
    expected = 4
    actual = lucas(3)
    assert actual == expected


def test_lucas_two():
    expected = 11
    actual = lucas(5)
    assert actual == expected


def test_lucas_three():
    expected = 29
    actual = lucas(7)
    assert actual == expected


def test_lucas_four():
    expected = 199
    actual = lucas(11)
    assert actual == expected


def test_lucas_five():
    expected = 1364
    actual = lucas(15)
    assert actual == expected


def test_sum_series():
    assert sum_series(2) == 1


def test_sum_series_two():
    expected = 2
    actual = sum_series(3)
    assert actual == expected


def test_sum_series_three():
    expected = 55
    actual = sum_series(10, 0, 1)
    assert actual == expected


def test_sum_series_four():
    expected = 199
    actual = sum_series(11, 2, 1)
    assert actual == expected