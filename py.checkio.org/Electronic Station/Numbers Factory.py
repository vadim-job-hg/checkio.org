def delimer_number(number):
    for n in range(9, 2, -1):
        if number % n == 0:
            return n, int(number / n)
    return None, None


def checkio(number):
    # replace this for
    delimers = []
    while number > 9:
        n, number = delimer_number(number)
        if (n is None):
            return 0
        delimers.append(str(n))
    delimers.append(str(number))
    return int(''.join(sorted(delimers)))


if __name__ == '__main__':
    print(checkio(560))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
