# What is g(3)? Try to figure it out by hand.
def g(n):
    if n == 1:
        return 3
    else:
        prev = g(n - 1)
        return 5 + 2 * prev

# What is h(3)? Try to figure it out by hand.
def h(n):
    if n == 1:
        return 2
    else:
        prev = h(n - 1)
        return (prev + 30) / 2

