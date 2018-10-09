import numpy as np
import matplotlib.pyplot as plt

numOfParticles = 2 ** 15
theta = [np.pi * k / numOfParticles for k in range(2 * numOfParticles + 1)]

q = 4
delta = 1.0 / q
J = 50
betaArray = [1, 3, 7, 10, 20, 50]
dataArray = []

b = pow((0.5 - delta) * np.tan(np.pi * delta) / (J * J * np.pi), delta)


for beta in betaArray:

    conformalTwoPointFunc = []
    for k in range(len(theta)):
        if k == 0 or k == len(theta) - 1:
            conformalTwoPointFunc.append(0)
        else:
            component = b * pow(np.pi / (beta * np.sin(theta[k] * 0.5)), 2 * delta)
            conformalTwoPointFunc.append(component)

    dataArray.append(conformalTwoPointFunc)

plt.grid(True)
for data in dataArray:
    plt.plot(theta, data)
plt.xlim(0, max(theta))
plt.ylim(0, 0.8)
plt.show()
