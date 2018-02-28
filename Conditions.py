# Let's study how work with conditional statements

def comparenumbers(x, y):
    if x > y:
        print("First argument is greater than second.")
    elif x == y:
        print("The first and second arguments are equal.")
    else:
        print("Second argument is greater than first.")


comparenumbers(5, 4)
comparenumbers(3, 7)
comparenumbers(2, 2)

# without using function
x = 6
y = 4

print("x is greater than y" if (x>y) else "x is greater than y")
