import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def is_dashed(word):
    word = ''.join([x for x in word.upper()])
    if (len(word) < 2):
        return False

    if (not (word[0] in VOWELS) and not (word[0] in CONSONANTS)):
        return False

    vow = word[0] in VOWELS
    for i in range(1, len(word)):
        if (vow and word[i] in VOWELS):
            return False
        if (not (vow) and word[i] in CONSONANTS):
            return False
        vow = not (vow)
    return True


def checkio(text):
    print(re.split('\W+', text))
    print(sum(1 for x in re.split('\W+', text) if is_dashed(x)))
    return sum(1 for x in re.split('\W+', text) if is_dashed(x))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
