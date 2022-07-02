# Ben Walker, baw3hg

def instructors(department):
    '''
    This function returns an alphebetized list of all instructors in a given department.
    :param department: This is the department in which instructor are chosen.
    :return: The return is the list of all instructors.
    '''
    from urllib.request import urlopen
    # opens the file
    u = urlopen("http://cs1110.cs.virginia.edu/files/louslist/" + department)

    biglist = []
    # for every line of the file it will make a string of just the instructor name
    for line in u:
        line = str(line)
        linenumber = line.index("|")
        line = line[linenumber + 1:]
        linenumber = line.index("|")
        line = line[linenumber + 1:]
        linenumber = line.index("|")
        line = line[linenumber + 1:]
        linenumber = line.index("|")
        line = line[linenumber + 1:]
        linenumber = line.index("|")
        line = line[:linenumber]
        linenumber = line.find("+")
        # if the instructor name has a + it gets rid of it
        if linenumber > -1:
            line = line[:linenumber]
        # the list adds every new instructor and then sorts it
        biglist.append(line)
        biglist.sort()
        # list is turned into a dict and then a list again to get rid of duplicates
        biglist = list(dict.fromkeys(biglist))
    u.close()

    return biglist


def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    '''
    This function searches all classes of a given department using different
    search parameters.
    :param dept_name: Given department to search from.
    :param has_seats_available: If the class still has open seats to enroll.
    :param level: The difficulty level of the class.
    :param not_before: Classes that start before this time are not included.
    :param not_after: Classes that start after this time are not included.
    :return: The classes that meet all of the requirements.
    '''

    from urllib.request import urlopen
    # opens the file
    u = urlopen("http://cs1110.cs.virginia.edu/files/louslist/" + dept_name)
    # every line in the file is put into a list
    biglist = u.readlines()
    # only does this if statement if the parameter is True
    if has_seats_available is True:
        # condenses the list to all classes with available seats
        for i in range(0, len(biglist)):
            line = str(biglist[i])
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            # this is the amount currently enrolled
            firstline = line[:linenumber]

            line = line[linenumber + 1:]
            linenumber = line.index("\\")
            line = line[:linenumber]
            # this is the amount allowed to enroll
            secondline = line
            # if a class has no seats available it is turned into a string called 'remove'
            if int(firstline) >= int(secondline):
                biglist[i] = 'remove'
        # all duplicate "'remove'" are made into one element
        biglist = list(dict.fromkeys(biglist))
        # the one remove is removed
        biglist.remove('remove')
    # if the level parameter is included this if statement runs
    if level is not None:
        level = str(level)
        # finds the given thousands digit of the class
        level = level[0:1]
        # condenses the list into only classes with the same thousands leve
        for i in range(0, len(biglist)):
            line = str(biglist[i])
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[:linenumber]
            # if the thousands level is different, the class is turned into
            # a string titled "'remove'"
            if str(line[0:1]) != str(level):
                biglist[i] = 'remove'
        # all duplicate "'remove'" are made into one element
        biglist = list(dict.fromkeys(biglist))
        # the one remove is removed
        biglist.remove('remove')
    # if this parameter is included then the if statement runs
    if not_before is not None:
        not_before = int(not_before)
        # condenses the list to only classes taking place on this time or after
        for i in range(0, len(biglist)):
            line = str(biglist[i])
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[:linenumber]
            # turns a class not with the right requirement into a string 'remove'
            if int(line) < not_before:
                biglist[i] = 'remove'
        # get rid of all duplicate 'remove'
        biglist = list(dict.fromkeys(biglist))
        # remove the remove if there are any
        if 'remove' in biglist:
            biglist.remove('remove')
    # if this parameter is included then the if statement runs
    if not_after is not None:
        not_after = int(not_after)
        # condenses the class list into only classes that meet the parameter
        for i in range(0, len(biglist)):
            line = str(biglist[i])
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[linenumber + 1:]
            linenumber = line.index("|")
            line = line[:linenumber]
            # if the time of the class takes place after the given time
            # it is turned into a string 'remove'
            if int(line) > not_after:
                biglist[i] = 'remove'
        # all duplicate 'remove' is removed
        biglist = list(dict.fromkeys(biglist))
        # if there are any 'remove' it is removed
        if 'remove' in biglist:
            biglist.remove('remove')
    # takes the final list and then strips the b' and \n'
    # then it splits the class pieces using the "|" character
    for i in range(0, len(biglist)):
        line = str(biglist[i])
        line = line.strip("b'")
        line = line.strip("\\n'")
        line = line.split("|")
        biglist[i] = line

    return biglist
