from numpy import sqrt
from numpy import mat
from FockSpace import *
from RandomCouplingTensor import randomCouplingTensor
import scipy.special


def psiSet(numberOfParticles):
    psiArray = []
    numberOfFermions = int(numberOfParticles / 2)
    stateVectors = stateVectorSet(numberOfParticles)

    annihilationOperatorSet = annihilationOperatorMatricesSet(numberOfParticles, stateVectors)
    creationOperatorSet = creationOperatorMatricesSet(numberOfParticles, stateVectors)

    for i in range(numberOfFermions):
        psi = (annihilationOperatorSet[i] + creationOperatorSet[i]) / sqrt(2)
        psiArray.append(psi)
        psi = (1J * (annihilationOperatorSet[i] - creationOperatorSet[i])) / sqrt(2)
        psiArray.append(psi)

    return psiArray


def Hamiltonian(numberOfParticles, psiSet):

    J = randomCouplingTensor(numberOfParticles)
    psiArray = psiSet(numberOfParticles)
    numberOfFermions = int(numberOfParticles / 2)

    hamiltonian = mat([[0 for _ in range(2 ** numberOfFermions)]\
            for _ in range(2 ** numberOfFermions)])

    for a in range(numberOfParticles):
        print("Creating Hamiltonian: a = " + str(a))
        for b in range(numberOfParticles):
            for c in range(numberOfParticles):
                for d in range(numberOfParticles):
                    hamiltonian = hamiltonian + \
                            J[a, b, c, d] * psiArray[a] * psiArray[b] * psiArray[c] * psiArray[d]

    return hamiltonian / scipy.special.factorial(numberOfParticles, exact=True)


def main():
    numberOfParticles = 8
    dimOfHilbertSpace = int(2 ** (numberOfParticles / 2))
    h = Hamiltonian(numberOfParticles, psiSet)
    for i in range(dimOfHilbertSpace):
        for j in range(dimOfHilbertSpace):
            if h[i,j] != h[j,i].conjugate():
                print("i = {}, j = {}".format(i, j))
                print("h[i,j] = {}, h[j, i] = {}".format(h[i,j], h[j,i]))
                print("-------------------------------------------------")

            
if __name__ == '__main__':
    main()
