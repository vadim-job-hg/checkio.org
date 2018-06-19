def safe_pawns(pawns):
    l = ' abcdefgh '
    return sum([1 for pawn in pawns if l[l.find(pawn[0])-1] + str(int(pawn[1])-1) in pawns or l[l.find(pawn[0])+1]+str(int(pawn[1])-1) in pawns])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
