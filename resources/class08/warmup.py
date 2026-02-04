# Three equivalent implementations of solutions to our warm up exercise for today:
# Write a function that returns "yes" when its parameter is a multiple of five or if it's between 1000 and 2000.

# Using chained conditional
def f(n):
    if n%5 == 0:
        print("yes")
    elif n>1000 and n<2000:
        print("yes")
    else:
        print("no")

# Using a more complex boolean expression and a simpler conditional statement
def f2(n):
    if n%5 == 0 or (n>1000 and n<2000):
        print("yes")
    else:
        print("no")

# Using nested conditional statements. (Not particularly recommended in this particular example since the other approaches are easier to read and understand.)
def f3(n):
    if n%5 == 0:
        print("yes")
    else:
        if n>1000 and n<2000:
            print("yes")
        else:
            print("no")
        
f(25)
f(26)
f(1001)
f(3001)
