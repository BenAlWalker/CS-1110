# Ben Walker, baw3hg

import urllib.request
import re

number = 0



def report(name):
    '''
    This function finds a person who is employed at the University
    of Virginia and displays their occupation and their salary, including their rank
    of monetary value per year if it is included. If the person does not
    exist in the UVA system, then it tells you that, too.
    :param name: This is the person you want to look up.
    :return: Returns the job of the person, the salary, and their rank if they have one
    '''
    global number

    name = str(name)

    name = name.split()

    whatiactuallywant = []

    for each in name:
        if each.find(',') == -1:
            each = each.strip('.').lower()
            whatiactuallywant.append(each)

    for each in name:
        if each.find(',') != -1:
            each = each.strip(',').lower()
            whatiactuallywant.append(each)

    string = '-'
    string = string.join(whatiactuallywant)

    try:
        url = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/uva2018/' + string)
        conts = url.read().decode('UTF-8')
        everything = conts.split('\n')

        whatiwant = []
        rank_re = re.compile(r'([0-9],?[0-9]*) of [0-9]+,[0-9]+')

        for line in everything:
            num = line.find('Job title')
            if num != -1:

                job_re = re.compile(r'Job title: (.*)<')
                sal_re = re.compile(r'\$[0-9]+,?[0-9]+')
                for match in job_re.finditer(line):
                    whatiwant.append(match.group(1))
                for match in sal_re.finditer(line):
                    whatiwant.append(match.group(0))

            for match in rank_re.finditer(line):
                whatiwant.append(match.group(1))

        job = str(whatiwant[0])
        job = job.replace('&amp;', '&')
        job = job.replace('&#39;', "'")

        money = whatiwant[1]
        money = money[1:]
        money = money.replace(',', '')
        money = float(money)

        try:
            rank = str(whatiwant[2])
            rank = rank.replace(',','')
            rank = int(rank)
        except:
            rank = 0
    except:
        job = None
        money = 0
        rank = 0

    return job, money, rank
