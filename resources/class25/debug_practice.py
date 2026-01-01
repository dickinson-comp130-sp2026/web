# We will practice various techniques to find and fix
# the bugs. See textbook sections 1.7, 2.9, 3.9, 4.9, 5.12, 6.10.

# This get_price() example comes from HW6. There are some bugs here.
# Reminder from HW6: ages 12 and 65 should get child/senior discount.
# Age 18 gets no discount.
def get_price(age, price):
    assert isinstance(age, int), "Age must be an integer"
    assert age >= 0, "Age cannot be negative"
    if age < 12 or age > 65:
        child_and_senior_price = price * 0.5
        return child_and_senior_price
    elif age > 12 and age < 18:
        student_price = price * 0.75
        return student_price
    elif age > 18 and age < 65:
        return price


def test_get_price():
    assert get_price(8, 10.00) == 5.00
    assert get_price(15, 10.00) == 7.50
    assert get_price(50, 10.00) == 10.00
    print('test_get_price succeeded')


# The next function contains some bugs. We will use a mixture of techniques to find them.
def add_multiples_of_3(a, b):
    """Add up all multiples of three in the range from a to b inclusive,
    and return the resulting sum. Parameters a and b are integers."""
    total = 0
    for i in range(a, b):
        if i % 3 == 1:
            total = total + i
    return total

def test_add_multiples_of_3():
    pass
    # Writing good tests is part of good debugging practice.
    # Maybe we need to write some good tests here to help our debugging?

# test_get_price()
# print(get_price(12, 10.00))