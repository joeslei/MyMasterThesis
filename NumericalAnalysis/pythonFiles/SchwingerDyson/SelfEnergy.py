import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dst
from sgnFunction import sgn


def discreteSineTransform(array):
    result = dst(array, type=2)

    return result


def inverseDiscreteSineTransform(array):
    # normalization factor
    f = 1.0 / (2 * len(array))

    result = dst(array, type=3)
    result = [k * f for k in result]

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
# Anomalous dimension
delta = 1.0 / q


# The speed of convergence of the Fourier series of the two point function
x = 1.0 / 2

# the real space
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

selfEnergy = [k.real for k in selfEnergy]

theta = [np.pi * k / numOfParticles for k in range(2 * numOfParticles + 1)]
selfEnergy = list(selfEnergy[:-1:]) + list(selfEnergy[-1::-1])

# corresponds to J = 50
v = 0.94625
selfEnergyLarge_q = []
for t in theta:
    selfEnergyLarge_q.append((np.pi * v / (2 * np.cos(np.pi * v / 2 * (1 - t / np.pi)))) ** 2)

plt.plot(theta, selfEnergy, 'b', label="selfEnergy")
plt.plot(theta, selfEnergyLarge_q, 'g', label="selfEnergyLarge_q")
plt.legend()
plt.show()
