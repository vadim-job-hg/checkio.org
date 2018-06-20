def s(time):
    return int(time[:2])*60 + int(time[3:])

def sun_angle(time):
    return [((s(time)-s('06:00'))/(s('18:00')-s('06:00')))*180, "I don't see the sun!"][s(time)<s('06:00') or s(time)>s('18:00')]

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")