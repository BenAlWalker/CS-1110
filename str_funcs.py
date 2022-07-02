# Ben Walker, baw3hg
import random


def ellipsis(s):
    a = s[0:2]
    b = s[len(s) - 2:len(s)]
    c = a + "..." + b
    return c


def eighteen(s):
    a = str(len(s) - 2)
    b = s[0]
    c = s[len(s) - 1:len(s)]
    d = b + a + c
    return d


def allit(s, t):
    a = s[0]
    b = t[0]
    a = a.lower()
    b = b.lower()
    if a and b == "a":
        return False
    elif a and b == "e":
        return False
    elif a and b == "i":
        return False
    elif a and b == "o":
        return False
    elif a and b == "u":
        return False
    else:
        return a == b


def between(a, b):
    c = a.count(b)
    if c < 2:
        return " "
    else:
        d = len(b)
        e = a.find(b)
        f = a[e + d:len(a)]
        g = f.find(b)
        h = f[0:g]
        return h


def rbetween(a, b):
    c = a.count(b)
    if c < 2:
        return " "
    else:
        d = len(b)
        e = a.rfind(b)
        a = a[1:e]
        g = a.rfind(b)
        h = a[g + d:len(a)]
    return h


def rand_between(a, b):
    num = random.randint(0, 1)
    if num == 0:
        c = a.count(b)
        if c < 2:
            return " "
        else:
            d = len(b)
            e = a.find(b)
            f = a[e + d:len(a)]
            g = f.find(b)
            h = f[0:g]
            return h
    else:
        c = a.count(b)
        if c < 2:
            return " "
        else:
            d = len(b)
            e = a.rfind(b)
            a = a[1:e]
            g = a.rfind(b)
            h = a[g + d:len(a)]
            return h
