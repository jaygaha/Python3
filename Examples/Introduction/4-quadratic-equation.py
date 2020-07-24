# The standard form of a quadratic equation is:
# ax2 + bx + c = 0, where
# a, b and c are real numbers and
# a ≠ 0

# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Calculate the discriminant
d = (b**2) - (4*a*c)

# Find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The solution are {0} and {1}".format(sol1,sol2))