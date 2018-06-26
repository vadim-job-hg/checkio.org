def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    response, b, e = [], 0, 0
    list = sorted(data)
    if(len(list)>0):
        for i in range(1, len(list)):
            if(list[i]-list[e]>1):
                response.append(tuple([list[b], list[e]]))
                b = i
            e = i
        if((list[b], list[e]) not in response):
            response.append(tuple([list[b], list[e]]))
    return response

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(create_intervals({1, 2, 3, 4, 5, 7, 8, 12}))
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
