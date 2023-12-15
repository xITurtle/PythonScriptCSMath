import GraphTheroy
import NumberTheory
import LinearAlgebra
import Polynomial


def print_introduction():
    print("Availible functions:\n1-is_prime(INT)\n2-find_primes(INT)\n3-list_length(LIST)\n4-how_many_primes("
          "INT)\n5-ggT(INT)\n6-kgV(INT)\n7-is_invertible(INT, INT)\n8-find_invertible(INT, INT)\n9-euler_phi("
          "INT)\n10-null_stellen(LIST polynomial)\n11-prime_factors(INT)\n12-Vector_multiplication([[INT]], [[INT]])")


if __name__ == '__main__':
    pass
    # print_introduction()

    # Ausführung hier hin:
    # ----------NumberTheory-------------
    # print(NumberTheory.prime_factors(4826))
    # permutation = NumberTheory.Permutation([(1,2,3), (4,4)])
    # print(permutation.pi(4))
    # ----------GraphTheroy--------------
    # Graph1 = GraphTheroy.DirectedWeightedGraph([1, 2, 3, 4], [(1, 2), (2, 3), (3, 4)])
    # ----------Polynomial----------------
    # Polynom1 = Polynomial.Polynom([1,2,3])
    # print(Polynom1.evaluate(4))
    # ----------LinearAlgebra----------------
    # KomplexeZahl1 = LinearAlgebra.ComplexNumbers(4,2)
    # print(KomplexeZahl1.multiplication(4,2))


    # TODO Graph-Gewichte, Dijkstra-ALG, LGS, Integrale, Permutationen pi^x, Verknüpfugnen
