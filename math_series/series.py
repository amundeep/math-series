def fibonacci(n):
    """Returns the nth value of the Fibonacci series - recursively."""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

def fibonacci_iter(n):
    """Returns the nth value of the Fibonacci series - iteratively."""
    n2, n1, current = 0, 0, 1
    if n == 0:
        return 0
    for i in range(1, n):
        n2 = n1
        n1 = current
        current = n2 + n1
    return current

def lucas(n):
    """Returns the nth value of the Lucas series - recursively."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)

def sum_series(n, first_val=0, second_val=1):
    """Returns the nth value of a series with the specified values - recursively.
    Parameters:
        - first_val: the value returned when n = 0
        - second_val: the value returned when n = 1
    """
    temp_first = first_val
    temp_second = second_val
    if n == 0:
        return first_val
    elif n == 1:
        return second_val
    else:
        return sum_series(n - 2, first_val=temp_first, second_val=temp_second) + sum_series(n - 1, first_val=temp_first, second_val=temp_second)