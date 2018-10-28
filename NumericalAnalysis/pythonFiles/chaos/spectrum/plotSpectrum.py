import numpy as np
import matplotlib.pyplot as plt


def plotSpectrum(distribution):
    distributionSize = len(distribution)
    line = [-0.3, 0, 0.3]

    previousSpectrum = distribution[0]
    for i in range(distributionSize):
        if i == 0:
            spectrum = previousSpectrum
        else:
            spectrum = distribution[i] + previousSpectrum
            previousSpectrum += distribution[i]

        spectrumLine = [spectrum for _ in range(len(line))]
        plt.plot(line, spectrumLine, color="k")

    plt.xlim(-1, 1)
    plt.show()


def main():
    distributionSize = 50
    poissonDistribution = np.random.poisson(lam=1, size=distributionSize)
    plotSpectrum(poissonDistribution)


if __name__ == "__main__":
    main()
