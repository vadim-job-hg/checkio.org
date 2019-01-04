import math
def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    prefix = 0
    while abs(number)>base or prefix>=len(powers):
        number, prefix = [number/base, [math.ceil(number/base),math.floor(number/base)][number>0]/1.0][decimals==0], prefix+1

    return "{:.{}f}{}{}".format(number, decimals, powers[prefix], suffix )

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    assert friendly_number(-150, base=100, powers=["","d","D"]) == '-1d', '-1d'

