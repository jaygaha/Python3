# Python program to print binary number using recusion

def convert_to_binary(n):
    if n > 1:
        convert_to_binary(n // 2)
    print(n % 2, end='')

num = input("Enter a number: ")
if float(num).is_integer() == True:
    print("The binary number is")
    convert_to_binary(int(num))
    print()
else:
    print("Binary number only works with whole numbers")