# https://github.com/anton-shablyko/checkio_solutions
def recall_password(cipher_grille, ciphered_password):
    result = []
    for z in range(4):
        for pair in zip(cipher_grille, ciphered_password):
            for a, b in zip(*pair):
                if a == 'X':
                    result.append(b)
        cipher_grille = list(zip(*cipher_grille[::-1]))
    return ''.join(result)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
