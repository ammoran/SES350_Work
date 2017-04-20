# Problem 2
# Expand your solution to the previous problem to allow the calculation of a comlete name such as "John Marvin Zelle" or
# "John Jacob Jingleheimer Smith." The total value is just the sum of the numeric values of all the names. For the final
# program output, divide this total value by the total number of letters used for each name (to normalize the output and
# create an average numeric value). Show the output for a couple of names.

print "What is your name?"
name = raw_input("> ").lower().split()
print name
nameSum = 0
for word in name:
    for ch in word:
        shift = ord(ch) - 96
        nameSum += shift

print "The numerical sum of your name is", nameSum, "."
