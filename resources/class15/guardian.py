def course_uses_math(course_code):
    assert isinstance(course_code, str), 'course code must be a string'
    assert not course_code.isdigit(), 'course code may not be all digits'
    if course_code.startswith('MATH') or course_code.startswith('COMP') or course_code.startswith('DATA'):
        print(course_code, 'uses math')
    elif course_code == 'ECON298':
        print('Econometrics requires mathematical knowledge')
    elif course_code == 'INBM220':
        print('Managerial decision-making requires some math')
    else:
        print(course_code, 'doesn\'t use much math')

def print_course_code(subject, number):
    assert isinstance(subject, str), 'subject must be a string'
    assert isinstance(number, int), 'number must be an integer'
    assert number>=100 and number<600, 'course number outside expected range'
    print('Course code is', subject.upper() + str(number))


course_uses_math('COMP130')
##course_uses_math('MATH171')
##course_uses_math('ECON298')
##course_uses_math('INBM220')
##course_uses_math(130)
##course_uses_math('130')
##
##print_course_code('comp', 130)
##print_course_code(130, 'comp')
##print_course_code('comp', '130')
##print_course_code('comp', 99)

##
