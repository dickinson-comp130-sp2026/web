def demonstrate_join(t):
    print('\nThe list t is:')
    print(t)

    print("\nThe result of 'ABC'.join(t) is:")
    print('ABC'.join(t))

    print("\nThe result of ','.join(t) is:")
    print(','.join(t))

    print("\nThe result of ' '.join(t) is:")
    print(' '.join(t))

    print("\nThe result of ''.join(t) is:")
    print(''.join(t))


# These words come from a line in the poem Lamenting Widow by Ho Xuan Huong
t = ["Don't", 'eat', 'the', 'meat', 'if', 'it', 'makes', 'you', 'cough', 'blood']
demonstrate_join(t)
