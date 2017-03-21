import math

def triples(r):
    x = (r * r) // 2    # r must be even

    # Find the pairs of divisors of x
    pairs = set()
    for a in range(1, int(math.sqrt(x)) + 1):
        if x % a == 0:
            pairs.add ((a, x // a))

    # Each pair gives a triple
    triples = set()
    for pair in pairs:
        s, t = pair
        x = r + s
        y = r + t
        z = r + s + t
        triples.add ((x, y, z))

    return triples

for r in range(2, 1000):
    for triple in triples(r):
        x, y, z = triple
        if x + y + z == 1000:
            print (x, y, z, x * y * z)
