# This script prompts the user to enter two numbers,
# adds them together, and prints the result.

# 1. Get the first number (a) from the user.
# The input is converted to an integer using int() so arithmetic can be performed.
a = int(input("Please enter the first whole number: "))

# 2. Get the second number (b) from the user.
b = int(input("Please enter the second whole number: "))

# 3. Add the two numbers and store the result in variable c.
c = a + b

# 4. Print the result (the value of c) to the console.
print("The sum of the two numbers is:")
print(c)