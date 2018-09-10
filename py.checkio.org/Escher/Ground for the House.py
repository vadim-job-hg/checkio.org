def rotate(matr):
    return list(zip(*matr[::-1]))

def cut_from_top(matr):
    return matr if matr[0].count('#') else matr[1:]

def house(plan):
    matr, size = [list(line) for line in plan.split('\n') if len(line)], 0
    while True:
        for i in range(4):
            matr = rotate(matr)
            matr = cut_from_top(matr)
            if (len(matr) == 0):
                return 0
        if (size == len(matr) * len(matr[0])):
            break
        else:
            size = len(matr) * len(matr[0])

    return size


if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
