a = 1
b = 1
sum = 0

while True:
    n = a + b
    if n > 4000000:
        break
    if n % 2 == 0:
        sum += n
    a = b
    b = n

print (sum)