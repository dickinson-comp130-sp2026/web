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
        students = enrollments[course]
        if id in students:
            print(course)

def has_overlap(enrollments, course1, course2):
    """Return True if, according to data in the enrollments 
    dictionary, there is at least one student enrolled in both 
    course1 and course2. Otherwise return False."""
    students1 = enrollments[course1]
    students2 = enrollments[course2]
    if students1 is None or students2 is None:
        return False
    for id1 in students1:
        for id2 in students2:
            if id1 == id2:
                return True
    return False