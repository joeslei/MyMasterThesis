import numpy as np
import matplotlib.pyplot as plt


def partitionFunction(beta, time, eigenEnergies):
    return sum([np.exp(-(beta + 1j * time) * energy) for energy in eigenEnergies])


def getDataSet():
    i = 0
    numberOfParticles = 12
    dataSet = []
    while True:
        try:
            fileName = "eigenValueData/eigenValueWith{}Particles_{}.txt".format(numberOfParticles, i)
            with open(fileName, "r") as f:
                dataSet.append([float(data[:-1]) for data in f.readlines()])
            i += 1
        except FileNotFoundError as err:
            print("All data input: DONE")
            break

    return dataSet


def averagedNumerator(dataSet, beta, time):
    N = len(dataSet)
    s = []
    for data in dataSet:
        Z = partitionFunction(beta, time, data)
        s.append(Z * Z.conjugate())

    return sum(s) / N


def averagedDenumerator(dataSet, time):
    N = len(dataSet)
    s = []
    for data in dataSet:
        Z = partitionFunction(0, time, data)
        s.append(Z)

    return (sum(s) / N) ** 2


def spectrumFormFactor(dataSet, beta, timeArray):
    result = []
    for time in timeArray:
        g = averagedNumerator(dataSet, beta, time) / averagedDenumerator(dataSet, time)
        result.append(g)

    return result


if __name__ == "__main__":
    time = [i for i in range(10 ** 4)]
    g = spectrumFormFactor(getDataSet(), beta=5, timeArray=time)

    plt.plot(time, g)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()
