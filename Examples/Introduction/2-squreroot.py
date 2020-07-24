print("Example: For positive numbers")
# Python program to calculate the square root

num = float(input("Enter a number: "))

num_sqrt = num ** 0.5

print("The square root of %0.3f is %0.3f"%(num, num_sqrt))

print("\n\nSource code: For real or complex numbers")
# Find square root of real or complex numbers
# Importing the complex math module
import cmath

num1 = 1+2j

num_sqrt1 = cmath.sqrt(num1)
print("The square root of {0} is {1:0.3f}+{2:0.3f}j".format(num1, num_sqrt1.real, num_sqrt1.imag))