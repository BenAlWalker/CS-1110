# Ben Walker, baw3hg

def binop(equation):
    """
    binop returns the value of an equation
    even with spaces in between values
    Example: "12     +   2" returns 14

    :param equation: this is the given equation used

    :return: sum: this is the sum of two integers
           diff: this is the difference of two integers
           prod: this is the product of two integers
           quot: this is the quotient of two integers
    """

    a = equation.find('+')
    b = equation.find('-')
    c = equation.find('*')
    d = equation.find('/')

    if equation[a] == '+':
        int1 = int(equation[:a])
        int2 = int(equation[a+1:])
        sum = int1 + int2
        return sum
    elif equation[b] == '-':
        int1 = int(equation[:b])
        int2 = int(equation[b + 1:])
        diff = int1 - int2
        return diff
    elif equation[c] == '*':
        int1 = int(equation[:c])
        int2 = int(equation[c+1:])
        prod = int1 * int2
        return prod
    elif equation[d] == '/':
        int1 = int(equation[:d])
        int2 = int(equation[d+1:])
        quot = float(int1 / int2)
        return quot
