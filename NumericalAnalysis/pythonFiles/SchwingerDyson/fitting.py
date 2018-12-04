from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

with open("dataFiles/omega.txt", "r") as f:
    omega = list((map(float, f.readlines())))
with open("dataFiles/transformedSelfEnergy.txt", "r") as f:
    transformedSelfEnergy = list((map(float, f.readlines())))


def fitting_func(x, a, b):
    return a * (x ** b)


popt, pcov = curve_fit(fitting_func, omega, transformedSelfEnergy)

fitting_data = []
for o in omega:
    fitting_data.append(fitting_func(o, *popt))

print("fitting function = a * (x ** b)")
print("parameters   = {}".format(popt))
print("standard dev = {}".format(np.sqrt(np.diag(pcov))))


if 1:
    plt.plot(omega, transformedSelfEnergy, 'b', label="Sigma(omega)")
    plt.plot(omega, fitting_data, 'y', label="%5.3f * (x ** %5.3f)" % tuple(popt))
    plt.legend()
    plt.xscale("log")
    plt.yscale("log")
    plt.show()
