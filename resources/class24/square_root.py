import math


def square_root(a):
    """Return the square root of a, using Newton's method"""
    eps = 1e-8
    x = a / 2  # initial guess for the square root
    while True:
        # compute a more accurate estimate y, using Newton's formula
        y = (x + a / x) / 2
        if abs(y - x) < eps:
            break
        x = y  # update current estimate using new estimate
    return y


def test_square_root():
    eps = 1e-6
    assert abs(math.sqrt(2) - square_root(2)) < eps
    assert abs(math.sqrt(10) - square_root(10)) < eps
    assert abs(math.sqrt(8.331) - square_root(8.331)) < eps
    print('test_square_root succeeded')


test_square_root()
