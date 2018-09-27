import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft  # for Fast Fourier Transform
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
n = 100

theta_min = 0
theta_max = 6
delta_theta = (theta_max - theta_min) / n
theta = [theta_min + i * delta_theta for i in range(n + 1)]
t = [beta * i / 2 / np.pi for i in theta]

# a parameter for making the correlator be convergence
x = 1 / 4.0


def freeTwoPointFunction(t):
    return [0.5 * i for i in sgn(t)]


# the initial two point function
twoPointFunction = freeTwoPointFunction(t)
# the Fourier transformed initial two point function
transformedTwoPointFunction = fft(twoPointFunction)

difference = []
for i in range(1000):
    # the self energy in the time-coordinate
    selfEnergy = [(J ** 2) * (i ** (q - 1)) for i in twoPointFunction]
    # the Fourier transformed self energy
    transformedSelfEnergy = fft(selfEnergy)

    # the next transformed two point function
    nextTransformedTwoPointFunction = []
    for omega in range(n + 1):
        term1 = (1 - x) * transformedTwoPointFunction[omega]
        term2 = x / (-1j * omega / 2 / np.pi - transformedSelfEnergy[omega])
        nextTransformedTwoPointFunction.append(term1 + term2)
    transformedTwoPointFunction = nextTransformedTwoPointFunction[:]
    # the next two point function
    twoPointFunction = ifft(transformedTwoPointFunction)


plt.plot(t[1:], twoPointFunction[1:])
plt.show()
