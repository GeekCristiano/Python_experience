# lets' learn how work with files: create, open, append, read, write

# Open or create file.txt
f = open("file.txt", "w+")
for row in range(1, 12):
    # write into file
    f.write("Line #%d\n" % row)
# close file
f.close()

# append line into file
f = open("file.txt", "a+")
f.write("It is last line into file!\n")
f.close()

# open file for reading
f = open("file.txt", "r")
# read contents from file
contents = f.read()
print(contents)
f.close()

# read contents line by line

f = open("file.txt", "r")

for line in f.readlines():
    print(line, end="")
