import numpy as np

class DirectedWeightedGraph:
    nodes = []
    connections = [(0,0)]
    #TODO Add Weights
    
    def __innit__(nodesParam, connectionsParam):
        counter = 0
        for i in nodesParam:
            this.nodes[counter] = i
            counter = counter + 1
        counter = 0
        for i in connectionsParam:
            this.connections[counter] = i
            counter = counter + 1
            
    def is_connected(nodeStart, nodeEnd):
        pass
    
    def find_connection(nodeStart, nodeEnd):
        pass
    
    def find_lightest_way(nodeStart, nodeEnd):

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


def list_length(liste):
    count = 0
    for _ in liste:
        count = count + 1
    return count


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
    return list_length(oddTeilerfremd)


def null_stellen(coefficients):
    return np.roots(coefficients)


def prime_factors(num):
    factors = []
    primesOneToNum = find_primes(int(np.sqrt(num)+1))
    while num != 1:
        for i in primesOneToNum:
            if num % i == 0:
                while num % i == 0:
                    num = num / i
                    factors.append(i)
    return factors


def vector_multiply(vec1, vec2):
    vecRes = [[0 for _ in range(list_length(vec2[0]))] for _ in range(list_length(vec1))]
    if not (list_length(vec1[0]) == list_length(vec2)):
        print("Vector multiplication is not defined ont these vectors.")
        return -1
    for i in range(list_length(vec1)):
        for j in range(list_length(vec2[0])):
            for k in range(list_length(vec2)):
                vecRes[i][j] += vec1[i][k] * vec2[k][j]

    return vecRes


def solve_lgs():
    #TODO
    pass


def print_introduction():
    print("Availible functions:\n1-is_prime(INT)\n2-find_primes(INT)\n3-list_length(LIST)\n4-how_many_primes("
          "INT)\n5-ggT(INT)\n6-kgV(INT)\n7-is_invertible(INT, INT)\n8-find_invertible(INT, INT)\n9-euler_phi("
          "INT)\n10-null_stellen(LIST polynomial)\n11-prime_factors(INT)\n12-Vector_multiplication([[INT]], [[INT]])")

    
if __name__ == '__main__':
    print_introduction()
    #Ausführung hier hin:
    #print(prime_factors(4826))

    # TODO Graph-Gewichte, Dijkstra-ALG, LGS