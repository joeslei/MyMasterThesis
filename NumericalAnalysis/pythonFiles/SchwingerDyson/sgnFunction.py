from numpy import linspace


def sgn(x):
    '''
    return the signatures of each component of x
    '''

    result = []
    for i in x:
        if i > 0:
            result.append(1)
        elif i < 0:
            result.append(-1)
        else:  # i = 0
            result.append(0)

    return result


def main():
    x = linspace(0, 5, 10)
    print(10 * sgn(x))


if __name__ == '__main__':
    main()
