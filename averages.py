# Ben Walker, baw3hg

def mean(a, b, c):
    d = float((a + b + c) / 3)
    return d


def median(a, b, c):
    if a == b:
        return a
    elif b == c:
        return b
    elif a == c:
        return a

    elif b < a < c:
        return a
    elif b > a > c:
        return a

    elif a < b < c:
        return b
    elif a > b > c:
        return b

    elif a < c < b:
        return c
    elif a > c > b:
        return c


def rms(a, b, c):
    a = a ** 2
    b = b ** 2
    c = c ** 2
    d = mean(a, b, c)
    e = d ** (1 / 2)
    return e


def middle_average(a, b, c):
    d = mean(a, b, c)
    e = median(a, b, c)
    f = rms(a, b, c)
    g = median(d, e, f)
    return g
