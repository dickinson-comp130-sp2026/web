import random


# basic while loop
def print_up_to(n):
    i = 1
    while i <= n:
        print(i)
        i = i + 1
    print('finished printing')


# challenge 1: rewrite using a while loop
def print_evens_up_to(n):
    for i in range(2, n + 1, 2):
        print(i)
    print('finished printing')


# count how many 6-sided dice rolls are needed to get to 100
def dice_rolls_to_100():
    total = 0
    count = 0
    while total < 100:
        roll = random.randint(1, 6)
        total = total + roll
        count = count + 1
    return count


# challenge 2: fix this by adding new lines of code,
# but don't change the existing lines
def dice_rolls_to_100B():
    total = 0
    count = 0
    done = False
    while not done:
        roll = random.randint(1, 6)
        total = total + roll
        count = count + 1
    return count


# count how many rolls of 2 dice are needed to get a double 6
def dice_rolls_for_double_6():
    count = 0
    while True:
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        count = count + 1
        if roll1 == 6 and roll2 == 6:
            break
    return count


# challenge 3: fix this by adding new lines of code,
# but don't change the existing lines
def dice_rolls_to_100C():
    total = 0
    count = 0
    while True:
        roll = random.randint(1, 6)
        total = total + roll
        count = count + 1
    return count


