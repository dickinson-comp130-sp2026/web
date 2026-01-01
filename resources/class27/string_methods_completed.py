def whitespace_demo():
    print('a\tb\tc')
    print('aaa\tbbb\tccc')
    print('aaa\nbbb\nccc')

# challenge 1
# Fill in the string below, without using any space characters, so that the output is
# 12  4.5 6
# a   b   c
# apple\cherry
def print_something():
    s = '12\t4.5\t6\na\tb\tc\napple\\cherry'  # fill in
    print(s)

# challenge 2
# What does the following function print?
def print_something_else():
    s = '    \n\tapple banana\n\n'
    print('*' + s + '*')
    print('*' + s.strip() + '*')


# challenge 3
# What does the following function print?
def print_more():
    s = 'abcdefghijabc'
    print(s.find('a'))
    print(s.find('d'))
    print(s.find('j'))
    print(s.find('k'))
    print(s.find('def'))
    print(s.find('ace'))
    print(s.rfind('b'))
    print(s.find('b', 4))
    print(s.find('b', 4, 8))

# challenge 4
# What does the following function print?
def print_even_more():
    s = 'abcdefg'
    t = 'cd'
    if t in s:
        print('t in s')
    if s in t:
        print('s in t')
    if s > t:
        print('s > t')
    if t > s:
        print('t > s')

# challenge 5
# Fix the incorrect line
def sort_words(word1, word2):
    """Print the two words in alphabetical order, where the order is case-insensitive"""
    if word1.lower() < word2.lower():  # fix this line
        print(word1, word2)
    else:
        print(word2, word1)

# challenge 6
# Write this function
def print_to_Dickinson(s):
    """If s contains the string 'Dickinson', print up to and including the last
    occurrence of 'Dickinson'. Otherwise, print 'not found'."""
    dson = 'Dickinson'
    index = s.rfind(dson)
    if index != -1:
        end = index + len(dson)
        print(s[:end])
    else:
        print('not found')
