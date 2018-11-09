import numpy as np
from generalized_assoc_laguerre import generalized_assoc_laguerre as L
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

    second_term = np.linspace(0 + 0j, 0 + 0j, len(t), endpoint=True)
    for i in range(N):
        a = z_bar * (((beta ** 2 - t ** 2 - 2j * beta * t) / (beta ** 2 + t ** 2)) ** (N - i))
        b = L(-z ** 2, i, N - i) * L(-z_bar ** 2, N - 1, i + 1 - N)
        second_term += 2 * (a * b).real
    second_term *= np.exp(0.5 * (z ** 2 + z_bar ** 2)) / (z + z_bar)

    return first_term - second_term


if __name__ == '__main__':
    N = 2 ** 5
    beta = 5
    time_range_scale = 3
    size_of_time_array = 10 ** (time_range_scale + 1)
    t = np.linspace(0, 10 ** time_range_scale, size_of_time_array, endpoint=True)
    zeros = np.linspace(0, 0, size_of_time_array, endpoint=True)
    denumerator = g_dis_numerator(zeros, beta, N)
    g_dis = g_dis_numerator(t, beta, N) / denumerator
    g_conn = g_conn_numerator(t, beta, N) / denumerator
    g = g_conn + g_dis
    plt.plot(t, g.real, label=r"RMT, $g(t), \beta={}, L={}$".format(beta, N))
    plt.legend(loc="upper right")
    # plt.plot(t, g_dis.real)
    # plt.plot(t, g_conn.real)
    # plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()
