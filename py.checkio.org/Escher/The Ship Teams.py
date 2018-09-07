def two_teams(sailors):
    #replace this for solution
    return [
        sorted([k for k,v in sailors.items() if v<20 or v>40]),
        sorted([k for k,v in sailors.items() if 40>=v>=20])
    ]

if __name__ == '__main__':
    print("Example:")
    print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert two_teams({
        'Smith': 34,
        'Wesson': 22,
        'Coleman': 45,
        'Abrahams': 19}) == [
            ['Abrahams', 'Coleman'],
            ['Smith', 'Wesson']
            ]

    assert two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
            ['Fernandes', 'Kale', 'McCortney'],
            ['Johnson']
            ]
    print("Coding complete? Click 'Check' to earn cool rewards!")
