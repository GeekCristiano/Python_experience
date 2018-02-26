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
