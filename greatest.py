import sys

# If arguments are passed from Jenkins, use them. Otherwise, prompt user normally locally.
if len(sys.argv) >= 4:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    num3 = float(sys.argv[3])
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

# Your exact logic
if (num1 >= num2) and (num1 >= num3):
    greatest = num1
elif (num2 >= num1) and (num2 >= num3):
    greatest = num2
else:
    greatest = num3

print(f"The numbers are: {num1}, {num2}, {num3}")
print(f"The greatest number is: {greatest}")
