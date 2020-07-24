def print_msg(msg):
    # This is the outer enclosing function
    def printer():
        # This is the nested function
        print(msg)
    
    return printer #returns the nested function

# Now let's try calling this function
# Output: Hello
another = print_msg('Hello')
another()

# The print_msg() function was called with the string "Hello" and the returned function was bound to the name another. 
# On calling another(), the message was still remembered although we had already finished executing the print_msg() function.
# This technique by which some data ("Hello in this case) gets attached to the code is called closure in Python.

# This value in the enclosing scope is remembered even when the variable goes out of scope or the function itself is removed from 
# the current namespace.

# Try running the following in the Python shell to see the output.

del print_msg
another()

print_msg("Hello")