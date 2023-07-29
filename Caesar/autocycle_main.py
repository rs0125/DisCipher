import caesarcode
from binarysearch import search, wordcount

inpt = input('enter the paragraph :')
inpt.lower()

# opening the 474k english words text file
f = open('words.txt', 'r')
wordlist = f.read()

# getting the wordcount in enciphered text
wordcounter = wordcount(inpt)

# running 25 shift cases
for i in range(0, 26):
    dcount = 0
    shift = i
    decipher = (caesarcode.decode(shift, inpt)).lower()  # runs a singular shift cycle, turns it to lower case
    decipher1 = decipher.split()  # conversion to word list for binary search operation through word database
    for j in decipher1:  # running through each word
        temp = search(wordlist, j)  # checking if word is a part of the english database
        if temp == True:
            dcount += 1  # adds to a counter if word is found in database

    # if counter is over 75% of the enciphered word count, it returns as a successful decipher
    if dcount > 0.75 * wordcounter:
        print(decipher)
        break
# closing the 474k english words text file
f.close()
