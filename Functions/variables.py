# GLOBAL
x = "global"

def foo():
    print("x inside:", x)


foo()
print("x outside:", x)

# Local Variables
def foo1():
    y = "local"
    print(y)

foo1()

#Using Global and Local variables in the same code
x = "global "

def foo2():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo2()

#Global variable and Local variable with same name
x = 5

def foo3():
    x = 10
    print("local x:", x)


foo3()
print("global x:", x)

# Nonlocal Variables
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()