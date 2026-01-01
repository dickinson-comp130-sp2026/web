# challenge 1: Without running the program, figure out
# the value of each variable in the following function
def index_practice():
    chant = 'swim fast, Dickinson'

    a = chant[1]
    b = chant[0]
    c = chant[6]
    d = len(chant)
    e = chant[19]
    f = chant[-1]
    g = chant[-2]
    h = chant[c]  # runtime error -- deliberate mistake
    i = chant[c - 1]


# challenge 2: Same again – figure out the value of these variables
def slice_practice():
    title = 'ForWhomTheBellTolls'

    a = title[3:7]
    b = title[:7]
    c = title[7:]
    d = title[3:-5]
    e = title[:-5]

    # challenge 3: write code that stores 'Bell' in variable f using a string slice
    f = title[10:14]


# challenge 4: What does the following function do?
# Answer:  It prints every second letter of the string ask, starting with the first
# letter. Example: when the input is 'abcde', the output is 'a', 'c', 'e' printed on
# separate lines.
def iteration_practice(s):
    for i in range(len(s)):
        if i % 2 == 0:
            print(s[i])


# challenge 5: Write a function that returns the number of
# occurrences of the letter 'x' in a given string s.
def count_x(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'x':
            count = count + 1
    return count


# An easier solution to challenge 5 uses iteration over the characters in a string...
def count_x2(s):
    count = 0
    for c in s:
        if c == 'x':
            count = count + 1
    return count


# challenge 6: Write a function that returns the number of
# vowels in a given string s. Hint: use the `in` operator.
# Another hint: see count_upper_case() in the study guide.
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for c in s:
        if c in vowels:
            count = count + 1
    return count


def test_count_x():
    assert count_x('') == 0
    assert count_x('x') == 1
    assert count_x('xx') == 2
    assert count_x('abc') == 0
    assert count_x('axbxc') == 2
    assert count_x('aaxxxbx') == 4
    assert count_x('xaaxxxbx') == 5
    print('test_count_x succeeded')


def test_count_vowels():
    assert count_vowels('') == 0
    assert count_vowels('e') == 1
    assert count_vowels('U') == 1
    assert count_vowels('qwertyuiop') == 4
    assert count_vowels('abbbbe') == 2
    assert count_vowels('ABBBBE') == 2
    print('test_count_vowels succeeded')
