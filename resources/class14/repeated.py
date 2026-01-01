import random

# Print the result of rolling some six-sided dice
def roll_sixsided_dice(num_dice):
    total = 0
    for i in range(num_dice):
        roll = random.randint(1, 6)
        total = total + roll
    print('Dice total is', total)


# Print the result of rolling some eight-sided dice
def roll_eightsided_dice(num_dice):
    total = 0
    for i in range(num_dice):
        roll = random.randint(1, 8)
        total = total + roll
    print('Dice total is', total)



print('Rolling 4 six-sided dice...')
roll_sixsided_dice(4)

print()
print('Rolling 10 eight-sided dice...')
roll_eightsided_dice(10)



