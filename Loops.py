# Let's study how work with loops in python

# while loop example

x = 5

while x < 8:
    print(x)
    x += 1


# for loop example

def print_twice(value):
    for i in range(2):
        print(value)


print_twice("String")


# iterate over list
def get_even_numbers(numbers):
    even_numbers = []

    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)

    return even_numbers


numbers = [0, -17, 4, 17, 6, 9]
print(get_even_numbers(numbers))
