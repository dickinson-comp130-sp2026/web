import random


# challenge 1
def print_evens_up_to(n):
    i = 2
    while i <= n:
        print(i)
        i = i + 2
    print('finished printing')


# challenge 2
def dice_rolls_to_100B():
    total = 0
    count = 0
    done = False
    while not done:
        roll = random.randint(1, 6)
        total = total + roll
        count = count + 1
        if total >= 100:
            done = True
    return count


# challenge 3
def dice_rolls_to_100C():
    total = 0
    count = 0
    while True:
        roll = random.randint(1, 6)
        total = total + roll
        count = count + 1
        if total >= 100:
            break
    return count
