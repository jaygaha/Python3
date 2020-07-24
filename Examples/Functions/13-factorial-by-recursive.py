# Python program to find factorial of a number using recusion function

def recusion_factor(n):
    if n == 1:
        return n
    else:
        return n * recusion_factor(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exists for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recusion_factor(num))