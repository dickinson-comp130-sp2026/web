import math


def f(x):
    return 3 * x ** 2 + 4 * x - 5


def solve_f_eq_0(low, high):
    """Use the bisection method to solve the equation f(x)=0. The parameters low and
    high represent the interval that will be searched for a solution. For this to work
    correctly, f(low) and f(high) must have opposite signs. See
    https://en.wikipedia.org/wiki/Bisection_method"""
    eps = 1e-9
    f_low = f(low)
    f_high = f(high)
    # Check for opposite signs
    assert (f_low <= 0 and f_high >= 0) or (f_low >= 0 and f_high <= 0)
    while True:
        mid = (low + high) / 2
        f_mid = f(mid)
        if (f_mid <= 0 and f_low <= 0) or (f_mid >= 0 and f_low >= 0):
            # f_mid and f_low have the same sign, so replace the low estimate with the
            # mid estimate
            low = mid
            f_low = f_mid
        else:
            # f_mid and f_high have the same sign, so replace the high estimate with the
            # mid estimate
            high = mid
            f_high = f_mid
        if high - low < eps:
            return mid


def test_solve_f_eq_0():
    # Calculate the true solution using quadratic formula with a=3, b=4, c=-5
    solution = (-4 + math.sqrt(4 ** 2 - 4 * 3 * (-5))) / (2 * 3)
    # Calculate our estimate of the solution using the bisection method
    calculated = solve_f_eq_0(0, 1)
    eps = 1e-6
    assert abs(solution - calculated) < eps
    print('test_solve_f_eq_0 succeeded')
    print('true solution:', solution)
    print('solution via bisection:', calculated)

test_solve_f_eq_0()