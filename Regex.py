# using regular expression in python

# imported necessary module
import re

str = "Learning python is fun and interesting."
pattern = r"^\w+"
print(re.findall(pattern, str))
