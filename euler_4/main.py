def is_palindrome(n):
    s = str(n)
    l = len(s)
    for i in range(l // 2):
        if s[i] != s[l-i-1]:
            return False
    return True

max = 0
for a in range (1000):
    for b in range (1000):
        if is_palindrome(a * b):
            if a * b > max:
                max = a * b

print (max)