# Problem 8
# Word Count
# A common utility on Unix/Linux systems is a small program called "wc." This program analyzes a file to determine the
# number of lines, words, and characters contained therein. Write your own version of wc. The program should accept a
# file name as input and then print three numbers showing the count of lines, words, and characters in the file.

import os.path

lines, words, characters = 0, 0, 0
print "Enter the filename you want to analyze"
filename = raw_input("> ")
textf = open(os.path.abspath(filename), 'r')

for line in textf:
    lines += 1
    word = line.split()
    words += len(word)
    chars = len(line)
    characters += chars
print "There are", lines, "lines in the file", filename + "."
print "There are", words, "words in the file", filename + "."
print "There are", characters, "characters in the file", filename + "."

