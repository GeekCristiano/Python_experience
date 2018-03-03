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
