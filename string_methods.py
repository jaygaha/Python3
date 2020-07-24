name = "JaY GAha"
print(len(name))
print(name.lower())
print(name.upper())
print(name.title())
print(name.count("a"))

# ------------------------------
# FIND and REPLACE
str = "She is beautiful and she is good student"
print(str.replace(" ", "-"))
print(str.replace("is", "was"))
print(str.replace("is", "was", 1)) #1 is count value, how many time it should replace the old

#FIND
pos = str.find("is")
print(pos)
#to search second "is"
print(str.find("is" , pos +1))

#CENTER
ctr = "Middle"
# print(ctr.center(10))
print(ctr.center(10, '*'))