import random

def roll_dice():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 8)
    roll3 = random.randint(1, 20)
    total = roll1 + roll2 + roll3
    print('You rolled a total of', total)


roll_dice()
roll_dice()
roll_dice()
roll_dice()

