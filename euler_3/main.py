import math

def findfactor(n):
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n

def factorise(n, factors):
    factor = findfactor(n)
    factors.add(factor)
    if factor == n:
        return
    factorise(n // factor, factors)

factors = set()
factorise(600851475143, factors)

max = 0
for n in factors:
    if n > max:
        max = n

print(max)