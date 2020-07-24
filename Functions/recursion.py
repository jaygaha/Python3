def factorial(x):
    """This is a recursive function
    to find the factorial of an integer
    For example, the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720.
    """

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 8
print("The factorial of", num, "is", factorial(num))