def time_converter(time):
    h, m = time.split(':')
    pm, b12 = time.find(' p.m.') != -1, int(h) == 12
    result = '{}:{}'.format(str([[h, '00'][b12 and not (pm)], int(h) + 12][pm and not (b12)]).zfill(2),
                            m.replace(' p.m.', '').replace(' a.m.', ''))
    return result


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))
    print(time_converter('9:00 a.m.'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")
