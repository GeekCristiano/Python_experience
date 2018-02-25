# Create dictionary
dic = {"ONE": 1, "two": 2, "three": 3, "one": 2, "five": 5}
if dic["ONE"] == dic["one"]:
    print("Keys aren't case sensitive!")
else:
    print("Keys are case sensitive!")

# Remove key: value pair from dictionary, and update value
del dic["ONE"]
dic.update({"one": 1})
print(dic)

even = {"two": 2, "four": 4, "six": 6}
odd = {"one": 1, "three": 3, "five": 5}

print(list(odd.items()))

# Iterate over dictionary
for key in even.keys():
    if key in dic.keys():
        print("Source dictionary does contain key %s" % key)
    else:
        print("Source dictionary doesn't contain key %s" % key)
