import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft
from sgnFunction import sgn

# ---------------------------------
# constant parameters of the system
# ---------------------------------
# beta times J
betaTimesJ = 50
# the inverse of the temperature
beta = 5
# the average of the components of the random coupling tensor
J = betaTimesJ / beta
# the number of the interacting particles
q = 4
# the anomalous dimension
delta = float(1 / q)

# ---------------------------------------
# the coordinate i.e. time of the system
# ---------------------------------------
# the number of discrete components of time
n = 1000

theta_min = 0
theta_max = 10
theta = np.linspace(theta_min, theta_max, n, endpoint=True)
t = [beta * i / 2 / np.pi for i in theta]

# a parameter for making the correlator be convergence
# NOTE: the two point function does not depend on this parameter
x = 1.0 / 16


def freeTwoPointFunction(t):
    return [0.5 * i for i in sgn(t)]


# the initial two point function
twoPointFunction = freeTwoPointFunction(t)
# the Fourier transformed initial two point function
transformedTwoPointFunction = fft(twoPointFunction, norm="ortho")

for i in range(100000):
    if i % 2000 == 0:
        print(i)
    # the self energy in the time-coordinate
    selfEnergy = [(J ** 2) * (i ** (q - 1)) for i in twoPointFunction]
    # the Fourier transformed self energy
    transformedSelfEnergy = fft(selfEnergy, norm="ortho")

    # the next transformed two point function
    nextTransformedTwoPointFunction = []
    for i in range(len(t)):
        term1 = (1 - x) * transformedTwoPointFunction[i]
        term2 = x / (-1j * i / 2 / np.pi - transformedSelfEnergy[i])
        nextTransformedTwoPointFunction.append(term1 + term2)
    transformedTwoPointFunction = nextTransformedTwoPointFunction[:]
    # the next two point function
    twoPointFunction = ifft(transformedTwoPointFunction, norm="ortho")


plt.plot(t, twoPointFunction)
plt.show()
