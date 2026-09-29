# Day 1 — Challenge 2
# Now let's make it slightly harder.
# Write a program that asks the user for their age and prints:
# Age 0–12    → Child
# Age 13–19   → Teenager
# Age 20+     → Adult
# Start with:
# age = int(input("Enter your age: "))
# Then complete the if / elif / else.





age = int(input("enter your age: "))
if age <= 12:
    print("child")
elif age <= 19:
    print("Teenager")
else:
    print("Adult")