import numpy as np
import matplotlib.pyplot as plt
import scipy.special


def randomCouplingTensor(numberOfParticles):
    N = numberOfParticles
    np.random.seed

    # Initialize the tonsor with zeros
    J = np.zeros((N, N, N, N))

    # assign a random number for each component of the tensor
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    J[a, b, c, d] = np.random.normal(0, np.sqrt(6.0 / (N * N * N))) / scipy.special.factorial(4)

    # Make the tensor be totally anti-symmetric
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    if a == b or a == c or a == d or b == c or b == d or c == d:
                        J[a, b, c, d] = int(0)
                    if a < b < c < d:
                        J[a, b, d, c] = -J[a, b, c, d]
                        J[a, c, b, d] = -J[a, b, c, d]
                        J[a, d, c, b] = -J[a, b, c, d]

                        J[b, a, c, d] = -J[a, b, c, d]
                        J[b, c, d, a] = -J[a, b, c, d]
                        J[b, d, a, c] = -J[a, b, c, d]

                        J[c, a, d, b] = -J[a, b, c, d]
                        J[c, b, a, d] = -J[a, b, c, d]
                        J[c, d, b, a] = -J[a, b, c, d]

                        J[d, a, b, c] = -J[a, b, c, d]
                        J[d, b, c, a] = -J[a, b, c, d]
                        J[d, c, a, b] = -J[a, b, c, d]

                        J[a, c, d, b] = J[a, b, c, d]
                        J[a, d, b, c] = J[a, b, c, d]

                        J[b, a, d, c] = J[a, b, c, d]
                        J[b, c, a, d] = J[a, b, c, d]
                        J[b, d, c, a] = J[a, b, c, d]

                        J[c, a, b, d] = J[a, b, c, d]
                        J[c, b, d, a] = J[a, b, c, d]
                        J[c, d, a, b] = J[a, b, c, d]

                        J[d, a, c, b] = J[a, b, c, d]
                        J[d, b, a, c] = J[a, b, c, d]
                        J[d, c, b, a] = J[a, b, c, d]

    return J


def main():
    numberOfParticles = 30
    data = []
    J = randomCouplingTensor(numberOfParticles)
    for a in range(numberOfParticles):
        for b in range(a + 1, numberOfParticles):
            for c in range(b + 1, numberOfParticles):
                for d in range(c + 1, numberOfParticles):
                    data.append(J[a, b, c, d])

    plt.hist(data, bins=100)
    plt.show()


if __name__ == '__main__':
    main()
