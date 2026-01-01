def decide1(hungry, tired):
    if hungry:
        if tired:
            print('get takeout')
        else:
            print('cook dinner')
    else:
        if tired:
            print('sleep')
        else:
            print('watch Netflix')


def decide2(hungry, tired):
    if hungry and tired:
        print('get takeout')
    elif hungry and not tired:
        print('cook dinner')
    elif not hungry and tired:
        print('sleep')
    else:  # not hungry and not tired
        print('watch Netflix')
