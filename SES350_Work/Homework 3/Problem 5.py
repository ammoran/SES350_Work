# Problem 5
# A professor gives 100-point exams that are graded on the scale 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F. Write a
# program that accepts an exam score as input and prints out the corresponding grade.

print "Please enter your score"
grade = input("> ")

if grade > 100:
    print "Impossibru!"
elif grade >= 90:
    print "You got an A"
elif grade >= 80:
    print "You got a B"
elif grade >= 70:
    print "You got a C"
elif grade >= 60:
    print "You got a D"
elif grade < 60:
    print "You got a F"
