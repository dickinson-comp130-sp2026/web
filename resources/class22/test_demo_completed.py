def icecream_cost(num_scoops):
    """Return the cost of an icecream in cents, based on the number of scoops. One scoop
    costs $4.50. Two scoops cost $6. Any other number of scoops is invalid and the
    return value is -1."""
    if num_scoops == 1:
        return 450  # $4.50 in cents
    elif num_scoops == 2:
        return 601  # $6.00 in cents
    else:  # invalid number of scoops
        return -1


def test_icecream_cost():
    assert icecream_cost(1) == 450
    assert icecream_cost(2) == 600
    assert icecream_cost(3) == -1
    assert icecream_cost(-7) == -1
    print('test_icecream_cost succeeded')


def test_icecream_cost2():
    assert icecream_cost(1) == 450, 'failed with single scoop'
    assert icecream_cost(2) == 600, 'failed with two scoops'
    assert icecream_cost(3) == -1, 'failed with three scoops, which should be invalid'
    assert icecream_cost(-7) == -1, 'failed with negative number of scoops'
    print('test_icecream_cost2 succeeded')


def graduation_year(status: str, semester: str, current_year: int):
    """Return the graduation year of a junior or senior student based on the current
    semester and year. The status parameter should be either 'junior' or 'senior'
    (insensitive to case). The semester parameter should be either 'fall' or 'spring'
    (also case-insensitive). Any other values are invalid and the return value is -1."""
    status = status.lower()  # ensures case-insensitive
    semester = semester.lower()  # ensures case-insensitive
    if status != 'senior' and status != 'junior':
        return -1
    if semester != 'fall' and semester != 'spring':
        return -1
    if status == 'senior':
        if semester == 'fall':
            return current_year + 1
        else:
            return current_year
    else:  # status == 'junior'
        if semester == 'fall':
            return current_year + 2
        else:
            return current_year + 1


def test_graduation_year():
    assert graduation_year('senior', 'fall', 2023) == 2024
    assert graduation_year('senior', 'spring', 2019) == 2019
    assert graduation_year('junior', 'fall', 2010) == 2012
    assert graduation_year('junior', 'spring', 2023) == 2024
    assert graduation_year('sophomore', 'spring', 2023) == -1, \
        'sophomore should be invalid'
    assert graduation_year('junior', 'summer', 2023) == -1, \
        'summer should be invalid'
    assert graduation_year('Senior', 'SPRING', 2019) == 2019, \
        'failed with uppercase letters'
    print('test_graduation_year succeeded')


def add_1000_times(increment):
    """Add the given increment 1000 times and return the result."""
    total = 0.0
    for i in range(1000):
        total = total + increment
    return total


def test_add_1000_times():
    eps = 1e-6
    assert abs(add_1000_times(0.1) - 100.0) < eps
    assert abs(add_1000_times(4.567) - 4567) < eps
    print('test_add_1000_times succeeded')


print('add_1000_times(0.1):', add_1000_times(0.1))
print('add_1000_times(4.567):', add_1000_times(4.567))

test_icecream_cost()
test_icecream_cost2()
test_graduation_year()
test_add_1000_times()

