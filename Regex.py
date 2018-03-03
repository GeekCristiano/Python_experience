# using regular expression in python

# imported necessary module
import re

str = "Learning python is fun and interesting."
pattern = r"^\w+"
print(re.findall(pattern, str))

regexList = re.split(r"\s", str)
noneRegexList = re.split(" ", str)

if regexList == noneRegexList:
    print("Lists are the same.")
else:
    print("Lists are the different.")

# To search for matches at the beginning of a line, use the function match

checkString = "1980 year of my birth"
print(re.match("(\d{4})", checkString).groups())

# checkString = "Peter was born in 1980, and Jessica 3 years later in 1983."
