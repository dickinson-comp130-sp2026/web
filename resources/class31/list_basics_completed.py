# challenge 1: what is the output?
def print_some_list_items():
    t1 = ['a', 'b', 'c', 'd', 'e']
    t2 = [5, 10, 15, 20]
    t3 = ['apple', 6, 'banana', 5]
    t4 = [47]
    t5 = []

    print('t1[0], t1[3], t1[-2]:', t1[0], t1[3], t1[-2])
    print('t2[0] + t2[3]:', t2[0] + t2[3])
    print('t3[2:]:', t3[2:])
    print('t4[0]:', t4[0])
    print('t4:', t4)
    print('t5:', t5)

    t2[2] = 35
    print('t2:', t2)

    t1[2:4] = ['x', 'y']
    print('t1:', t1)


# challenge 2: what is the output?
def print_nested_list_items():
    t = [10, 20, [25, 26], 30, [], 40, [45, 46, 47, 48], 50]
    print('t[0]:', t[0])
    print('t[2]:', t[2])
    print('t[2][1]:', t[2][1])
    print('len(t):', len(t))
    print('len(t[2]):', len(t[2]))
    print('len(t[4]):', len(t[4]))
    print('t[6][1:]:', t[6][1:])
    print('t.index(30):', t.index(30))


# challenge 3: what is the output?
def do_list_operations_and_methods():
    t1 = [2, 4]
    t2 = [1, 3, 5]

    print('t1*3:', t1 * 3)
    print('t1+t2:', t1 + t2)
    print('t1[:]', t1[:])

    t1.append(6)
    print('t1:', t1)

    t2.extend([7, 9])
    print('t2:', t2)

    t3 = t2 + t1
    print('t3[5]:', t3[5])
    t3.sort()
    print('t3:', t3)


# challenge 4: write this method.
def print_even_numbers(t):
    """t is a list of integers. This method prints the elements of t that are even."""
    for n in t:
        if n % 2 == 0:
            print(n)


# challenge 5: write this method.
def add_10_to_each(t):
    """t is a list of integers. This method adds 10 to each element of t."""
    for i in range(len(t)):
        t[i] = t[i] + 10
