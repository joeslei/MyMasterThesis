import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg


# -------------------------------
# parameters of the theory
# -------------------------------
numberOfParticles = 20      # The number of particles
beta = 5                    # The inversed temperature of the system
numberOfStates = int(2 ** (numberOfParticles / 2))  # The dimension of the Hilbert Space
numberOfSamples = 90        # The number of samples


def couplingTensor(numberOfParticles):
    '''
    This is the coupling tensor in the Hamiltonian of SYK model.
    Each component is a random real number chosen from a Gaussian
    distribution with zero mean and variance given by

        sigma^2 = 3! * J^2 / N^3

    where N is the number of particles and J is a constant.
    We set J = 1 for convenience.
    '''

    random.seed()

    mean = 0
    N = numberOfParticles
    sigma = 3 * 2 * 1 / N / N / N

    # Initialize the random coupling tensor with zeros
    randomTensor = np.zeros((N, N, N, N))

    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    randomTensor[a, b, c, d] = random.gauss(mean, sigma)

    return randomTensor


def disorderAverage(numberOfSamples, object):
    """
    Return the disorder-averaged "object".
    The variable "object" is a function which has random numbers as its variable.
    """

    sum = 0
    result = sum / numberOfStates

    return result
