# Python program to display the powers of 2 using anonymous function

terms = int(input("Enter a terms? "))

# use anonymous function
res = list(map(lambda x:2 ** x, range(terms)))

print("The total terms are:", terms)

for i in range(terms):
    print("2 raised to powers",i,"is",res[i])