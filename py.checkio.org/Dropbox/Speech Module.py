FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    answer = []
    hundred = int(number/100)
    ten = int((number - hundred*100)/10)
    ften = int(number - hundred*100 - ten*10)
    print(hundred, ten, ften)
    if(hundred>0):
        answer.append(FIRST_TEN[hundred-1]+' '+HUNDRED)
    if(ten>1):
        answer.append(OTHER_TENS[ten-2])
    if(ften>0 and ten!=1):
        answer.append(FIRST_TEN[ften-1])
    if(ten==1):
        answer.append(SECOND_TEN[ften])
    return ' '.join(answer)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(checkio(12))
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')