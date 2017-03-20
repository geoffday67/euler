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

primes = [2]
count = 1
n = 2
while count < 10001:
    if is_prime(n, primes):
        primes.append(n)
        count += 1
    n += 1
print (primes[-1])