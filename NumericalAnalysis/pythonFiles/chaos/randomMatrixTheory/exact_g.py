import numpy as np
from scipy.special import assoc_laguerre as L
import matplotlib.pyplot as plt


def g_dis_numerator(t, beta, mat_size):
    N = mat_size
    z = (-beta + 1j * t) / np.sqrt(N)

    e = np.exp(0.5 * z * z)
    a = e * L(-z * z, N - 1, 1)
    numerator = (a * a.conjugate()).real

    return numerator


def g_conn_numerator(t, beta, mat_size):
    N = mat_size
    z = (-beta + 1j * t) / np.sqrt(N)
    z_bar = z.conjugate()

    first_term = np.exp(0.5 * (z + z_bar) * (z + z_bar))
    first_term *= L(-(z + z_bar) ** 2, N - 1, 1)

    second_term = np.linspace(0j, 0j, len(t))
    second_term += 0.0
    for i in range(N):
        print((z ** (N - i))[-1])
        a1 = 2 * (z ** (N - i)) * (z_bar ** (i + 1 - N))
        a2 = L(-z * z, i, N - i) * L(-z_bar * z_bar, N - 1, i + 1 - N)
        second_term += a1 * a2
    second_term *= np.exp(0.5 * (z ** 2 + z_bar ** 2)) / (z + z_bar)

    numerator = (first_term - second_term).real

    return numerator


if __name__ == '__main__':
    N = 2 ** 8
    beta = 5
    size_of_time_array = 10 ** 4
    t = np.linspace(0, 10 ** 3, size_of_time_array, endpoint=True)
    zeros = np.linspace(0, 0, size_of_time_array, endpoint=True)
    denumerator = g_dis_numerator(zeros, beta, N)
    # g_dis = g_dis_numerator(t, beta, N) / denumerator
    g_conn = g_conn_numerator(t, beta, N) / denumerator
    # g = g_conn + g_dis
    plt.plot(t, g_conn)
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()
