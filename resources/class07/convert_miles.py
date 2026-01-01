def feet_to_miles1(num_feet):
    miles = num_feet // 5280
    remaining_feet = num_feet % 5280
    print(num_feet, 'feet is the same as', miles, 'miles and', remaining_feet, 'feet.')


def feet_to_miles2(num_feet):
    feet_in_mile = 5280
    miles = num_feet // feet_in_mile
    remaining_feet = num_feet % feet_in_mile
    print(num_feet, 'feet is the same as', miles, 'miles and', remaining_feet, 'feet.')


def feet_to_miles3(num_feet):
    if num_feet < 0:
        print("Sorry, I can't convert negative quantities.")
        print('Please ignore the output below.')

    feet_in_mile = 5280
    miles = num_feet // feet_in_mile
    remaining_feet = num_feet % feet_in_mile
    print(num_feet, 'feet is the same as', miles, 'miles and', remaining_feet, 'feet.')

def feet_to_miles4(num_feet):
    if num_feet < 0:
        print("Sorry, I can't convert negative quantities.")
        print('The input will be transformed to a positive number before continuing.')
        num_feet = -num_feet

    feet_in_mile = 5280
    miles = num_feet // feet_in_mile
    remaining_feet = num_feet % feet_in_mile
    print(num_feet, 'feet is the same as', miles, 'miles and', remaining_feet, 'feet.')

def feet_to_miles5(num_feet):
    if num_feet < 0:
        print("Sorry, I can't convert negative quantities.")
        print('The input will be transformed to a positive number before continuing.')
        num_feet = -num_feet
    else:
        print('Thanks for entering a non-negative quantity.')
        print('That makes my life easier.')

    feet_in_mile = 5280
    miles = num_feet // feet_in_mile
    remaining_feet = num_feet % feet_in_mile
    print(num_feet, 'feet is the same as', miles, 'miles and', remaining_feet, 'feet.')


def feet_to_miles6(num_feet):
    feet_in_mile = 5280
    if num_feet >= 0 and num_feet < feet_in_mile:
        print(num_feet, 'feet is less than 1 mile.')
        print("I don't need to convert that!")
    else:
        miles = num_feet // feet_in_mile
        remaining_feet = num_feet % feet_in_mile
        print(num_feet, 'feet is the same as', miles, 'miles and', remaining_feet, 'feet.')




# feet_to_miles1(29032)
# feet_to_miles2(29032)
# feet_to_miles3(-29032)
# feet_to_miles4(-29032)
# feet_to_miles6(1000)