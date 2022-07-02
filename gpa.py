# Ben Walker, baw3hg

totalgpa = 0.0
totalcredit = 0


def add_course(newgpa, newcredit=3):
    global totalcredit
    global totalgpa
    newcredit = int(newcredit)

    coursegpa = newgpa * newcredit

    totalgpa = totalgpa * totalcredit
    totalcredit = totalcredit + newcredit

    totalgpa = totalgpa + coursegpa
    totalgpa = totalgpa / totalcredit

    return totalgpa, totalcredit


def credit_total():
    global totalcredit
    return totalcredit


def gpa():
    global totalgpa
    return totalgpa
