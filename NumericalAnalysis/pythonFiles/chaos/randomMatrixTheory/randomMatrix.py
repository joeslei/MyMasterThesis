import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg


def hermitianRandomMatrix(size):
    result = np.mat([[0.0 for _ in range(size)] for _ in range(size)])

    for i in range(size):
        for j in range(i, size):
            result[i, j] = np.random.normal(loc=0.0, scale=1.0 / np.sqrt(size))
            result[j, i] = result[i, j]

    return result


def diagnalizeHermitianMatrix(matrix):
    if not np.allclose(matrix, matrix.T):
        print("ERROR: not hermitian matrix")
        return []

    eigenValues, eigenVectors = scipy.linalg.eigh(matrix)

    return eigenValues


def partitionFunction(beta, time, matrix):
    eigenValues = diagnalizeHermitianMatrix(matrix)

    return sum([np.exp(-(beta + 1j * time) * eigenValue) for eigenValue in eigenValues])


if __name__ == '__main__':
    size = 2 ** 10
    time_max = 10 ** 5
    time = np.linspace(0, time_max, num=time_max * 10, endpoint=True)
    numberOfEnsembles = 300
    spectrumFormFactor = []

    previous_t = 0
    for t in time:
        if int(t) % (time_max / 10) == 0 and int(t) != previous_t:
            print("t = {} / {}".format(str(int(t)), time_max))
            previous_t = int(t)

        numeratorArray = []
        denumeratorArray = []
        for i in range(numberOfEnsembles):
            matrix = hermitianRandomMatrix(size)

            Z = partitionFunction(beta=5, time=t, matrix=matrix)
            Z_0 = partitionFunction(beta=5, time=0, matrix=matrix)

            numeratorArray.append((Z * Z.conjugate()).real)
            denumeratorArray.append(Z_0.real)
        numerator = sum(numeratorArray) / numberOfEnsembles
        denumerator = (sum(denumeratorArray) / numberOfEnsembles) ** 2
        spectrumFormFactor.append(numerator / denumerator)
    plt.plot(time, spectrumFormFactor)
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()
