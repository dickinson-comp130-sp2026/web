import random


# Randomly return one of the following: 'Go', 'Come on', 'Keep it up'
def get_cheer_verb():
    val = random.randint(1, 3)
    if val == 1:
        return 'Go'
    elif val == 2:
        return 'Come on'
    else:
        return 'Keep it up'


# Randomly return one of the following: 'Dickinson', 'Red Devils'
def get_team_name():
    val = random.randint(1, 2)
    if val == 1:
        return 'Dickinson'
    else:
        return 'Red Devils'


# Randomly return one of the following: 'lacrosse', 'swimming', 'programming'
def get_sport():
    val = random.randint(1, 3)
    if val == 1:
        return 'lacrosse'
    elif val == 2:
        return 'swimming'
    else:
        return 'programming'


# Return a random cheer by picking a verb, a team name, and a sport
def get_cheer():
    first_part = get_cheer_verb()
    middle_part = get_team_name()
    last_part = get_sport()
    cheer = first_part + ' ' + middle_part + ' ' + last_part + '!'
    return cheer


# Print many random cheers. The same random cheer should be repeated three times on the same line.
# The next line has a different random cheer repeated three times. This continues for 20 lines.
def print_many_cheers():
    for i in range(20):
        my_cheer = get_cheer()
        for j in range(3):
            print(my_cheer, end=' ')
        print()


# top-level code -- prints the cheers
print_many_cheers()

