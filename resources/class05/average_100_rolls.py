import random

total = 0
for i in range(100):
    result = random.randint(1, 20)
    total = total + result
average = total / 100
print("Average of 100 rolls:", average)
    
