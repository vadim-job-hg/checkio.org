def longest_palindromic(text):
    palindromes = ['']
    for i in range(len(text)):
        for j in range(i, len(text)):
            if text[i:j+1]==text[i:j+1][::-1]:
                palindromes.append(text[i:j+1])
    return max(palindromes, key=len)

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
