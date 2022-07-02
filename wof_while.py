# Kieran O'Dell (kfo7qb) & Ben Walker (baw3hg)

word = input("Enter a word or phrase: ")
word1 = "_".join(word.lower())+"_"

print("The word to guess:", word1[1::2])

while "_" in word1:
    letter = input("Guess a letter: ")
    word1 = word1.replace(letter + "_", letter + letter)
    if "_" in word1:
        print("The word to guess:", word1[1::2])

print("It was "+word+"; you win!")