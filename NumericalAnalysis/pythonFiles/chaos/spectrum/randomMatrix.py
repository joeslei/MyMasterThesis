import numpy as np
import matplotlib.pyplot as plt
from plotSpectrum import plotSpectrum


def gaussianOrthogonalEnsemble(matrixSize, mean=0, deviation=1):
    randomMatrix = []
    for _ in range(matrixSize):
        v = np.random.normal(loc=mean, scale=deviation, size=matrixSize)
        randomMatrix.append(v)

    orthogonalMatrix, r = np.linalg.qr(randomMatrix)

    return orthogonalMatrix


def main():
    mat = gaussianOrthogonalEnsemble(7)
    components = []
    for i in mat:
        for j in i:
            components.append(j)
    plotSpectrum(components)


if __name__ == "__main__":
    main()
