import numpy as np
from scipy import linalg, integrate


def integrand(*elements):
    L = len(elements)
    trace = 0
    for e in elements:
        trace += e ** 2
    return trace

    return np.exp(-0.5 * L * trace)


def ensembleAverage(*elements, x):
    integrateRange = [[-np.inf, np.inf] for _ in range(len(elements))]
    return integrate.nquad(integrand, integrateRange) * x
