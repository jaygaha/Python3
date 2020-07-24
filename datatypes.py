#Python Numbers
a = 5
print("Python Numbers")
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

#Python List
a = [5,10,15,20,25,30,35,40]

print("Python List")
# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

#Python Tuple
t = (5,'program', 1+3j)
print("Python Tuple")
# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
#t[0] = 10

#Python Strings
print("Python String")
s = "This is a string"
print(s)
s = '''A multiline
string'''
print(s)

#Python Set
print("Python set")
a = {5,2,3,1,4}

# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))

#We can perform set operations like union, intersection on two sets. Sets have unique values. They eliminate duplicates.
u = {1,2,2,3,3,3}
print(u)

#Python Dictionary
print("Python Dictionary")
d = {1:'value','key':2}
print(type(d))

print("d[1] = ", d[1])

print("d['key'] = ", d['key'])

# Generates error
#print("d[2] = ", d[2])