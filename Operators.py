# Let's study how different operators work in the python

# A few simple arithmetic operators

x = 3
y = 5
print(x - y)
print(x + y)
print(x / y)
print(x * y)
print(y % x)
print(y % y)
print(x % y)

# Comparison Operators
if x > y:
    print("x > y")
else:
    print("x < y")

# Assignment Operators
z1 = x - y
x -= y

if (x == z1):
    print("same values")
else:
    print("different values")

# Logical operators

t = True
f = False

print(("t is f", t is f))
print(("t is not f", t is not f))
print(("t and f is", t and f))
print(("t or f is", t or f))
print(("not f is", not f))

# Membership Operators

str = "I love python <3 ! And python loves me too)"

if "l" in str:
    print(str.index('l'))
else:
    print("The string does not contain a character \"l\"")
