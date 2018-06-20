def checkio(n, m):
    t1, t2 = str(bin(n)[2:]).zfill(32), str(bin(m)[2:]).zfill(32)
    return sum([1 for i in range(32) if t1[i]!=t2[i]])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
    assert checkio(1,999999) == 11
