def sgn(x):
    '''
    return the signature of x
    '''

    if x == 0:
        print("ERROR: the variable is zero")
        raise ValueError
    else:
        if x > 0:
            return 1
        else:
            return -1


def main():
    x = float(input("input a number: "))
    print("sgn({}) = {}".format(x, sgn(x)))


if __name__ == '__main__':
    main()

