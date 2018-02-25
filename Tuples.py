# packing
man = ("Bob", "28", "MyCompanyName")
# unpacking
(name, age, company) = man
print(name)
print(age)
print(company)

tl1 = (6, 6)
tl2 = (5, 7)

# comparison of two tuples
if (tl1 == tl2):
    print("Equals!")
else:
    if (tl1 > tl2):
        print("First is bigger than second!")
    else:
        print("Second is bigger than first.")

# In dictionary each item is tuple
a = {"x": 100, "y": 4}
list = list(a.items())

for i in list:                                               # tuples everywhere :)
    print("Current item is: %s. Type object is: %s" % (str(i), str(type(i))))
