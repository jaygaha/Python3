#Example 1: Accessing global Variable From Inside a Function
c = 1 # global variable

def add():
    print(c)

add()

#Example 2: Modifying Global Variable From Inside the Function
c1 = 1 # global variable
def add1():
    global c1
    c1 = c1 + 2 # increment c1 by 2
    print(c1)

add1()