from SYKHamiltonian import *
from DiagonalizeHamiltonian import *
import matplotlib.pyplot as plt


def createHistogram():
    numberOfParticles = int(input("input the number of particles: "))
    numberOfbins = 300

    data = diagonalizeHamiltonian(numberOfParticles)["eigenValue"]

    plt.hist(data, bins=numberOfbins)

    plt.show()


if __name__ == '__main__':
    createHistogram()

