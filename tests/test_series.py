from math_series.series import fibonacci
from math_series.series import fibonacci_iter
from math_series.series import lucas
from math_series.series import sum_series

def test_fibonacci_0():
    assert fibonacci(0) == 0

def test_fibonacci_1():
    assert fibonacci(1) == 1

def test_fibonacci_7():
    assert fibonacci(7) == 13

def test_fibonacci_iter_0():
    assert fibonacci_iter(0) == 0

def test_fibonacci_iter_1():
    assert fibonacci_iter(1) == 1

def test_fibonacci_iter_7():
    assert fibonacci_iter(7) == 13

def test_lucas_0():
    assert lucas(0) == 2

def test_lucas_1():
    assert lucas(1) == 1

def test_lucas_7():
    assert lucas(7) == 29

def test_sum_series_0():
    assert sum_series(0) == 0

def test_sum_series_1():
    assert sum_series(1) == 1

def test_sum_series_7():
    assert sum_series(7) == 13

def test_sum_series_params_2_1_2():
    assert sum_series(2, first_val=2, second_val=1) == 3