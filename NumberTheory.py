import numpy as np


def is_prime(num):
    i = 2
    running = True
    while running and i < num:
        if num % i == 0:
            return False
        i = i + 1
        return True


def find_primes(numMax):
    i = 2
    primes = []
    for i in range(i, numMax):
        if is_prime(i):
            primes.append(i)
    return primes


def how_many_primes(num):
    primes = find_primes(num)
    count = 0
    for _ in primes:
        count = count + 1
    return count


def ggT(num1, num2):
    if num1 % num2 == 0:
        return num2
    else:
        return ggT(num2, (num1 % num2))


def kgV(num1, num2):
    i = 2
    while not ((i % num1 == 0) and (i % num2 == 0)):
        if i > 10_000_000:
            print("No kgV was found in the Integers 1-10_000_000")
            return -1
        i = i + 1
    return i


def is_invertible(element, RestKlasssenRing):
    if ggT(element, RestKlasssenRing) == 1:
        return True
    else:
        return False


def find_invertible(element, RestKlassenRing):
    if is_invertible(element, RestKlassenRing):
        for i in range(1, 10_000):
            if ((element * i) % RestKlassenRing) == 1:
                return i
        print("No Inverse found in the Integers of 1-10.000")


def euler_phi(num):
    i = 1
    oddTeilerfremd = []
    for i in range(i, num):
        if ggT(num, i) == 1:
            oddTeilerfremd.append(i)
    return len(oddTeilerfremd)


def prime_factors(num):
    factors = []
    primesOneToNum = find_primes(int(np.sqrt(num) + 1))
    while num != 1:
        for i in primesOneToNum:
            if num % i == 0:
                while num % i == 0:
                    num = num / i
                    factors.append(i)
    return factors


class Permutation:
    #TODO pi^x + verknüfpungen

    def __init__(self, connections):
            self.connections = connections

    def pi(self, x):
        for i in self.connections:
            for j in range(0, len(i)):
                if i[j] == x:
                    if len(i)-1 > j:
                        return i[j+1]
                    else:
                        return i[0]
