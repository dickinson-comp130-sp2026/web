import random

def roll_dice(num_dice, num_sides):
    total = 0
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        total = total + roll
    print('Dice total is', total)

# Print the result of rolling some six-sided dice
def roll_sixsided_dice(num_dice):
    roll_dice(num_dice, 6)


# Print the result of rolling some eight-sided dice
def roll_eightsided_dice(num_dice):
    roll_dice(num_dice, 8)



print('Rolling 4 six-sided dice...')
roll_sixsided_dice(4)

print()
print('Rolling 10 eight-sided dice...')
roll_eightsided_dice(10)



