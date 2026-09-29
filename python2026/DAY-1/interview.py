# What will this program output?

x = 15
y = 10

if x > y:
    print("A")
elif x == y:
    print("B")
else:
    print("C")

# And tell me why.
# in this program x,y is given in first condition x>y is true because 15>10 and the 2 condition x == y its false because 15 == 10 15 is not equal to 10   then it print A true B flase Or defalut C


# Python checks from top to bottom:

# 1️⃣ First condition
# x > y

# becomes:

# 15 > 10 → True

# So Python immediately executes:

# print("A")

# Output:

# A
# 2️⃣ Does it check elif?

# No.

# This is very important:

# Once Python finds a True condition in an if/elif/else chain, it executes that block and skips the remaining conditions.

# So technically, 15 == 10 is indeed False, but Python doesn't even need to check it because the first condition was already True.

# Remember:
# if     → checked first
# elif   → checked only if previous condition is False
# else   → runs if all conditions are False

# You're doing well with the logic. Now let's move from basic conditions into a slightly more realistic MNC coding problem.