import scipy.linalg
from SYKHamiltonian import *


def diagonalizeHamiltonian(numberOfPaticles):
    eigenValue, eigenVector = scipy.linalg.eig(Hamiltonain(numberOfPaticles, psiSet))

    return {"eigenValue": eigenValue, "eigenVector": eigenVector}


def main():
    numberOfPaticles = 4
    result = diagonalizeHamiltonian(numberOfPaticles)
    print("eigenValue = {}".format(result["eigenValue"]))
    print("eigenVector = {}".format(result["eigenVector"]))


if __name__ == '__main__':
    main()

