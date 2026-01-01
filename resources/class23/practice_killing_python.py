# Watch out – what happens when we run this program? Learn how to deal with this by
# killing Python on your computer.
import random


def dice_rolls_for_20():
    count = 0
    while True:
        roll = random.randint(1, 6)
        count = count + 1
        if roll == 20:
            break
    return count


num_rolls = dice_rolls_for_20()
print(num_rolls)
