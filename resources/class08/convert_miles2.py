def feet_to_miles7(num_feet):
    feet_in_mile = 5280
    if num_feet < 0:
        print("Sorry, I can't convert negative quantities.")
    elif num_feet < feet_in_mile:
        print(num_feet, 'feet is less than 1 mile.')
        print("I don't need to convert that!")
    else:
        miles = num_feet // feet_in_mile
        remaining_feet = num_feet % feet_in_mile
        print(num_feet, 'feet is the same as', miles, 'miles and', remaining_feet, 'feet.')



def feet_to_miles8(num_feet):
    feet_in_mile = 5280
    miles = num_feet // feet_in_mile
    remaining_feet = num_feet % feet_in_mile
    if num_feet < 0:
        print("Sorry, I can't convert negative quantities.")
    elif num_feet < feet_in_mile:
        print(num_feet, 'feet is less than 1 mile.')
        print("I don't need to convert that!")
    elif remaining_feet == 0:
        print(num_feet, 'feet is the same as exactly', miles, 'miles')
    else:
        print(num_feet, 'feet is the same as', miles, 'miles and', remaining_feet, 'feet.')


def feet_to_miles9(num_feet):
    feet_in_mile = 5280
    miles = num_feet // feet_in_mile
    remaining_feet = num_feet % feet_in_mile
    if num_feet < 0:
        print("Sorry, I can't convert negative quantities.")
    elif num_feet < feet_in_mile:
        print(num_feet, 'feet is less than 1 mile.')
        print("I don't need to convert that!")
    elif remaining_feet == 0:
        if miles == 1:
            print(num_feet, 'feet is the same as exactly one mile')
        else:
            print(num_feet, 'feet is the same as exactly', miles, 'miles')
    else:
        if miles == 1:
            print(num_feet, 'feet is the same as one mile and', remaining_feet, 'feet.')
        else:
            print(num_feet, 'feet is the same as', miles, 'miles and', remaining_feet, 'feet.')


feet_to_miles7(-300)
feet_to_miles7(2000)
feet_to_miles7(50000)

feet_to_miles8(7000)
feet_to_miles8(3 * 5280)

feet_to_miles9(5280 + 200)