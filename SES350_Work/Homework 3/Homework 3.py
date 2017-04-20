# Third Problem
# Write a program to calculate the area of a triangle given the length of its three sides a, b, and c using these
# formulas:
#
# s = (a+b+c)/2
# A = sqrt(s(s-a) (s-b) (s-c))

import math

print "What are the lenghths of the 3 sides of the triangle?"
n = 1
sides = []
while n < 4:
    i = input("Side" + " " + str(n) + ": ")
    print "Side %d is: %d" % (n, i)
    sides.append(i)
    n += 1

a, b, c = sides[0], sides[1], sides[2]
s = (a + b + c) / 2
A = math.sqrt(s * (s - a) * (s - b) * (s-c))
print "The area of the trinagle is %s units" % format(A, '.2f')
