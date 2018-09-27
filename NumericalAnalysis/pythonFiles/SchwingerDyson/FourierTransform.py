import numpy as np
import matplotlib.pyplot as plt


def fourierTransform(array):
    N = len(array)
    result = []

    for k in range(N):
        fourierComponents = []
        for i in range(N):
            fourierComponent = array[i] * np.exp(1j * i * k / N)
            fourierComponents.append(fourierComponent)
        result.append(sum(fourierComponents))

    return result


def inverseFourierTransform(array):
    N = len(array)
    result = []

    for k in range(N):
        fourierComponents = []
        for i in range(N):
            fourierComponent = array[i] * np.exp(-1j * i * k / N)
            fourierComponents.append(fourierComponent)
        result.append(sum(fourierComponents) / N / np.pi)

    return result


def main():
    x = np.linspace(0, 2 * np.pi, 100, endpoint=True)
    array = np.sin(x)
    transformedArray = fourierTransform(array)
    inverseTransformedArray = inverseFourierTransform(transformedArray)

    plt.plot(x, array)
    # plt.plot(x, transformedArray)
    plt.plot(x, inverseTransformedArray)
    plt.show()


if __name__ == '__main__':
    main()
