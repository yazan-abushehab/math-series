import pytest

from series.series import fibonacci
from series.series import lucas
from series.series import sum_series


def test_fibonacci_one():
    actual=fibonacci(1)
    expected=1
    assert actual == expected
def test_fibonacci_two():
    actual=fibonacci(0)
    expected=0
    assert actual == expected
def test_fibonacci_three():
    actual=fibonacci(2)
    expected=1
    assert actual == expected
def test_fibonacci_four():
    actual=fibonacci(3)
    expected=2
    assert actual == expected
def test_fibonacci_five():
    actual=fibonacci(4)
    expected=3
    assert actual == expected
def test_fibonacci_six():
    actual=fibonacci(5)
    expected=5
    assert actual == expected
def test_fibonacci_seven():
    actual=fibonacci(6)
    expected=8
    assert actual == expected
def test_fibonacci_eight():
    actual=fibonacci(7)
    expected=13
    assert actual == expected




def test_lucas_one():
    actual=lucas(1)
    expected=1
    assert actual == expected
def test_lucas_two():
    actual=lucas(0)
    expected=2
    assert actual == expected
def test_lucas_three():
    actual=lucas(2)
    expected=3
    assert actual == expected
def test_lucas_four():
    actual=lucas(3)
    expected=4
    assert actual == expected
def test_lucas_five():
    actual=lucas(4)
    expected=7
    assert actual == expected
def test_lucas_six():
    actual=lucas(5)
    expected=11
    assert actual == expected
def test_lucas_seven():
    actual=lucas(6)
    expected=18
    assert actual == expected
def test_lucas_eight():
    actual=lucas(7)
    expected=29
    assert actual == expected


 
def test_sum_series():
    actual=sum_series(2,3,4)
    expected=7
    assert actual == expected
def test_sum_series_1():
    actual=sum_series(5,1,4)
    expected=23
    assert actual == expected
def test_sum_series_2():
    actual=sum_series(5)
    expected=5
    assert actual == expected
def test_sum_series_2():
    actual=sum_series(5,2,1)
    expected=11
    assert actual == expected