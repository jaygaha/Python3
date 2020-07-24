# The least common multiple (L.C.M.) of two numbers is the smallest positive integer 
# that is perfectly divisible by the two given numbers. For example, the L.C.M. of 12 and 14 is 84.

# Python program to find the LCM of two numbers

def compute_lcm(x, y):
# choose the greater number
    if x > y:
        greater = x
    else:
        greater = y
    
    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The LCM is", compute_lcm(num1, num2))

print("Using GCD")
def compute_gcd(x, y):
    while (y):
        x, y = y, x % y
    return x

def compute_lcm_gcd(x, y):
    return (x*y)//compute_gcd(x, y)

num3 = int(input("Enter first number: "))
num4 = int(input("Enter second number: "))

print("The LCM is", compute_lcm_gcd(num3, num4))