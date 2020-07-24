# Python program to convert decimal into other number systems like binary, octal and hexadecimal

num = int(input("Enter decimal value: "))

print("The decimal value of", num, "is:")
print(bin(num), "in binary")
print(oct(num), "in octal")
print(hex(num), "in hexadecimal")