from SYKHamiltonian import *
from DiagonalizeHamiltonian import *
import matplotlib.pyplot as plt


def createHistogram():
    numberOfParticles = 8

    data = diagonalizeHamiltonian(numberOfParticles)["eigenValue"]

    plt.hist(data, bins=30)

    plt.show()


if __name__ == '__main__':
    createHistogram()

