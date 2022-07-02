# Ben Walker, baw3hg

def mymap(func, lst):
    """
    This function applies a single argument function to a list
    :param func: This is the single argument function
    :param lst: This is the given list
    :return: The list is then returned, having the function been applied to it
    """
    lst = list(lst)
    for i in range(0, int(len(lst))):
        lst[i] = func(lst[i])
    return lst


def myreduce(func, lst):
    """
    This function takes a two argument function and returns the total value
    after applying the function to the entire list
    :param func: This is the two argument function
    :param lst: This is the given list
    :return: The total value is returned
    """
    lst = list(lst)
    total = lst[0]
    for i in range(0, int(len(lst) - 1)):
        total = func(total, lst[i + 1])
    return total
