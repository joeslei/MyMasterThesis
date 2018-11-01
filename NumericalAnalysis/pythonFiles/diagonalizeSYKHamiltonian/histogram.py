import numpy as np
import matplotlib.pyplot as plt
from DiagonalizeHamiltonian import diagonalizeHamiltonian


def histogram(data, bins=10, showHist=True):
    maxValue = max(data)
    minValue = min(data)
    binWidth = (maxValue - minValue) / float(bins)
    valueCells = [minValue + i * binWidth for i in range(bins + 1)]
    result = [0 for _ in range(len(valueCells))]

    for d in data:
        for cellIndex in range(len(valueCells) - 1):
            if valueCells[cellIndex] <= d < valueCells[cellIndex + 1]:
                result[cellIndex] += 1

    if showHist:
        cells = []
        for cellIndex in range(len(valueCells) - 1):
            cells += [valueCells[cellIndex], valueCells[cellIndex + 1]]
        res = []
        for resultIndex in range(len(valueCells) - 1):
            res += [result[resultIndex], result[resultIndex]]
        plt.plot(cells, res)
        plt.xlim(min(cells) - 1, max(cells) + 1)
        plt.ylim(0, max(res) + 3)
        plt.show()

    return result


def main():
    data = np.random.normal(size=5000)
    histogram(data, bins=50, showHist=True)


if __name__ == "__main__":
    main()
