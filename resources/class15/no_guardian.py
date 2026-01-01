def course_uses_math(course_code):
    if course_code.startswith('MATH') or course_code.startswith('COMP') or course_code.startswith('DATA'):
        print(course_code, 'uses math')
    elif course_code == 'ECON298':
        print('Econometrics requires mathematical knowledge')
    elif course_code == 'INBM220':
        print('Managerial decision-making requires some math')
    else:
        print(course_code, 'doesn\'t use much math')


def print_course_code(subject, number):
    course_code = subject.upper() + str(number)
    print('Course code is', course_code)


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


