"""The Next Palindrome"""
a = int(input("Enter a number\n"))
def Is_palindrome(n):
    return int(str(n)[::-1]) == n
def next_palindrome(m):
    i = m
    while True:
        if Is_palindrome(i):
            break
        i += 1
    return i
print(next_palindrome(a))