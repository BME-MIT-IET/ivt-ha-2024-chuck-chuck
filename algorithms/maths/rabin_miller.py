"""
Rabin-Miller primality test
returning False implies that n is guaranteed composite
returning True means that n is probably prime
with a 4 ** -k chance of being wrong
"""
import random

import random

def is_prime(n, k):
    if n < 5:
        return n == 2 or n == 3

    r, d = pow2_factor(n - 1)

    for _ in range(k):
        if is_composite(n, r, d):
            return False

    return True

def pow2_factor(num):
    """Factor n into a power of 2 times an odd number"""
    power = 0
    while num % 2 == 0:
        num //= 2
        power += 1
    return power, num

def is_composite(n, r, d):
    """Check if n is composite using Miller-Rabin primality test"""
    for _ in range(k):
        if valid_witness(n, r, d, random.randrange(2, n - 2)):
            return True
    return False

def valid_witness(n, r, d, a):
    """Check if a is a valid 'witness' for n"""
    x = pow(int(a), int(d), int(n))

    if x in (1, n - 1):
        return False

    for _ in range(r - 1):
        x = pow(int(x), int(2), int(n))

        if x == 1:
            return True
        if x == n - 1:
            return False

    return True
