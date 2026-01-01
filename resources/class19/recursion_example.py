# Print some consecutive numbers using a for loop.
def print_from_m_to_n(m, n):
    for i in range(m, n+1):
        print(i)



# Same thing using recursion - this seems more complex, but it introduces a very
# important new idea
##def print_from_m_to_n(m, n):
##    if m == n:
##        print(n)
##    else:
##        print(m)
##        print_from_m_to_n(m + 1, n)
##    print("We're back in the stack frame with m =", m)
##    print('That stack frame will now disappear, because the function has finished.')
##    print()



print_from_m_to_n(3, 7)

