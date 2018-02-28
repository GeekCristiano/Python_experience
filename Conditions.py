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

print("x is greater than y" if (x > y) else "x is greater than y")


# switch-case python analog

def getNameMonth(number):
    months = {1: "January",
              2: "February",
              3: "March",
              4: "April",
              5: "May",
              6: "June",
              7: "July",
              8: "August",
              9: "September",
              10: "October",
              11: "November",
              12: "December"}

    return months.get(number) if number in months.keys() else "Incorrect input value"

print(getNameMonth(4))
print(getNameMonth(127))

