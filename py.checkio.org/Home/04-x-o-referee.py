def checkio(gr):
    r = gr
    r += ["".join(v) for v in zip(*gr)]
    r += [gr[0][0] + gr[1][1] + gr[2][2],
          gr[0][2] + gr[1][1] + gr[2][0]]

    o = r.count("OOO")
    x = r.count("XXX")

    if o and x:
        return "D"
    elif o:
        return "O"
    elif x:
        return "X"
    else:
        return "D"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

