import matplotlib.pyplot as plt
from ConformalTwoPointFunc import betaArray

dataArray = []

for beta in betaArray:
    fileName = "conformalTwoPointFuncWithBeta{}.txt".format(beta)

    with open(fileName, "r") as f:
        data = [float(k[:-1]) for k in f.readlines()[:-1]]
        dataArray.append(data)

with open("theta.txt", "r") as f:
    theta = [float(k[:-1]) for k in f.readlines()[:-1]]

plt.grid(True)
for data in dataArray:
    plt.plot(theta, data)
plt.xlim(0, max(theta))
plt.ylim(0, 1)
plt.show()
