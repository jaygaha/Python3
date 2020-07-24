# Python program to display the Fibonacci sequence up to n-th term
# for eg: 0,1,1,2,3,5,8...nth term
# The first two terms are 0 and 1. 
# All other terms are obtained by adding the preceding two terms. 
# This means to say the nth term is the sum of (n-1)th and (n-2)th term.

terms = int(input("How many terms?: "))

# first two terms
n1, n2 = 0, 1
count = 0

# Check if the number of terms is valid
if terms <= 0:
    print("Please enter positive number")
elif terms == 1:
    print("Fibonacci sequence upto", terms, ":")
    print(n1)
else:
    print("Fibonacci sequence: ")
    while count < terms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1