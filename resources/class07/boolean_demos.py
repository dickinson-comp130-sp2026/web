# Print yes if x is a multiple of 5 and not a multiple of 7. Otherwise print no.
def boolean_expr_demo1(x):
    if x % 5 == 0 and not x % 7 == 0:
        print('yes')
    else:
        print('no')


# Print yes if x is bigger than 50 or smaller than 30 or equal to 40.
# Otherwise print no.
def boolean_expr_demo2(x):
    if x > 50 or x < 30 or x == 40:
        print('yes')
    else:
        print('no')


# Print yes if x is not equal to any of these numbers: 3, 12, 25, 31.
# Otherwise print no.
def boolean_expr_demo3(x):
    if x != 3 and x != 12 and x != 25 and x != 31:
        print('yes')
    else:
        print('no')

# As above -- different approach
def boolean_expr_demo3b(x):
    if not (x == 3 or x == 12 or x == 25 or x == 31):
        print('yes')
    else:
        print('no')

# boolean_expr_demo1(35)
# boolean_expr_demo2(40)
# boolean_expr_demo3(31)
# boolean_expr_demo3b(31)

