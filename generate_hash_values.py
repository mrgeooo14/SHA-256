import math
import numpy as np

def hash_values():  # Hash Values, fractions of square rooting the first 8 prime numbers (2, 3, 5, 7, 11, 13, 17, 19).
    h = []
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    for prime in primes:
        s_root = math.sqrt(prime)
        fractions = math.modf(s_root)[0]
        fractions = int(fractions * (2 ** 32))
        h.append("{0:b}".format(fractions).zfill(32))
    return h


def create_constants():  # Hash Constants, the fractions of cubed rooting the first 64 prime numbers
    k = []
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
              59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
              127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
              191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
              257, 263, 269, 271, 277, 281, 283, 293, 307, 311]
    roots = np.cbrt(primes, dtype=np.float64)
    fractions = np.modf(roots)[0]

    for fraction in fractions:
        z = int(fraction * (2 ** 32))
        k.append("{0:b}".format(z))
        # k.append('0x{:08x}'.format(z))
    return k
