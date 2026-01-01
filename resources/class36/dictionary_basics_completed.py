def create_dictionary_v1():
    """Create and return a dictionary that stores enrollment data for Dickinson
    courses. In each key-value pair, the key is a course code such as 'COMP130'. The
    corresponding value is the number of students currently enrolled. Here is the data
    we would like to store: COMP130 23, COMP232 18, COMP356 21, COMP190 15.
    """
    enrollments = dict()
    enrollments['COMP130'] = 23
    enrollments['COMP232'] = 18
    # challenge 1: add the remaining data to the dictionary
    enrollments['COMP356'] = 21
    enrollments['COMP190'] = 15
    return enrollments


def create_dictionary_v2():
    """Achieve exactly the same thing as the previous function, but use the notation
    for initializing dictionaries with data."""

    # challenge 2: Edit the following line so that the dictionary is initialized with
    # all desired data.
    enrollments = {'COMP130': 23, 'COMP232': 18, 'COMP356': 21, 'COMP190': 15}
    return enrollments


def print_enrollment(course):
    """Print a message stating the number of students enrolled in the given course."""
    enrollments = create_dictionary_v1()
    # challenge 3: Complete the following line of code.
    num_enrolled = enrollments[course]
    print('There are', num_enrolled, 'students enrolled in', course)


def is_known(course):
    """Return True if the enrollment of the given course is known, and False otherwise."""
    enrollments = create_dictionary_v1()
    # challenge 4: Complete the following line of code.
    if course in enrollments:
        return True
    else:
        return False


def max_enrollment():
    """Return the highest enrollment."""
    enrollments = create_dictionary_v1()
    # challenge 5: Complete the following line of code.
    return max(enrollments.values())
