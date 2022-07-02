# Ben Walker, baw3hg


import re
import urllib.request


def leppard(stream):
    email_re = re.compile(r'[a-zA-Z0-9]+' + '@' + '[a-zA-Z0-9]+' + '\.' + '[a-z]+')

    url = urllib.request.urlopen(stream)
    conts = url.read().decode('UTF-8')
    conts = str(conts)

    biglist = []
    for match in email_re.finditer(conts):
        biglist.append(match.group(0))

    biglist = list(dict.fromkeys(biglist))

    for i in biglist:
        print(i)


leppard('http://cs1110.cs.virginia.edu/emails.html')
