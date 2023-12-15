import numpy as np


class Polynom:

    def __init__(self, coefficients):
        self.coefficients = list(coefficients)  # Erstellen einer Kopie der Liste
        self.degree = len(coefficients) - 1

    def null_stellen(self):
        return np.roots(self.coefficients)

    def evaluate(self, x):
        y = 0
        counter = 0
        for i in self.coefficients:
            y = y + i * pow(x, counter)
            counter = counter + 1
        return y
