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
