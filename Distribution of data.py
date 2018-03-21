# We solve the following problem:
# There is a file for 4000 lines. It is necessary to make 40 files of 100 lines.
import random


def main():
    # create source data set
    source_file = open("source_file.txt", "w")

    # generate random data and write to source file
    for elem in range(4000):
        value = random.randint(10000000, 19999999)
        source_file.write("{}\n".format(value))

    source_file.close()


if __name__ == "__main__":
    main()
