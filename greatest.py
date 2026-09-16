import sys

# Check if arguments are provided from Jenkins, otherwise use defaults
if len(sys.argv) >= 4:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    num3 = float(sys.argv[3])
else:
    num1, num2, num3 = 10.0, 25.0, 15.0

# Find the greatest number
greatest = max(num1, num2, num3)

print(f"The numbers are: {num1}, {num2}, {num3}")
print(f"The greatest number is: {greatest}")
