import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dst
from sgnFunction import sgn


def discreteSineTransform(array):
    result = dst(array, type=2)

    return result


def inverseDiscreteSineTransform(array):
    # normalization factor
    f = np.sqrt(1.0 / (2 * len(array)))
    g = np.sqrt(1.0 / (4 * len(array)))

    result = dst(array, type=3)
    result = [result[0] * g * g] + [k * f * f for k in result[1:]]

    return result


def isConvergentEnough(previousArray, nextArray, epsilon=0.0001):
    array = [abs(nextArray[n] - previousArray[n]) ** 2 for n in range(len(previousArray))]
    return sum(array) < epsilon


# ---------------------------------
# constant parameters of the system
# ---------------------------------
# The inverse temperature; we set its value to one for simplicity
beta = 1
# The scale of the random coupling tensor
J = 50
# Number of particles
numOfParticles = 2 ** 15
# Number of the interacting particles
q = 4


# The speed of convergence of the Fourier series of the two point function
x = 1.0 / 2

# the real space__
theta = [np.pi * k / numOfParticles for k in range(numOfParticles + 1)]


# -------------------------------------------
# Now let's iterate the Schwinger Dyson eq.
# -------------------------------------------

# The initial two point function is the free one.
twoPointFunction = [0.5 * k for k in sgn(theta)]
object = [1j * k for k in twoPointFunction]
transformedTwoPointFunction = inverseDiscreteSineTransform(object)

cnt = 0

while True:
    previousTwoPointFunction = twoPointFunction[:]

    selfEnergy = [J * J * (k ** (q - 1)) for k in twoPointFunction]
    object = [1j * k for k in selfEnergy]
    transformedSelfEnergy = inverseDiscreteSineTransform(object)

    nextTransformedTwoPointFunction = []
    for n in range(len(transformedSelfEnergy)):
        omega = 2 * np.pi * (n + 0.5)
        term1 = x / (- 1j * omega - transformedSelfEnergy[n])
        term2 = (1 - x) * transformedTwoPointFunction[n]
        nextTransformedTwoPointFunction.append(term1 + term2)

    transformedTwoPointFunction = nextTransformedTwoPointFunction[:]
    object = [-1j * k for k in transformedTwoPointFunction]
    twoPointFunction = discreteSineTransform(object)

    if isConvergentEnough(previousTwoPointFunction, twoPointFunction):
        print("The two point function was convergent enough at cnt = {}".format(cnt))
        break

    cnt += 1

x = [np.pi * k / numOfParticles for k in range(2 * numOfParticles + 1)]
y = list(twoPointFunction[:-1:]) + list(twoPointFunction[-1::-1])
plt.grid(True)
plt.plot(x, y)
plt.show()
