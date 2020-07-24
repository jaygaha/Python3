name = "Jay"
age = 30
print("Name: " + name + " Age: " + str(age)) #NOT RECOMMENDED

print("Name: {} Age: {}".format(name, age)) #PYTHON 3
print(f"Name: {name} Age: {age}") #PYTHON 3.6


# string indexing

x = "Python"

# positions (index no) | negative indexing
# 0=P | -6
# 1=y | -5
# 2=t | -4
# 3=h | -3
# 4=o | -2
# 5=n | -1 for the last character
# 
print(x[3]) #h
print(x[-1]) #n


# String Slicing
# 1) Slicing - [start argument : stop argument + 1]

print (x[0:2]) #Py
print (x[3:6]) #hon

print(x[:]) #all characters --Python

# Step Argument
# syntax: [start argument: stop argument - 1 : step]

print("NepalKingdom"[0:4:1]) #Nepa
print("NepalKingdom"[0:4:2]) #Np
print("NepalKingdom"[0::2]) #Npligo

#REVERSE
print("Nepal"[4::-1]) #lapeN
print("Nepal"[-1::-1]) #lapeN