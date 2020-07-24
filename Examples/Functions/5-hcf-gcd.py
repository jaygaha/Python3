# The highest common factor (H.C.F) or greatest common divisor (G.C.D) of two numbers is the largest positive integer
# that perfectly divides the two given numbers. For example, the H.C.F of 12 and 14 is 2.

# Python program to find HCF of two numbers

def compute_hcf_loop(x, y):
    # Choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Using Loop")
print("The HCF is", compute_hcf_loop(num1, num2))


print("\n\nUsing Euclidean algorithm")
# Function to find HCF the using Euclidian algorithm
def compute_hcf_euclidian(x, y):
    while(y):
        x, y = y, x % y
    return x

num3 = int(input("Enter first number: "))
num4 = int(input("Enter second number: "))

print("The HCF is", compute_hcf_euclidian(num3, num4))
