# Let's study how define own functions in python, study arguments, return value

# define custom function
def sayhello():
    print("Hello!")


# call function
sayhello()


# example  of using return value in python function
def doubleMessage(message):
    return message * 2


print(doubleMessage("Welcome!"))


# argument y has default value equals zero, if value isn't pass into function
def multiply(x, y=0):
    print("x is %s" % x)
    print("y is %s" % y)
    return x * y


print(multiply(5))
print(multiply(5, 2))
# Change order in arguments list
print(multiply(y=4, x=1))


# Multiple Arguments
def printArguments(*args):
    print(args)


printArguments(("Tuple"), 2, "String", {"key": "value"})
