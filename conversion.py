#Ben Walker, baw3hg

def c2f(temp):
    temp = float(temp)
    temp = temp * 9 * (1/5)    #
    # formula from Google: (0°C × 9/5) + 32
    temp = temp + 32
    return temp


def f2c(temp2):
    temp2 = float(temp2)
    temp2 = temp2 - 32
    temp2 = temp2 * 5 * (1/9)
    return temp2
