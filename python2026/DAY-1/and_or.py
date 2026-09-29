# Write this program:
# Ask the user for their age.
# If their age is 18 or above AND 60 or below, print "Eligible". Otherwise print "Not Eligible".
# Use and.
# ⭐ Important interview shortcut
# There is another way to write the same condition:
# if 18 <= age <= 60:
#     print("Eligible")
# This is called chained comparison in Python.
# Both are valid:
# age >= 18 and age <= 60





age = int(input("enter your age: "))
# if age >= 18 and age <= 60:
if 18 <= age <=60:
    print("Eligible")
else:
    print("Not Eligible")