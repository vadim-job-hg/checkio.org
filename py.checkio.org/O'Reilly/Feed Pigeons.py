def checkio(number):
    count, i = 0, 1
    while count + i<=number:
        print('count, i<=number', count, i,number)
        count += i
        i += 1
        number -= count
    print('answer', count, i)
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"