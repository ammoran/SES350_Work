# Problem 4
# You have seen that the math library contains a function that computes the square root of a number. In this exercise,
# you are to write your own algorithm for computing square roots. One way to solve this problem is to use a
# guess-and-check approach. You first guess what the square root might be and then see how close your guess is. You can
# use this information to make another guess and continue guessing until you have found the square root (or a close
# approximation to it). One particularly good way of making guesses is to use Newton's method. Suppose x is the number
# we want the root of and guess is the current guessed answer. The guess can be improved by using (guess+x/guess)/2 as
# the next guess. Write a program that implements Newton's method. The program should prompt the user for the value to
# find the square root of (x) and the number of times to improve the guess. Start with a guess value of x/2, your
# program should loop the specified number of times applying Newton's method and report the final value of guess. You
# should also subract your estimate from the value of math.sqrt(x) to show how close it is.

import math

print "What do you want to calculate the square root of?"
x = input("> ")
print "How many attempts do you want to make?"
attempts = input("> ")
guess = round(float(x) / 2, 3)
print type(guess)

i = 1
while i < attempts:
    print "Current guess is ", guess
    guess = round((guess + x / guess) / 2, 3)
    i += 1

print "Final guess is ", guess
off = abs(math.sqrt(x) - guess)
print "You were off by ", off
