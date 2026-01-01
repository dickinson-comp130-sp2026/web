def demonstrate_split(s):
    print('\nThe string s is:')
    print(s)

    print("\nThe result of s.split() is:")
    print(s.split())

    print("\nThe result of s.split(',') is:")
    print(s.split(','))

    print("\nThe result of s.split('ea') is:")
    print(s.split('ea'))


# This song lyric is from the track 'Rainforest' by the rapper/poet Noname
lyric = "You ain't seen death, I can hear the blood on the moon"
demonstrate_split(lyric)
