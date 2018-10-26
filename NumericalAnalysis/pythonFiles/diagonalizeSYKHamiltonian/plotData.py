import matplotlib.pyplot as plt
from DiagonalizeHamiltonian import diagonalizeHamiltonian


def main():
    numberOfPaticles = 20
    numberOfSamples = 5

    # ---------------------------
    # Create a number of samples
    # ---------------------------
    dataList = []
    for n in range(numberOfSamples):
        print("------------------------")
        print("         n = {}".format(n))
        print("------------------------")
        eigenValue = diagonalizeHamiltonian(numberOfPaticles)["eigenValue"]
        eigenValue = [e.real for e in eigenValue]
        dataList.append(eigenValue)

    # ---------------------------
    # Average the values
    # ---------------------------
    result = []
    for dataIndex in range(len(dataList[0])):
        sum = 0
        for sampleIndex in range(numberOfSamples):
            sum += dataList[sampleIndex][dataIndex]
        result.append(float(sum) / numberOfSamples)

    plt.hist(result, bins=100)
    plt.show()


if __name__ == "__main__":
    main()
