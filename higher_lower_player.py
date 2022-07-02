# Ben Walker, baw3hg

'''
Higher - lower games that has the computer guess the number
'''



print("Think of a number between 1 and 100 and I'll guess it.")
guesscount = int(input("How many guesses do I get? "))


def guess(x, y):
    """
    Creates a guess that is the mean of two bounds
    :param x: lower bound
    :param y: upper bound
    :return: this is the mean of the two numbers
    """
    a = int(x)
    b = int(y)
    z = int((a + b) / 2)
    return z


lowbound = 1
highbound = 100

compguess = guess(lowbound, highbound)

while guesscount > 1:
    if highbound > 100:
        highbound = 100
    if lowbound > 100:
        lowbound = 100
    compguess = guess(lowbound, highbound)

    answer = input("Is the number higher, lower, or the same as " + str(compguess) + "? ")
    print(lowbound, highbound)
    if answer == 'same':
        print("I won!")
        break

    elif answer == 'lower':
        if highbound - lowbound < 10:
            if highbound - 1 < lowbound:
                print("Wait; how can it be both higher than " + str(compguess - 1) + " and lower than " + str(
                    compguess) + "?")
                break
        elif highbound - 1 < lowbound:
            print("Wait; how can it be both lower than " + str(compguess) + " and higher than " + str(
                compguess - 1) + "?")
            break

        highbound = (highbound - lowbound) // 2 + lowbound - 1
        guesscount = guesscount - 1
        continue

    elif answer == 'higher':
        if highbound - lowbound < 10:
            if lowbound + 1 > highbound:
                print("Wait; how can it be both higher than " + str(compguess) + " and lower than " + str(
                    compguess + 1) + "?")
                break
        elif lowbound + 1 > highbound:
            print("Wait; how can it be both higher than " + str(compguess - 1) + " and lower than " + str(
                compguess + 1) + "?")
            break

        lowbound = (highbound - lowbound) // 2 + lowbound + 1
        if compguess == 99:
            lowbound = 100
            highbound = 100
        guesscount = guesscount - 1
        continue

if guesscount == 1:

    compguess = guess(lowbound, highbound)
    answer = input("Is the number higher, lower, or the same as " + str(compguess) + "? ")
    if answer == 'same':
        print("I won!")
    else:
        lose = int(input("I lost; what was the answer? "))
        if lose > 50 and compguess <= 50:
            print("That can't be; you said it was lower than 50!")
        elif lose < 50 and compguess >= 50:
            print("That can't be; you said it was higher than 50!")
        else:
            print("Well played!")
