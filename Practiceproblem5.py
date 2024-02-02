"""Palindromify The List"""
lst1 = [1,5,45,23,789,6,98,9,753,10]
def Is_palindrome(n):
    return int(str(n)[::-1]) == n
def next_palindrome(m):
    i = m
    while True:
        if Is_palindrome(i):
            break
        i += 1
    return i
print(list(map(next_palindrome,lst1)))