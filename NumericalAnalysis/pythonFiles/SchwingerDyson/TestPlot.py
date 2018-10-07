import matplotlib.pyplot as plt
from SchwingerDyson import J


with open("theta.txt", "r") as f:
    theta = [float(k) for k in f.readlines().split("\n")]

dataNameForTwoPointFunc = "twoPointFunctionDataWithJ{}.txt".format(J)
with open(dataNameForTwoPointFunc, "r") as f:
    twoPointFunction = [float(k) for k in f.readlines().split("\n")]

plt.plot(theta, twoPointFunction)
plt.show()
