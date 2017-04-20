# Problem 1
# Numerologists claim to be able to determine a person's character traits based on the "numeric value" of a name. The
# value of a name is determined by summing up the values of the letters of the name where "a" is 1, "b" is 2, "c" is 3,
# etc. For example, the name "Zelle" would have the value 26+5+12+12+5=60. Write a program that calculates the numeric
# value of a single name provided as input. Show that program and example input/output.

print "What is your name?"
name = raw_input("> ").lower()
nameSum = 0
for ch in name:
    shift = ord(ch) - 96
    nameSum += shift
print "The numeric value of your name is", nameSum, "."
