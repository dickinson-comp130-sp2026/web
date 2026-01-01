def create_enrollments_dict():
    enrollments = {'COMP130': 23, 'COMP232': 18, 'COMP356': 21, 'COMP190': 15}
    return enrollments


def print_all(d):
    """Print all key-value pairs in a dictionary. The argument d is the dictionary to print."""
    for ______:
        v = ______
        print(f'key {k}, value {v}')


def print_with_threshold(d, min_val):
    """Print some of the key-value pairs in the dictionary d. Only pairs whose
    value is at least min_val are printed."""
    pass


def set_all_to_zero(d):
    """
    Sets all values in a dictionary to 0, modifying the dictionary in place.
    The argument d is the dictionary whose values will be set to 0.
    """
    pass


def reverse_lookup(d, target_val):
    """Print a key corresponding to the value target_val if one exists in the dictionary d and otherwise print 'not found'"""
    for k in d:
        v = d[k]
        if ___________:
            print(____)
            return
    print(__________)