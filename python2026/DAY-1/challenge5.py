# Problem:
# Ask the user for a number.
# If the number is positive → print "Positive"
# If the number is negative → print "Negative"
# If the number is exactly 0 → print "Zero"
# Example:
# Enter a number: -5
# Negative

number = int(input("enter a number: "))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")
    