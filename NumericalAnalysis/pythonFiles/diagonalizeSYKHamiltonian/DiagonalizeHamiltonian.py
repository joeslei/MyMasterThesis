import scipy.linalg
from SYKHamiltonian import *


def diagonalizeHamiltonian(numberOfPaticles):
    eigenValue, eigenVector = scipy.linalg.eig(Hamiltonian(numberOfPaticles, psiSet))

    return {"eigenValue": eigenValue, "eigenVector": eigenVector}


def main():
    numberOfPaticles = 8
    result = diagonalizeHamiltonian(numberOfPaticles)
    eigenValue = [e.real for e in result["eigenValue"]]
    for e in eigenValue:
        print(e)


if __name__ == '__main__':
    main()
