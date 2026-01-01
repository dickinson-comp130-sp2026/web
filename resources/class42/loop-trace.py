# What is the output of the following Python code?
z = 'pqrst'
a = -10
for i in range(len(z)):
    if a > 10 and i>=1:
        print(z[i], z[i-1])
    a = -2 * a
    j = i
    while j >= 0:
        print(j, end=', ')
        j -= 1
    print()
