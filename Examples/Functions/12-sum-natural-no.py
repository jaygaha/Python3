# Python program to find the sum of natural number using recursive function

def recursive_sum(n):
    if n <= 1:
        return n
    else:
        return n + recursive_sum(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Enter a positive number")
else:
    print("The sum is", recursive_sum(num))