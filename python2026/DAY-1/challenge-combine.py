# 🚀 Day 1 Challenge — Combine Everything
# Now let's make your first slightly more realistic coding problem.
# Write a program that asks for age and marks.
# Rules:
# Age must be 18 or above
# Marks must be 40 or above
# If both are satisfied → print "Eligible for interview"
# Otherwise → print "Not eligible"
# Example:
# Enter age: 22
# Enter marks: 65
# Eligible for interview
# You'll need:
# input()
# int()
# if
# and
# >=
# else


age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

if age >= 18 and marks >=40:
    print("Eligible for interview")
else:
    print("Not Eligible")