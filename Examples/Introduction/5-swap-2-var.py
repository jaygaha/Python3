print("Using a temporary variable")

# Python program to swap two variables
a = input('Enter value of a: ')
b = input('Enter value of b: ')

# Create a temporary variable and swap the values
tmp = a
a = b
b = tmp

print("The value of a after swapping: {}" . format(a))
print("The value of b after swapping: {}" . format(b))

print("\n\nWithout using temporary variable")

x = input("Enter value of x: ")
y = input("Enter value of y: ")

x, y = y, x

print("The value of x after swapping: {}" . format(x))
print("The value of y after swapping: {}" . format(y))