# Problem 6
# An acronym is a word formed by taking the first letters of the words in a phrase and and making a word from them. For
# example, RAM is an acronym for "random access memory." Write a program that allows the user to type in a phrase and
# then outputs the acronym for that phrase. Note: the acronym should be all uppercase, even if the words in that phrase
# are not capitalized.

print "Enter a phrase to acronymize"
phrase = raw_input("> ")

capPhrase = phrase.upper()
wordArray = capPhrase.split(' ')
acronym = ""

for i in range(len(wordArray)):
    character = wordArray[i][0]
    acronym = acronym + character
print "The acronym for", phrase + " is:", acronym
