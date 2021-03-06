import numpy as np
import matplotlib.pyplot as plt


def potentialPrime(x, K):
    return K / (2 * np.pi) * np.sin(2 * np.pi * x)


def main():
    numberOfLoops = 3000

    initialMomentum = np.linspace(start=0, stop=1, num=50, endpoint=True)
    initialMomentum = [0.02 * i for i in range(16)]
    initialMomentum += [0.03 * i for i in range(10, 23)]
    initialMomentum += [0.02 * i for i in range(35, 51)]
    initialPosition = [0, 1]

    chaosIntensities = np.linspace(start=0, stop=8, num=100, endpoint=True)
    i = 0

    plt.figure(figsize=(3, 3), dpi=200)

    for K in chaosIntensities:
        print(i)
        plt.cla()
        for p0 in initialMomentum:
            for x0 in initialPosition:
                x = [x0]
                p = [p0]
                xn = x0
                pn = p0

                for _ in range(numberOfLoops):
                    pn = pn - potentialPrime(xn, K)
                    xn = xn + pn

                    if xn < 0:
                        if xn < -1:
                            xn = 1 - xn % 1
                        else:
                            xn = 1 - np.abs(xn)
                    if xn > 1:
                        xn = xn % 1

                    x.append(xn)
                    p.append(pn)

                fileName = "data/x_with_x0_{}_and_p0_{}.txt".format(x0, p0)
                with open(fileName, "w") as f:
                    f.write("\n".join([str(xn) for xn in x]))
                fileName = "data/p_with_x0_{}_and_p0_{}.txt".format(x0, p0)
                with open(fileName, "w") as f:
                    f.write("\n".join([str(pn) for pn in p]))

        for p0 in initialMomentum:
            for x0 in initialPosition:

                fileName = "data/x_with_x0_{}_and_p0_{}.txt".format(x0, p0)
                with open(fileName, "r") as f:
                    x = [float(xn[:-1]) for xn in f.readlines()]
                fileName = "data/p_with_x0_{}_and_p0_{}.txt".format(x0, p0)
                with open(fileName, "r") as f:
                    p = [float(pn[:-1]) for pn in f.readlines()]

                plt.scatter(x, p, color='k', marker='o', s=1)

        plt.title("K = {}".format(K))
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.savefig("fig/figure{}.png".format(i))
        i += 1


if __name__ == "__main__":
    main()
