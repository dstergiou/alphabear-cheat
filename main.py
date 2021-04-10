#!/usr/bin/env python3
import sys
import readline

# Initialize list
wordlist = []
executed = 0

# Open the Scrabble word list, exit if the file is not present
try:
    with open("words.txt", "r") as f:
        for line in f:
            wordlist.append(line.strip().replace('qu','Q')
except EnvironmentError:
    print("Cannot find wordlist")
    exit(1)

while True:
    try:
        # Initialize valid word list
        valid_words = []

        # Get user input
        query = input("[" + str(executed) + "]> ")
        if " " in query:
            rack, preference = query.split()
        else:
            rack = query
            preference = None

        # Find the words
        for word in wordlist:
            candidate = True
            rack_letters = list(rack)
            for letter in word:
                if letter not in rack_letters:
                    candidate = False
                    break
                else:
                    rack_letters.remove(letter)
            if candidate:
                valid_words.append([len(word), word])

        # Sort the valid words
        valid_words.sort()

        # Print words in the format (number of letters, word)
        for entry in valid_words:
            length = entry[0]
            word = entry[1].replace('Q','qu')
            if preference:                              # If we had a preferred letter
                candidate = True
                if '+' in preference:
                    if preference.replace('+', '') not in word:
                        candidate = False
                else:
                    for letter in list(preference):
                        if not str(letter) in word:     # Check if the letter is in the word
                            candidate = False
                if candidate:
                    # And print only words containing the preferred letter(s)
                    print(str(length) + " " + word)
            else:                                   
                print(str(length) + " " + word)          # Print all matching words
        executed += 1

    except KeyboardInterrupt:
        print("Exiting")
        exit(1)
