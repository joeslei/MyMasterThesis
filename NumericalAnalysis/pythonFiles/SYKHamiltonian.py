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


def Hamiltonain(numberOfParticles, psiSet):

    J = randomCouplingTensor(numberOfParticles)
    psiArray = psiSet(numberOfParticles)
    numberOfFermions = int(numberOfParticles / 2)

    hamiltonian = mat([[0 for _ in range(2 ** numberOfFermions)]\
            for _ in range(2 ** numberOfFermions)])

    for a in range(numberOfParticles):
        for b in range(numberOfParticles):
            for c in range(numberOfParticles):
                for d in range(numberOfParticles):
                    hamiltonian = hamiltonian + \
                            J[a, b, c, d] * psiArray[a] * psiArray[b] * psiArray[c] * psiArray[d]

    return hamiltonian / scipy.special.factorial(numberOfParticles, exact=True)


def main():
    numberOfParticles = 4
    print(Hamiltonain(numberOfParticles, psiSet))

            
if __name__ == '__main__':
    main()