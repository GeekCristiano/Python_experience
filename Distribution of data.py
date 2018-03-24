# We solve the following problem:
# There is a file for 4000 lines. It is necessary to make 40 files of 100 lines.


def main():
    # create source data set
    # try:
    #     source_file = open("source_file.txt", "w")
    #
    #     # generate random data and write to source file
    #     for elem in range(4000):
    #         value = random.randint(10000000, 19999999)
    #         source_file.write("{}\n".format(value))
    #
    #     source_file.close()
    # except IOError:
    #     print("An error occurred while opening the file.")
    source_file = open("source_file.txt", "r")

    # read and parse all data from source file
    list = source_file.readlines()

    file_name_template = "source_file_{}.txt"
    count = 0

    for ind, value in enumerate(list):

        if (ind + 1) % 40 == 0:
            count = count + 1
            start_index = (ind + 1) - 40
            print(start_index)

            file = open(file_name_template.format(count), "w")

            for i in range(40):
                file.write(list[start_index + i])

            file.close()
    source_file.close()


if __name__ == "__main__":
    main()
