import math


def findfactor(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


def factorise(n, factors):
    factor = findfactor(n)
    factors.append(factor)
    if factor == n:
        return
    factorise(n // factor, factors)


def powers(n):
    factors = []
    factorise(n, factors)
    result = {}
    for n in factors:
        if n in result:
            result[n] = result[n] + 1
        else:
            result[n] = 1
    return result


def lcm(n1, n2):
    p3 = {}
    p1 = powers(n1)
    p2 = powers(n2)
    for n in p1.keys():
        if n in p2.keys():
            p3[n] = max(p1[n], p2[n])
        else:
            p3[n] = p1[n]
    for n in p2.keys():
        if n not in p1.keys():
            p3[n] = p2[n]
    result = 1
    for n in p3.keys():
        result *= n ** p3[n]
    return result


print(powers(100))

# l = 1
# for n in range(1, 20):
#    l = lcm (l, n)
# print (l)
