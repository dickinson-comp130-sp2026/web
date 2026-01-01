# This file demonstrates three common patterns for processing lists: reduce, map, filter.
# See textbook section 10.7.

###############################################################################
# 1. REDUCE pattern
#    Combine all elements of a list into a single output.
###############################################################################

def sum_of_squares(numbers):
    """Given a list of numbers, return the sum of the squares of those numbers.
    Example: [3, 5, 2] returns 38, which is 3*3 + 5*5 + 2*2"""
    total = 0
    for n in numbers:
        total += n * n
    return total

###############################################################################
# 2. MAP pattern
#    Create a new list that transforms each element of the old list in a certain way.
###############################################################################

def square_each_element(numbers):
    """Given a list of numbers, return a new list consisting of the same numbers
    squared. Example: [3, 5, 2] returns [9, 25, 4]"""
    result = []
    for n in numbers:
        result.append(n * n)
    return result


###############################################################################
# 3. FILTER pattern
#    Create a new list that contains only certain elements from the old list.
###############################################################################

def extract_multiples(numbers, m):
    """Given a list of integers, return a new list consisting only of the
    list elements which are multiples of the parameter m."""
    result = []
    for n in numbers:
        if n % m == 0:
            result.append(n)
    return result


###############################################################################
# Tests for the above functions.
###############################################################################

def test_sum_of_squares():
    assert sum_of_squares([3, 5, 2]) == 38
    assert sum_of_squares([]) == 0
    assert sum_of_squares([-4]) == 16
    assert sum_of_squares([2, 2, 2, 2, 2]) == 20
    print('test_sum_of_squares succeeded')


def test_square_each_element():
    assert square_each_element([3, 5, 2]) == [9, 25, 4]
    assert square_each_element([]) == []
    assert square_each_element([-4]) == [16]
    assert square_each_element([2, 2, 2, 2, 2]) == [4, 4, 4, 4, 4]
    print('test_square_each_element succeeded')


def test_extract_multiples():
    assert extract_multiples([5, 10, 15, 60, 25, 50], 10) == [10, 60, 50]
    assert extract_multiples([5, 10, 15, 60, 25, 50], 5) == [5, 10, 15, 60, 25, 50]
    assert extract_multiples([5, 10, 15, 60, 25, 50], 7) == []
    assert extract_multiples([], 7) == []
    print('test_extract_multiples succeeded')


###############################################################################
# Top-level code
###############################################################################

# test_sum_of_squares()
# test_square_each_element()
# test_extract_multiples()
