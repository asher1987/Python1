#  Write me a program that prints the times tables for a given number.
# You program should ask for 3 numbers:
# Investigated number
# Lower number of a range
# Higher number of a range
# Your program should print to the user this number multiplied by every number
# in that range. i.e. If I ask to investigate the number 5, from a lower number 
# of 8 to a higher number of 14 -->



# user input for investigatedNumber
investigatedNumber = input("We're doing math today. Please enter a number between 1 and 10. We will call this our 'investigated number': ")

#cast an str to an Int
investigatedNumber = int(investigatedNumber)
# Using a while loop to continuously prompt the user until they type 10
while investigatedNumber < 10:
    # checking for an integer using isdigit method
    if investigatedNumber < 10:
       # investigatedNumber = int(investigatedNumber)
        print("Great, thanks!")
        break  # Exit the loop if the number is valid
    else:
        print("Please enter a number.")
        
        
# asking for the lower number
lowerNumberOfARange = input("Please enter a number that is less than your investigated number. We will refer to this number as 'lower number': ")
#casting the str to an int
lowerNumberOfARange = int(lowerNumberOfARange)
# checking for an integer using isdigit method
#if lowerNumberOfARange.isdigit():
   # lowerNumberOfARange = int(lowerNumberOfARange)
if lowerNumberOfARange < (investigatedNumber):
    print("Great, thanks!")
else:
    print("please enter a number less than the investigated number")
        

            



# asking for a higher number
higherNumberOfARange = input("Please enter a number that is higher than your investigated number, but less than 10. We will refer to this number as 'higher number': ")
#casting the str to an int
higherNumberOfARange = int(higherNumberOfARange)

# checking for an integer using isdigit method
#if higherNumberOfARange.isdigit():
   # higherNumberOfARange = int(higherNumberOfARange)
    # checking to see if the higher number is greater than the lower number
if higherNumberOfARange > lowerNumberOfARange: 
        if higherNumberOfARange > investigatedNumber:
            print("Great thanks! Here comes the magic!")
        else:
            print("Please enter a higher number")
else: 
    print("Please enter a number")

# create a list of numbers to multiply by using the range function
userRanges = list(range(lowerNumberOfARange,higherNumberOfARange + 1))

# print user range
print( "investigated number =", investigatedNumber)
print("minimum calculated range =", lowerNumberOfARange)
print("maximum calcuated range =",higherNumberOfARange )

# for loop to loop through the list and multiply the investigated number by each element in the list
for userRange in userRanges:
    result = investigatedNumber * userRange
    #print(result)
#print statement using f string
    print(f"{investigatedNumber} X {userRange} = {result}\n")


    





