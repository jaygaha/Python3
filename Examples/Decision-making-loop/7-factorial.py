# Python program to find the factorial of number
# eg: factorial of 6 = 1*2*3*4*5*6 = 720

num = int(input("Enter a number: "))

factorial = 1
# Check if the num is negative, positive or zero

if num < 0:
    print("Sorry, factorial does not exist for negative number")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial*i
    print("The factorial of", num, "is", factorial)