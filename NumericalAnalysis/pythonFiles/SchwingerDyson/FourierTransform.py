import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft


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
    array = [1 for _ in range(len(x))]
    transformedArray = fft(array)
    inverseTransformedArray = ifft(transformedArray)

    plt.plot(x, array)
    # plt.plot(x, transformedArray, 'r')
    plt.plot(x, inverseTransformedArray, 'g')
    plt.show()


if __name__ == '__main__':
    main()
