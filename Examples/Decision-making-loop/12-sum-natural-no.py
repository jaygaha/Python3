# Python program to sum of natural numbers

num = int(input("Enter a positive number: "))

if num < 0:
    print("Enter a positive number: ")
else:
    # formula: n*(n+1)/2
    sum = num * (num + 1) / 2
    print("The sum is", sum)
