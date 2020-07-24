# Program to check Armstrong numbers in a certain interval

lower = int(input("Enter a starting number: "))
upper = int(input("Enter a ending number: "))

for num in range(lower, upper + 1):
    # order of number
    order = len(str(num))
    sum = 0

    tmp = num
    while tmp > 0:
        digit = tmp % 10
        sum += digit ** order
        tmp //= 10
    if num == sum:
        print(num)