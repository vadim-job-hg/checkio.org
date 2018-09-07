def to_encrypt(text, delta):
    # replace this for solution
    return ''.join([[chr([[ord(x) + delta, ord('a') + (ord(x) + delta - ord('z'))-1][ord(x) + delta > ord('z')],
                          ord('z') - (ord('a') - (ord(x) + delta)) + 1][ord(x) + delta < ord('a')]), x][x == ' '] for x
                    in text])

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")