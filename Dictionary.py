# Create dictionary
dic = {"ONE": 1, "two": 2, "three": 3, "one": 2}
if dic["ONE"] == dic["one"]:
    print("Keys aren't case sensitive!")
else:
    print("Keys are case sensitive!")

# Remove key: value pair from dictionary, and update value
del dic["ONE"]
dic.update({"one": 1})
print(dic)
