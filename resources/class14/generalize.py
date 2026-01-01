import random

# Print the result of rolling some dice
def roll_dice(num_dice, num_sides):
    total = 0
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        total = total + roll
    print('Dice total is', total)

roll_dice(4, 6)

