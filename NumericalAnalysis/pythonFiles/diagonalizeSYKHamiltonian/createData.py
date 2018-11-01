from DiagonalizeHamiltonian import diagonalizeHamiltonian


def createData():
    numberOfParticles = 12
    numberOfDataFiles = 100
    for i in range(numberOfDataFiles):
        print("i = " + str(i))
        data = diagonalizeHamiltonian(numberOfParticles)["eigenValue"]
        data = [str(d.real) for d in data]
        fileName = "eigenValueData/eigenValueWith{}Particles_{}.txt".format(numberOfParticles, i)
        with open(fileName, "w") as f:
            f.write("\n".join(data))


if __name__ == '__main__':
    createData()
