# challenge 1: write this method
def replace_courses(s):
    """In string s, replace all occurrences of DATA180 with COMP180,
    replace all occurrences of DATA200 with COMP200, and return the result."""
    pass


def test_replace_courses():
    s = """MATH170 is a prerequisite for DATA180. After taking
    DATA180, you can continue into DATA200, then DATA300."""
    t = """MATH170 is a prerequisite for COMP180. After taking
    COMP180, you can continue into COMP200, then DATA300."""
    assert replace_courses(s) == t
    print("test_replace_courses succeeded")

# challenge 2: write this method
def replace_Dickinson(s):
    """Replace only the first occurrence of 'Dickinson' with 'Red Devils',
    in the string s, and return the result."""
    pass


def test_replace_Dickinson():
    s = 'Come on Dickinson! Dickinson College was founded in 1773'
    t = 'Come on Red Devils! Dickinson College was founded in 1773'
    assert replace_Dickinson(s) == t
    print("test_replace_Dickinson succeeded")


# challenge 3: Write the following method. This is a much more difficult challenge,
# but it can be completed using only the knowledge we have covered so far in the course.
def check_comp_courses(s):
    """Return True if every occurrence of the substring 'COMP' in s is followed by 3 digits,
    as in COMP130 or COMP332. Otherwise, return False."""
    pass


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
    print("test_check_comp_courses succeeded")


