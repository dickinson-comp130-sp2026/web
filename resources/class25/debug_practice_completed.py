# We will practice various techniques to find and fix
# the bugs. See textbook sections 1.7, 2.9, 3.9, 4.9, 5.12, 6.10.

# This get_price() example comes from HW6. There are some bugs here.
# Reminder from HW6: ages 12 and 65 should get child/senior discount.
# Age 18 gets no discount.
#
# ... In class we demonstrated a syntax error a runtime error and a semantic error in this code.
#  We did not spend time fixing the bugs in the code, but the updated code below does fix these bugs.
#
def get_price(age, price):
    assert isinstance(age, int), "Age must be an integer"
    assert age >= 0, "Age cannot be negative"
    assert isinstance(price, float) or isinstance(price, int), \
           'Price must be a float or int'
    assert price >= 0, 'Price must be non-negative'
    if age <= 12 or age >= 65:
        child_and_senior_price = price * 0.5
        return child_and_senior_price
    if 12 < age < 18:
        student_price = price * 0.75
        return student_price
    # must have 18 <= age < 65:
    return price

## We've also added a few extra tests here check on the boundary cases.
def test_get_price():
    assert get_price(0, 10.00) == 5.00
    assert get_price(8, 10.00) == 5.00
    assert get_price(12, 10.00) == 5.00
    assert get_price(15, 10.00) == 7.50
    assert get_price(18, 10.00) == 10.00
    assert get_price(50, 10.00) == 10.00
    assert get_price(65, 10.00) == 5.00
    assert get_price(80, 10.00) == 5.00
    print('test_get_price succeeded')


# The next function contains some bugs. We will use a mixture of techniques to find them.

## ... In class we learned how to add print statements to employ print debugging. These are shown below.
## It's not necessary to use the f-string formatting technique. 
def add_multiples_of_3(a, b):
    """Add up all multiples of three in the range from a to b inclusive,
    and return the resulting sum. Parameters a and b are integers."""
    total = 0
    print(f"a = {a}, b = {b}")
    for i in range(a, b+1):
        print(f"before if statement: i = {i}")
        if i % 3 == 0:
            print(f"inside if statement: i = {i}")
            total = total + i
            print(f"new total is {total}")
        else:
            print("skipped if statement")
    return total

def test_add_multiples_of_3():
    assert add_multiples_of_3(0, 0) == 0
    assert add_multiples_of_3(3,12) == 30
    assert add_multiples_of_3(3,15) == 45
    assert add_multiples_of_3(3,4) == 3
    assert add_multiples_of_3(2,4) == 3
    assert add_multiples_of_3(2,6) == 9
    print('test_add_multiples_of_3 succeeded')
    
test_get_price()
# print(get_price(12, 10.00))

test_add_multiples_of_3()

