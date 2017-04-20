# First problem
# Write a program that determines the distance to a lightning strike based on the time elapsed between the flash and
# the sound of thunder. The speed of sound is about 1100ft/sec and 1 mile is 5280ft. (Assume light travels infinitely
# fast.

speed_of_sound = 1100
feet_in_mile = 5280

print "Enter number of seconds between lightning flash and sound: "
elapsedTime = input("> ")

distance = speed_of_sound * elapsedTime
distanceInMiles = float(distance) / feet_in_mile

print "The lightning struck %s miles away." % format(distanceInMiles, '.2f')