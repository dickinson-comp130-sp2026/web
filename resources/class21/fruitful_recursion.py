# Calculate 1*1 + 2*2 + 3*3 + ... + n*n
# We could easily do this using a for loop, but here we show how to do the calculation using recursion.
def sum_of_squares(n):
    if n == 1:
        return 1
    else:
        prev_sum = sum_of_squares(n - 1)
        new_sum = prev_sum + n * n
        return new_sum


k = 3
s = sum_of_squares(k)
print("The sum of the squares from 1 to", k, "is:", s)
      
