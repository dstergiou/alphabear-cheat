import sys

# Get the letters from the command line
if len(sys.argv) < 2:
    print ("You need to supply the letters")
    exit(1)

# Assign the letters we got from the command line to the rack variable
rack = sys.argv[1]

# Initialize an empty wordlist
wordlist = []

# Open the Scrabble word list, exit if the file is not present
try:
    with open("words.txt", "r") as f:
        for line in f:
            wordlist.append(line.strip())
except EnvironmentError:
    print ("Cannot find wordlist")
    exit(1)

# Initialize an empty wordlist to hold valid words
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

# Sort the valid words
valid_words.sort()

# Print words in the format (number of letters, word)
for entry in valid_words:
    length = entry[0]
    word = entry[1]
    print(str(length) + " " + word)
