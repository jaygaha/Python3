# Python program to find the numbers divisible by another number and display it

lists = [10, 35, 55, 63, 76, 188, 216, 345, 466]
# divisible by
div = 12

# use anonymous function to filter
res = list(filter(lambda x: (x % div == 0), lists))

# display the result
print("Numbers divisible by ", div, "are",res)