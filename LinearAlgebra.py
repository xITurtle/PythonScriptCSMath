import numpy as np


def vector_multiply(vec1, vec2):
    vecRes = [[0 for _ in range(len(vec2[0]))] for _ in range(len(vec1))]
    if not (len(vec1[0]) == len(vec2)):
        print("Vector multiplication is not defined ont these vectors.")
        return -1
    for i in range(len(vec1)):
        for j in range(len(vec2[0])):
            for k in range(len(vec2)):
                vecRes[i][j] += vec1[i][k] * vec2[k][j]

    return vecRes


def solve_lgs():
    # TODO
    pass


class ComplexNumbers:
    real = 0
    complex = 0

    def __init__(self, re, im):
        self.real = re
        self.complex = im

    def addition(self, re, im):
        return self.real + re, self.complex + im

    def multiplication(self, re, im):
        newRe = self.real * re - self.complex * im
        newIm = self.real * im + self.complex * re
        return newRe, newIm

    def konjugation(self):
        return self.real, self.complex * -1

    def length(self):
        return np.sqrt(self.real * self.real + self.complex * self.complex)
