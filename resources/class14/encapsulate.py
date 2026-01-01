import random

# Print the result of rolling some six-sided dice
def roll_sixsided_dice(num_dice):
    total = 0
    for i in range(num_dice):
        roll = random.randint(1, 6)
        total = total + roll
    print('Dice total is', total)

roll_sixsided_dice(4)

