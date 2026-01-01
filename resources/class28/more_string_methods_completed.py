# challenge 1: write this method
def replace_courses(s):
    """In string s, replace all occurrences of DATA180 with COMP180,
    replace all occurrences of DATA200 with COMP200, and return the result."""
    t = s.replace('DATA180', 'COMP180')
    u = t.replace('DATA200', 'COMP200')
    return u;


def test_replace_courses():
    s = """MATH170 is a prerequisite for DATA180. After taking
    DATA180, you can continue into DATA200, then DATA300."""
    t = """MATH170 is a prerequisite for COMP180. After taking
    COMP180, you can continue into COMP200, then DATA300."""
    assert replace_courses(s) == t
    print('test_replace_courses succeeded')


# challenge 2: write this method
def replace_Dickinson(s):
    """Replace only the first occurrence of 'Dickinson' with 'Red Devils',
    in the string s, and return the result."""


def test_replace_Dickinson():
    s = 'Come on Dickinson! Dickinson College was founded in 1773'
    t = 'Come on Red Devils! Dickinson College was founded in 1773'
    assert replace_Dickinson(s) == t


def check_comp_courses(s):
    """Return True if every occurrence of the substring 'COMP' in s is followed
    by 3 digits, as in COMP130 or COMP332. Otherwise, return False."""

    # The target string to search for
    target = 'COMP'
    # The index at which our next search for the target will begin
    start_index = 0
    # The number of digits which are expected to follow an occurrence of the target string
    num_digits_expected = 3
    while True:
        # Find the next occurrence of the target string.
        target_index = s.find(target, start_index)
        # If there are no more occurrences of the target, we can return True because
        # every occurrence found was followed by the expected number of digits.
        if target_index == -1:
            return True
        # Calculate the index for the start and end of the digits (inclusive and
        # exclusive respectively).
        digits_start = target_index + len(target)
        digits_end = digits_start + num_digits_expected
        # If the string s is too short to contain the required number of digits,
        # we can immediately return False.
        if len(s) < digits_end:
            return False
        # Check that the range from digits_start to digit_end consists entirely of digits.
        expected_digits = s[digits_start:digits_end]
        if not expected_digits.isdigit():
            return False
        # Update the start index so that the next search will begin after the
        # previously-found occurrence of the target and its following digits.
        start_index = target_index + len(target) + num_digits_expected


def test_check_comp_courses():
    assert check_comp_courses(
        'You can take COMP130 or COMP132 as your first course in computer science.')
    assert not check_comp_courses(
        'Some courses are cross listed as COMP/DATA, such as COMP200/DATA200')
    assert check_comp_courses('COMP130')
    assert check_comp_courses('COMP130COMP130')
    assert check_comp_courses('COMP130COMP130COMP130')
    assert not check_comp_courses('COMP13')
    assert not check_comp_courses('COMP13COMP130')
    assert not check_comp_courses('COMP130COMP13')
    assert not check_comp_courses('COMP130COMP13COMP130')
    print('test_check_comp_courses succeeded')


test_check_comp_courses()
