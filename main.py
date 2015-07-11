import sys

if len(sys.argv) < 2:
    print ("You need to supply letter")
    exit(1)

rack = sys.argv[1]

wordlist = []

try:
    with open("words.txt", "r") as f:
        for line in f:
            wordlist.append(line.strip())
except EnvironmentError:
    print ("Cannot find wordlist")
    exit(1)

valid_words = []

for word in wordlist:
    candidate = True
    rack_letters = list(rack)
    for letter in word:
        if letter not in rack_letters:
            candidate = False
            break
        else:
            rack_letters.remove(letter)
    if candidate == True:
        valid_words.append([len(word), word])

valid_words.sort()

for entry in valid_words:
    length = entry[0]
    word = entry[1]
    print(str(length) + " " + word)
