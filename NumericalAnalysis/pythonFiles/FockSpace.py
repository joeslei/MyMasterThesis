from numpy import mat
from KroneckerDeltaFunction import delta


def stateVectorSet(numberOfPaticles):
    '''
    Create a set of state vectors in the Fock space

    For example, if the number of particles is four then the reslut set is
    [[0,0], [0,1], [1,0], [1,1]].

    ----------------------------------------------------
        how to create the fermion state vectors
    ----------------------------------------------------

    Since the number of a fermion is zero or one,
    we have states such that | 0 0 1 0 1 1 ...> and so on.

    Thus we have a  binary number 001011... for each state vector,
    and we can make a correspondece between a state representated in a binary number
    and a number with base 10.

    For example, let us consider a state such that only the first fermon exists: |1 0 0 0 0 ... >.
    This state corresponds to 1 in the base 10, and its binary representation is 000...00001.

    Note that we expect the way of numbering fermions as | "first", "second", "third", ... >,
    but the corresponding binary number has the reversed numbering way
    i.e.  000...000 "third" "second" "first".
    So we need to reverse the binary numbers.
    '''

    # number of fermions in the Fock space
    N = int(numberOfPaticles / 2)

    stateVectorArray = []

    for i in range(2 ** N):
        stateString = bin(i)
        stateString = stateString[2:]
        while len(stateString) < N:
            stateString = "0" + stateString
        stateVector = list(stateString)
        stateVector = list(map(int, stateVector))
        stateVector = stateVector[::-1]
        stateVectorArray.append(stateVector)

    return stateVectorArray


def creationOperatorMatrixElement(fermionIndex, leftStateVector, rightStateVector):
    '''
    creation operator on the Fock space

    fermionIndex: if its value is N, then Nth fermion will be created.
    '''

    left = leftStateVector
    right = rightStateVector

    matrixElement = 1

    for i in range(len(left)):
        if fermionIndex == i:
            matrixElement *= delta(left[i], right[i] + 1)
        else:
            matrixElement *= delta(left[i], right[i])

    return matrixElement


def creationOperatorMatricesSet(numberOfPaticles, stateVectorSet):
    '''
    create a set of creation operators
    '''

    creationOperatorMatrixArray = []
    numberOfFermions = int(numberOfPaticles / 2)

    for fermionIndex in range(numberOfFermions):
        creationOperatorMatrix = mat([\
                [creationOperatorMatrixElement(fermionIndex, l, r) for l in stateVectorSet]\
                for r in stateVectorSet])

        # note: the two indices of each matrix are transversed as default,
        # so we need to transverse the indices again.
        creationOperatorMatrix = creationOperatorMatrix.T

        creationOperatorMatrixArray.append(creationOperatorMatrix)

    return creationOperatorMatrixArray


def annihilationOperatorMatrixElement(fermionIndex, leftStateVector, rightStateVector):
    '''
    annihilation operator on the Fock space

    fermionIndex: if its value is N, then Nth fermion will be annihilated.
    '''

    left = leftStateVector
    right = rightStateVector

    matrixElement = 1

    for i in range(len(left)):
        if fermionIndex == i:
            matrixElement *= delta(left[i], right[i] - 1)
        else:
            matrixElement *= delta(left[i], right[i])

    return matrixElement


def annihilationOperatorMatricesSet(numberOfPaticles, stateVectorSet):
    '''
    create a set of annihilation operators
    '''

    annihilationOperatorMatrixArray = []
    numberOfFermions = int(numberOfPaticles / 2)

    for fermionIndex in range(numberOfFermions):
        annihilationOperatorMatrix = mat([\
                [annihilationOperatorMatrixElement(fermionIndex, l, r) for l in stateVectorSet]\
                for r in stateVectorSet])

        # note: the two indices of each matrix are transversed as default,
        # so we need to transverse the  indices again.
        annihilationOperatorMatrix = annihilationOperatorMatrix.T

        annihilationOperatorMatrixArray.append(annihilationOperatorMatrix)

    return annihilationOperatorMatrixArray


def main():
    numberOfPaticles = 4

    stateVectors = stateVectorSet(numberOfPaticles)
    print("annihilationOperatorMatricesSet")
    print(*annihilationOperatorMatricesSet(numberOfPaticles, stateVectors))
    print("creationOperatorMatricesSet")
    print(*creationOperatorMatricesSet(numberOfPaticles, stateVectors))

if __name__ == '__main__':
    main()

