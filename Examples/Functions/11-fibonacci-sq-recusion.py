# Python program to find the fibonacci sequence using recusion

def recurion_fib(n):
    if n <= 1:
        return n
    else:
        return (recurion_fib(n - 1) + recurion_fib(n - 2))

num = int(input("Enter a terms: "))
if num > 0:
    print("Fibonacci sequence: ")
    for i in range(num):
        print(recurion_fib(i))
else:
    print("Please enter a positive number")