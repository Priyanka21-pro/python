# Challenge 4 — Grade Calculator
# Write a program that takes marks and prints:
# 90–100 → A
# 75–89  → B
# 60–74  → C
# 40–59  → D
# Below 40 → Fail
# For example:
# Enter marks: 82
# Grade: B
# Notice that we didn't need to write:
# if marks >= 90 and marks <= 100:
# for every condition.
# Because Python checks from top to bottom, this is enough:
# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")
# elif marks >= 60:
#     print("C")
# elif marks >= 40:
#     print("D")
# else:
#     print("Fail")
# One important improvement

# Your current program would also give A for:

# 101

# because:

# 101 >= 90 → True



marks = int(input("enter your marks: "))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >=90:
    print("A")
elif marks >=75:
    print("B")
elif marks >=60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("Fail")