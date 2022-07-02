# Ben Walker, baw3hg
def check(card_number):

    """
    This program takes a given integer value and checks whether or not
    it is a valid credit card number.

    :param card_number: This is the given card number
    :return: Boolean of whether or not the number is valid
    """

    card_number = int(card_number)
    first_sum = 0
    digitsum = 0
    card_number_list = list(map(int, str(card_number)))

    # finds the sum of every other number starting from the right
    for i in range(0, int((len(card_number_list) / 2) + (len(card_number_list) % 2))):
        i = i * 2
        first_sum = card_number_list[len(card_number_list) - 1 - i] + first_sum

    # if the length of the card number is even, doubles all odd indexes
    if len(card_number_list) % 2 == 0:
        for i in range(0, int(len(card_number_list) / 2)):
            i = i * 2
            card_number_list[i] = card_number_list[i] * 2

        # finds the sum of the double digit numbers
        for i in range(0, int(len(card_number_list) / 2)):
            i = i * 2
            number = card_number_list[i]
            while number > 0:
                remainder = number % 10
                digitsum = digitsum + remainder
                number = int(number / 10)
        # if total is divisible by 10, it is true
        return (digitsum + first_sum) % 10 == 0

    # if the length of the card number is odd, doubles all the even indexes
    if len(card_number_list) % 2 == 1:
        for i in range(0, int(len(card_number_list) / 2)):
            i = i * 2 + 1
            card_number_list[i] = card_number_list[i] * 2
        # finds the sum of the double digit numbers
        for i in range(0, int(len(card_number_list) / 2)):
            i = i * 2 + 1
            number = card_number_list[i]
            while number > 0:
                remainder = number % 10
                digitsum = digitsum + remainder
                number = int(number / 10)
        # if total is divisible by 10, it is true
        return (digitsum + first_sum) % 10 == 0
