# We solve the following problem:
# There is a file for 4000 lines. It is necessary to make 40 files of 100 lines.

import os
from random import randint


def main():
    # create directory to put it original file and 40s part of source file

    test_dir_name = "40s part"
    test_dir_full_path = os.path.realpath(os.path.curdir) + os.sep + test_dir_name

    try:
        os.mkdir(test_dir_full_path)
        if os.path.exists(test_dir_full_path) and os.path.isdir(test_dir_full_path):
            print("Folder \"{}\" is successfully created!".format(test_dir_name))
    except OSError:
        print("An error occurred while making new directory.")

    # create source data set

    source_file_name = "dataset.txt"
    source_file_full_path = test_dir_full_path + os.sep + source_file_name

    try:
        source_file = open(source_file_full_path, "w")

        # generate random data and write to source file

        for i in range(4000):
            value = randint(10000000, 19999999)
            source_file.write("{}\n".format(value))

        source_file.close()

    except IOError:
        print("Something went wrong. . .")


# source_file = open("source_file.txt", "r")  # read and parse all data from source file
# list = source_file.readlines()
#
# file_name_template = "source_file_{}.txt"
# count = 0
#
# for ind, value in enumerate(list):
#
#     if (ind + 1) % 40 == 0:
#         count = count + 1
#         start_index = (ind + 1) - 40
#         print(start_index)
#
#         file = open(file_name_template.format(count), "w")
#
#         for i in range(40):
#             file.write(list[start_index + i])
#
#         file.close()
# source_file.close()

if __name__ == "__main__":
    main()
