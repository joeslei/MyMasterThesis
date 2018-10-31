import numpy as np
import matplotlib.pyplot as plt


def GOE_P(s):
    return np.pi * 0.5 * s * np.exp(-np.pi * s * s / 4)


def GUE_P(s):
    return 32 / np.pi / np.pi * s * s * np.exp(-4 * s * s / np.pi)


def main():
    s = np.linspace(0, 3.5, 100, endpoint=True)

    plt.plot(s, GOE_P(s), color="b")
    plt.plot(s, GUE_P(s), color="g")
    plt.xlim(0, 3.5)
    plt.ylim(0, 1)
    plt.grid(True)
    plt.title("GOE: blue, GUE: green")
    plt.show()


if __name__ == "__main__":
    main()
