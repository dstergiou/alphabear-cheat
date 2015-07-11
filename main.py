#!/usr/bin/env python3
import sys
import argparse

# Use an option parser
parser = argparse.ArgumentParser()
parser.add_argument('letters', help='Letter to use for finding word')
parser.add_argument('preference', nargs='?', help='Preferred letter')
args = parser.parse_args()

# Assign the letters we got from the command line to the rack variable
rack = args.letters

# Initialize lists
wordlist = []
valid_words = []

# Open the Scrabble word list, exit if the file is not present
try:
    with open("words.txt", "r") as f:
        for line in f:
            wordlist.append(line.strip())
except EnvironmentError:
    print ("Cannot find wordlist")
    exit(1)

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
    if args.preference:                     # If we had a preferred letter
        if str(args.preference) in word:    # Check if the letter is in the word
            print(str(length) + " " + word) # And print only words containing the preferred letter
    else:                                   # else
        print(str(length) + " " + word)     # print all matching words
