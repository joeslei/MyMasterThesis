import numpy as np
from scipy import special


def generalized_assoc_laguerre(x, n, k):
    sum = np.linspace(0 + 0j, 0 + 0j, len(x))
    for i in range(n + 1):
        numerator = special.poch(-n, i) * special.poch(i + k + 1, n-i)
        denumerator = float(special.factorial(i))
        sum += numerator * (x ** i) / denumerator

    return sum / special.factorial(n)


if __name__ == '__main__':
    N = 2 ** 5
    beta = 5
    t = np.linspace(start=0, stop=100, num=10, endpoint=True)
    z_bar = (-beta - 1j * t) / np.sqrt(N)
    L = generalized_assoc_laguerre(-z_bar ** 2, N - 1, 1 - N)
    for l in L:
        print(l)
