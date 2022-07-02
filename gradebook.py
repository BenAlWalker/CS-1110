# Ben Walker, baw3hg


grades = {}
sectionweight = {}
sectiongrade = {}


def assignment(kind, grade=1, weight=1):
    """
    This function keeps track of the overall grade of each type of assignment,
    as well as the overall weight of each type of assignment. If the assignment is new to
    the grade book, then it is added in.
    :param kind: Type of assignment (i.e, exam, lab, hw)
    :param grade: The grade received
    :param weight: How much weight this given assignment has
    :return: Return is the overall grade on this type of assignment
    """
    # adds a new kind of assignment if it is not in the grades dictionary
    if kind not in grades:
        grades[kind] = grade * weight
        # adds the new grade in the grades dictionary
    else:
        grades[kind] = grades[kind] + (grade * weight)

    # adds the weight of a new type of assignment
    if kind not in sectionweight:
        sectionweight[kind] = weight
        # adds the weight of a known assignment
    else:
        sectionweight[kind] = sectionweight[kind] + weight

    # finds the grade for that kind of assignment

    sectiongrade[kind] = grades[kind] / sectionweight[kind]

    return sectiongrade[kind]


def total(proportions):
    """
    This function returns the overall grade in the class.
    :param proportions: This is a dict that holds the values of each type
    of assignment.
    :return: The overall grade in the class.
    """
    proportions = dict(proportions)
    finalgrade = 0
    # loops through each kind in the proportion dictionary,
    # and then finds the overall grade for that weighted section
    for kind in proportions.keys():
        if kind in sectiongrade:
            finalgrade = finalgrade + sectiongrade[kind] * proportions[kind]
    return finalgrade
