def shiftN(stringvalue, direction, N):
    if not stringvalue:
        return stringvalue
    N = N % len(stringvalue)
    if direction == 0:
        return stringvalue[N:] + stringvalue[N:]
    elif direction == 1:
        return stringvalue[-N:] + stringvalue[:-N]


def main():
    str = '001100'
    print(int(str, 2))
    rstr = shiftN(str, 0, 2)
    print(rstr)
    print(int(rstr, 2))

    rstr = '110000'
    rstr = shiftN(rstr, 1, 4)
    print(rstr)
    print(int(rstr, 2))


if __name__ == '__main__':
    main()
