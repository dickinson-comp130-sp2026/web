def create_enrollments_dict():
    # In this dictionary, the key is a course code and 
    # the value is a list of student IDS enrolled in that course.
    enrollments = {'COMP130': [634, 772, 881], 
                   'COMP232': [772, 991], 
                   'COMP356': [634, 881, 939], 
                   'COMP190': [634, 772, 861, 902]}
    return enrollments



def print_courses(enrollments, id):
    """Print all courses in the given enrollments dictionary 
    taken by the student with the given id number"""
    for course in enrollments:
        students = ____________
        if _________________:
            print(course)

def has_overlap(enrollments, course1, course2):
    """Return True if, according to data in the enrollments 
    dictionary, there is at least one student enrolled in both 
    course1 and course2. Otherwise return False."""
    students1 = enrollments[__________]
    students2 = ________________________
    if students1 is None or students2 is None:
        return False
    for id1 in ___________:
        for ____________________:
            if ___________:
                return True
    return False