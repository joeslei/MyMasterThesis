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
J = 10
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

twoPointFunction = [k.real for k in twoPointFunction]

theta = [np.pi * k / numOfParticles for k in range(2 * numOfParticles + 1)]
twoPointFunction = list(twoPointFunction[:-1:]) + list(twoPointFunction[-1::-1])

# -------------------------------------
# Conformal Two Point Function
# -------------------------------------

b = pow((0.5 - delta) * np.tan(np.pi * delta) / (J * J * np.pi), delta)
conformalTwoPointFunc = []
for k in range(len(theta)):
    component = b * pow(np.pi / np.sin(theta[k] * 0.5), 2 * delta)
    conformalTwoPointFunc.append(component)


# -------------------------------------------------------------
# Correction from the conformal limit to the exact solution
# -------------------------------------------------------------

alpha = 2 * (q - 2) / (16 / np.pi + 6.18 * (q - 2) + (q - 2) ** 2)
f0 = [2 + (np.pi - abs(k)) / np.tan(abs(k) * 0.5) for k in theta]
approxTwoPointFunc = []
for k in range(len(theta)):
    correctingTerm = np.sqrt(pow(2, q - 1) / q) * alpha * f0[k]
    component = conformalTwoPointFunc[k] * (1 - correctingTerm / J)
    approxTwoPointFunc.append(component)

plt.title("two point functions with beta J = {}".format(J))
plt.plot(theta, twoPointFunction, color="b", label="exact two point func")
plt.plot(theta, conformalTwoPointFunc, color="g", label="conformal two point func")
# plt.plot(theta, approxTwoPointFunc, "r")
plt.xlabel("time")
plt.xlim(0, 6.3)
plt.ylim(0, 1)
plt.legend()
plt.show()

# -------------------------------------------------------------
# Calculate the sub-leading order of large J
# -------------------------------------------------------------
"""
cutOffIndex = 2 ** 12

theta = theta[cutOffIndex: 2 * numOfParticles - cutOffIndex]
twoPointFunction = twoPointFunction[cutOffIndex: 2 * numOfParticles - cutOffIndex]
approxTwoPointFunc = approxTwoPointFunc[cutOffIndex: 2 * numOfParticles - cutOffIndex]

subleadingTwoPointFunc = []
for k in range(len(theta)):
    component = J * J * (twoPointFunction[k] - approxTwoPointFunc[k])
    subleadingTwoPointFunc.append(component)

plt.grid(True)
plt.plot(theta, subleadingTwoPointFunc)
plt.title("Sub-leading order of two point function with $J = {}$".format(J))
plt.show()
"""
