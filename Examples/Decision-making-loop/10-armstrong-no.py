# Python program to check if the number is an Armstrong number or not
# A positive integer is called an Armstrong number of order n if

# abcd... = an + bn + cn + dn + ...

# In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself. For example:

# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.


num = int(input("Enter a number: "))

# Calculate the length or num
order = len(str(num))
sum = 0

# Find the sum of the cube of each digit
tmp = num
while tmp > 0:
    digit = tmp % 10
    sum += digit ** order
    tmp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")