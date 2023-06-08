# <!-- Write me a program that prints the times tables for a given number.
# You program should ask for 3 numbers:
# Investigated number
# Lower number of a range
# Higher number of a range
# Your program should print to the user this number multiplied by every number
# in that range. i.e. If I ask to investigate the number 5, from a lower number 
# of 8 to a higher number of 14 -->

# user input for investigatedNumber
investigatedNumber = input("We're doing math today. Please enter a number between 0 and 10. We will call this our 'investigated number': ")

# checking for an integer using isdigit method
if investigatedNumber.isdigit():
    investigatedNumber = int(investigatedNumber)
    print("Great, thanks!")
else:
    print("Please enter a number.")

# asking for the lower number
lowerNumberOfARange = input("Please enter a number that is less than your investigated number. We will refer to this number as 'lower number': ")

# checking for an integer using isdigit method
if lowerNumberOfARange.isdigit():
    lowerNumberOfARange = int(lowerNumberOfARange)
    print("Great, thanks!")

# asking for a higher number
higherNumberOfARange = input("Please enter a number that is higher than your investigated number, but less than 10. We will refer to this number as 'higher number': ")

# checking for an integer using isdigit method
if higherNumberOfARange.isdigit():
    higherNumberOfARange = int(higherNumberOfARange)
    print("Great, thanks! Here comes the magic!")

# create a list of numbers to multiply by using the range function
userRange = list(range(lowerNumberOfARange, higherNumberOfARange + 1))
print(userRange)
print( "investigated number =", investigatedNumber)
print("minimum calculated range =", lowerNumberOfARange)
print("maximum calcuated rainge =",higherNumberOfARange )

# for loop to loop through the list and multiply the investigated number by each element in the list
for rangeNumber in userRange:
    result = investigatedNumber * rangeNumber
#print statement using f string
    print(f"{investigatedNumber} * {rangeNumber} = {result}")


    





