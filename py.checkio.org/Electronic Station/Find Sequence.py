def checkio(matrix):
    string_array = []
    for x in range(len(matrix)):
        string_array.append(''.join([str(y) for y in matrix[x]]))
        string_array.append(''.join([str(matrix[z][x]) for z in range(len(matrix))]))
        string_array.append(''.join([str(matrix[z + x][z]) for z in range(len(matrix)) if z + x < len(matrix)]))
        string_array.append(''.join([str(matrix[z - x][z]) for z in range(len(matrix)) if z - x >= 0]))

    matrix = [m[::-1] for m in matrix]
    for x in range(len(matrix)):
        string_array.append(''.join([str(matrix[z + x][z]) for z in range(len(matrix)) if z + x < len(matrix)]))
        string_array.append(''.join([str(matrix[z - x][z]) for z in range(len(matrix)) if z - x >= 0]))

    # print(string_array)
    for n in range(10):
        if any([s.find(str(n) * 4) != -1 for s in string_array]):
            return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
