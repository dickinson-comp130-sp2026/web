def add5(x):
    y = x + 5
    print(x, 'plus 5 is', y)
    mult_by3(y)
    print('end of add5 function')


def mult_by3(m):
    n = 3 * m
    print(m, 'times 3 is', n)
    sub7(n)
    print('end of mult_by3 function')

def sub7(w):
    v = w - 7
    print(w, 'minus 7 is', v)
    print('end of sub7 function')


z = 10
add5(z)
print('end of main program')
