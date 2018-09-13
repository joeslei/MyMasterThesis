import scipy.linalg
from SYKHamiltonian import *


def diagonalizeHamiltonian(numberOfPaticles):
    eigenValue, eigenVector = scipy.linalg.eig(Hamiltonian(numberOfPaticles, psiSet))

    return {"eigenValue": eigenValue, "eigenVector": eigenVector}


def main():
    numberOfPaticles = 8
    result = diagonalizeHamiltonian(numberOfPaticles)
    print("eigenValue = {}".format(result["eigenValue"]))
    print("eigenVector = {}".format(result["eigenVector"]))


if __name__ == '__main__':
    main()

