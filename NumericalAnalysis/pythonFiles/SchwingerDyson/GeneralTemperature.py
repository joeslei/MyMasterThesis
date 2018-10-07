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


def theta(numOfParticles, beta=1):
    return [np.pi * k / numOfParticles / beta for k in range(numOfParticles + 1)]


def twoPointFunction(theta, beta=1, J=50, q=4, x=0.5):
    """
    theta = a coordinate of the two point function
    beta = the inverse of a temperature
    J = the scale of the random coupling tensor
    q = the number of the interacting particles
    x = the speed of convergence of the Fourier series of the two point function
    """

    # The initial two point function is the free one.
    result = [0.5 * k for k in sgn(theta)]
    object = [1j * k for k in result]
    transformedTwoPointFunction = inverseDiscreteSineTransform(object)

    cnt = 0

    while True:
        previousTwoPointFunction = result[:]

        selfEnergy = [J * J * (k ** (q - 1)) for k in result]
        object = [1j * k for k in selfEnergy]
        transformedSelfEnergy = inverseDiscreteSineTransform(object)

        nextTransformedTwoPointFunction = []
        for n in range(len(transformedSelfEnergy)):
            omega = 2 * np.pi * (n + 0.5) / beta
            term1 = x / (- 1j * omega - transformedSelfEnergy[n])
            term2 = (1 - x) * transformedTwoPointFunction[n]
            nextTransformedTwoPointFunction.append(term1 + term2)

        transformedTwoPointFunction = nextTransformedTwoPointFunction[:]
        object = [-1j * k for k in transformedTwoPointFunction]
        result = discreteSineTransform(object)

        if isConvergentEnough(previousTwoPointFunction, result):
            print("The two point function was convergent enough at cnt = {}".format(cnt))
            break

        cnt += 1

    result = [k.real for k in result]

    return {"twoPointFunction": result, "selfEnergy": selfEnergy}


def main():
    # ---------------------------------
    # constant parameters of the system
    # ---------------------------------
    # Number of particles
    numOfParticles = 2 ** 15
    # The inverse of a temperature
    beta = 0.5

    # the real space
    thetaValue = theta(numOfParticles, beta)

    result = twoPointFunction(thetaValue, beta)
    result = result["twoPointFunction"]
    result = list(result[:-1:]) + list(result[-1::-1])

    thetaValue = [np.pi * k / numOfParticles for k in range(2 * numOfParticles + 1)]

    # -------------------------------------
    # Conformal Two Point Function
    # -------------------------------------

    delta = 1.0 / 4.0
    J = 50
    b = pow((0.5 - delta) * np.tan(np.pi * delta) / (J * J * np.pi), delta)
    conformalTwoPointFunc = []
    for k in range(len(thetaValue)):
        if k == 0 or k == len(thetaValue) - 1:
            conformalTwoPointFunc.append(1)
        else:
            component = b * pow(np.pi / np.sin(thetaValue[k] * 0.5), 2 * delta)
            conformalTwoPointFunc.append(component)

    plt.grid(True)
    plt.plot(thetaValue, result, "b")
    plt.plot(thetaValue, conformalTwoPointFunc, "g")
    plt.xlim(0, 6.3)
    plt.ylim(0, 0.6)
    plt.show()


if __name__ == "__main__":
    main()