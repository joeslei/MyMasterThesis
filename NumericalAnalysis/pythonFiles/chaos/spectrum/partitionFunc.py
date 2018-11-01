import numpy as np
import scipy.linalg


def partitionFunc(matrix, time, beta=5):
    if type(time) in [np.ndarray, list]:
        Z = []
        if str in [type(t) for t in time]:
            print("ERROR: invalid type of time: str")
        else:
            for t in time:
                Z.append(np.trace(scipy.linalg.expm((-beta - 1j * t) * matrix)))
    elif type(time) in [int, float]:
        Z = np.trace(scipy.linalg.expm((-beta - 1j * time) * matrix))
    else:
        print("ERROR: invalid type of time: type(time) = {}".format(type(time)))
        return []

    return Z


def main():
    matrix = np.eye(3)
    t = "hohoh"
    print(partitionFunc(matrix, t))
    t = [0, 1, "hoge"]
    print(partitionFunc(matrix, t))


if __name__ == "__main__":
    main()
