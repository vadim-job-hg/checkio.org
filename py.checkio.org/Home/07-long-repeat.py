def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here

    return 0 if line == '' else max(
        [i for i in range(1, len(line) + 1) if any([True for char in line if line.find(char * i) != -1])])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
