# This file follows the textbook section 9.9, 9.10, and 9.11 closely.

# challenge 1: Draw a state diagram for this function
def compare_strings():
    # STAGE 1
    a = 'banana'
    b = 'banana'
    print('a:', a)
    print('b:', b)
    print('a is b:', a is b)
    print('a == b:', a == b)

    # Pause here and draw state diagram, then show how it updates when the rest of the
    # function executes.

    # STAGE 2
    print('\nRedefining a as "avocado"...')
    a = 'avocado'
    print('a:', a)
    print('b:', b)
    print('a is b:', a is b)
    print('a == b:', a == b)


# challenge 2: Draw a state diagram for this function
def compare_lists():
    # STAGE 1
    a = [1, 2, 3]
    b = [1, 2, 3]
    print('a:', a)
    print('b:', b)
    print('a is b:', a is b)
    print('a == b:', a == b)

    # Pause here and draw state diagram, then show how it updates when the rest of the
    # function executes.

    # STAGE 2
    print('\nRedefining a[1] as 20...')
    a[1] = 20
    print('a:', a)
    print('b:', b)
    print('a is b:', a is b)
    print('a == b:', a == b)


# challenge 3: Understand the fundamental difference between the following two
# functions, and draw state diagrams for compare_mult_by_10() to demonstrate that.

def mult_list_by_10_v1(t):
    for i in range(len(t)):
        t[i] *= 10


def mult_list_by_10_v2(t):
    result = []
    for n in t:
        result.append(n*10)
    return result


def compare_mult_by_10():
    # STAGE 1
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]

    # STAGE 2
    mult_list_by_10_v1(a)

    # STAGE 3
    d = mult_list_by_10_v2(c)

    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('d:', d)
    print('a is b:', a is b)
    print('a == b:', a == b)
    print('a is d:', a is d)
    print('a == d:', a == d)


# compare_strings()
# compare_lists()
# compare_mult_by_10()

