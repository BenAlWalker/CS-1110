#Ben Walker, baw3hg
def creepy(x, y):
    x = int(x)
    y = int(y)
    lowerage = y / 2 + 7   #age bounds taken from PA03
    upperage = y * 2 - 13
    return x < lowerage or x > upperage