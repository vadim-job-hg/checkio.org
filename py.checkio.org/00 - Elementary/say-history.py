# 1. on CheckiO your solution should be a function
# 2. the function should return the right answer, not print it.

def say_hi(name, age):
    """
        Hi!
    """
    # your code here
    return f"Hi. My name is {name} and I'm {age} years old"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')
