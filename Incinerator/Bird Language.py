VOWELS = "aeiouy"

def translate(phrase):
    list, skip = [], 0
    for i in range(len(phrase)):
        if (skip):
            skip-=1
            continue
        elif(phrase[i] not in VOWELS):
            list.append(phrase[i])
        elif(phrase[i]*3==phrase[i:i+3]):
            list.append(phrase[i])
            skip = 2
    return ''.join(list)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(translate("hoooowe yyyooouuu duoooiiine"))
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
