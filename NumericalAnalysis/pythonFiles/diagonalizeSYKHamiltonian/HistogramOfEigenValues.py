from SYKHamiltonian import *
from DiagonalizeHamiltonian import *
import matplotlib.pyplot as plt


def createHistogram():
    numberOfParticles = 12
    numberOfbins = 15

    data = diagonalizeHamiltonian(numberOfParticles)["eigenValue"]
    data = [d.real for d in data]

    plt.hist(data, bins=numberOfbins)
    plt.show()


if __name__ == '__main__':
    createHistogram()
