import numpy as np
import matplotlib.pyplot as plt


def conformalTwoPointFunc(theta, beta=1, J=50, q=4):
    """
    theta: real coordinate
    beta: an inverse temperature
    J: the scale of the random coupling tensor
    q: the number of the interacting particles
    """
    result = []
    delta = 1.0 / q
    b = pow((0.5 - delta) * np.tan(np.pi * delta) / (J * J * np.pi), delta)
    for k in theta:
        component = b * pow(np.pi / (beta * np.sin(k * 0.5)), 2 * delta)
        result.append(component)

    return result


def main():
    numOfParticles = 2 ** 15
    theta = [np.pi * k / numOfParticles for k in range(2 * numOfParticles + 1)]

    plt.plot(theta, conformalTwoPointFunc(theta))
    plt.xlim(0, max(theta))
    plt.ylim(0, 0.7)
    plt.show()


if __name__ == "__main__":
    main()
