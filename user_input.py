# name = input("Type your name: ")
# print("Hello " + name)
# age = input("Type your age: ")
# print("Your are " + age + " years old")

#MULTIPLE INPUTS IN SINGLE LINE
# name, age = input("Type your name and age: ").split() # default space must give to separate two values
# print(name)
# print(age)

# if we have to specify to separate values then we have to pass value on split function like ,,-
name, age = input("Type your name and age: ").split(",")
print(name)
print(age)