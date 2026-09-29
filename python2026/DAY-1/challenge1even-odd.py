#A very common beginner coding question is:
# Write a Python program to check whether a number is even or odd.
# Let's build it together.
# Start with:
# number = int(input("Enter a number: "))
# Now you write the next line.
# Hint: You need to use % and ==.
# What should the if condition be?



number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")