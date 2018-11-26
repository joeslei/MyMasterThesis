import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dst
from scipy.optimize import curve_fit
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


def fittingFunc(x, a, b):
    func = x ** (a) + b
    return func


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

omega = [2 * np.pi * (n + 0.5) for n in range(len(transformedSelfEnergy))]
transformedSelfEnergy = [k.imag for k in transformedSelfEnergy]

with open("dataFiles/omega.txt", "w") as f:
    f.write("\n".join(list(map(str, omega))))
with open("dataFiles/transformedSelfEnergy.txt", "w") as f:
    f.write("\n".join(list(map(str, transformedSelfEnergy))))

popt, pcov = curve_fit(fittingFunc, omega, transformedSelfEnergy)

fitting_data = []
for o in omega:
    fitting_data.append(fittingFunc(o, *popt))

plt.plot(omega, transformedSelfEnergy, 'b', label="transformedSelfEnergy")
plt.plot(omega, fitting_data, 'y', label="x ** {} + {}".format(popt[0], popt[1]))
plt.legend()
plt.xlabel("omega")
plt.title("beta = {}, J = {}".format(beta, J))
plt.show()
