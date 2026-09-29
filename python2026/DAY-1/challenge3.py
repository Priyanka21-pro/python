# 🚀 Day 1 Challenge 3 — Your turn
# Now let's combine input + variables + comparison + if/else.
# Write this program yourself:
# Ask the user for their name, age, and marks.
# If marks are 40 or more, print "Pass". Otherwise print "Fail".
# Finally, print their name and age.
# For example, if the user enters:
# Name: Priyanka
# Age: 22
# Marks: 65
# The output should be something like:
# Priyanka
# 22
# Pass
# Start with:
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# marks = int(input("Enter your marks: "))
# Now you write the if/else part and run it.


name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")


print(f"Hello {name}, you are {age} years old ")