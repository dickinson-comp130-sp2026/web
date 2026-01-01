import random

# Print the result of rolling 4 six-sided dice
total = 0
for i in range(4):
    roll = random.randint(1, 6)
    total = total + roll
print('Dice total is', total)

