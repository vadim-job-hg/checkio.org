from typing import List
import math
def checkio(a: int, b: int, c: int) -> List[int]:
    if(a+b<=c or b+c<=a or c+a<=b):
        return [0, 0, 0]
    aA = round(math.degrees(math.acos((c*c+b*b-a*a)/(2*c*b))))
    aB = round(math.degrees(math.acos((c*c+a*a-b*b)/(2*c*a))))
    aC = round(math.degrees(math.acos((a*a+b*b-c*c)/(2*a*b))))
    return sorted([aA, aB, aC])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio(4, 4, 4))
    print(checkio(3, 4, 5))
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print("Coding complete? Click 'Check' to earn cool rewards!")
