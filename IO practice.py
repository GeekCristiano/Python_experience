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
