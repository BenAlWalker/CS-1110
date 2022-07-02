from urllib.request import urlopen

u = urlopen("http://cs1110.cs.virginia.edu/files/words.txt")

biglist = u.readlines()

for i in range(0, len(biglist)):
    word = str(biglist[i])
    word = word[2:len(word) - 3]
    word = word
    biglist[i] = word

print("Type text; enter a blank line to end.")

words = ' '
while words is not '':
    words = str(input(" "))
    if not words:
        break

    words = words.split(" ")

    for i in range(0, len(words)):
        words[i] = words[i].strip('"')
        words[i] = words[i].strip("'")
        words[i] = words[i].strip(",")
        words[i] = words[i].strip(".")
        words[i] = words[i].strip("!")
        words[i] = words[i].strip("?")
        words[i] = words[i].strip("@")
        words[i] = words[i].strip("#")
        words[i] = words[i].strip("$")
        words[i] = words[i].strip("%")
        words[i] = words[i].strip("^")
        words[i] = words[i].strip("&")
        words[i] = words[i].strip("*")
        words[i] = words[i].strip("(")
        words[i] = words[i].strip(")")

        wordnum = words[i].find(",")

        if wordnum is not -1:
            wordy = str(words[i])
            wordy = wordy[0:len(wordy) - 1]
            words[i] = wordy
        else:
            words = words[:len(words)]

    while "" in words:
        words.remove("")
    for i in range(0, len(words)):
        if str(words[i].lower()) not in biglist:
            print("  MISSPELLED: " + words[i])
