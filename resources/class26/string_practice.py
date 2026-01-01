# challenge 1: Without running the program, figure out
# the value of each variable in the following function
def index_practice():
    chant = 'swim fast, Dickinson'

    a = chant[1]
    b = chant[0]
    g = chant[6]
    c = len(chant)
    d = chant[20]
    e = chant[-1]
    f = chant[-2]
    g = chant[c]  # runtime error -- oops
    h = chant[c - 1]


# challenge 2: Same again – figure out the value of these variables
def slice_practice():
    title = 'ForWhomTheBellTolls'

    a = title[3:7]
    b = title[:7]
    c = title[7:]
    d = title[3:-5]
    e = title[:-5]

    # challenge 3: write code that stores 'Bell' in variable f using a string slice
    # f = ____________


# challenge 4: What does the following function do?
def iteration_practice(s):
    for i in range(len(s)):
        if i % 2 == 0:
            print(s[i])


# challenge 5: Write a function that returns the number of
# occurrences of the letter 'x' in a given string s.
def count_x(s):
    pass


# challenge 6: Write a function that returns the number of
# vowels in a given string s. Hint: use the `in` operator.
# Another hint: see count_upper_case() in the study guide.
def count_vowels(s):
    pass




