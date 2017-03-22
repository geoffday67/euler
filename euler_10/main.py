import math

def is_prime(n, primes):
    # Start testing with the first prime in the list
    p = 0

    # Only test up to the square root of the number, if it has a factor at all it will be in that range
    limit = math.floor(math.sqrt(n)) + 1
    found = True
    while p < len(primes) and primes[p] <= limit:
        if n % primes[p] == 0:
            found = False
            break
        p += 1
    return found

primes = [2, 3]
n = 5
while n < 2000000:
    if is_prime(n, primes):
        primes.append(n)
    n += 2
print (sum(primes))