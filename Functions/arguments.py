def greet(name, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", name + ', ' + msg)

greet("Jay", "Good morning!")

#Variable Function Arguments
#Python Default Arguments
print("Python Default Arguments")
def greet1(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet1("Jay")
greet1("Jay", "How do you do?")

#Python Keyword Arguments
print("Python Keyword Arguments")
# 2 keyword arguments
greet1(name = "Jay",msg = "How do you do?")

# 2 keyword arguments (out of order)
greet1(msg = "How do you do?",name = "Jay") 

# 1 positional, 1 keyword argument
greet1("Jay", msg = "How do you do?") 

#Python Arbitrary Arguments
print("Python Arbitrary Arguments")
def greet2(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greet2("Jay", "John", "Doe", "Monica")