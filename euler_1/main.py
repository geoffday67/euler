sum = 0
for n in range(1, 1000):
    if n % 3 != 0 and n % 5 != 0:
        continue
    sum += n
print (sum)