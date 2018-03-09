# In this script I create a test directory, and inside it is a file.
# In the test file, I record some data.
# Next, I rename the test directory and the file.
# After I copy the file.
# Finally I delete the created directory and all the files inside.

import os
from os import path


def create_item(name):
    # get script execution folder
    current_directory = path.realpath(path.curdir)

    # Try to create a new directory in the current folder
    try:
        os.mkdir(current_directory + os.sep + name)
        return True
    except OSError:
        print("An error occurred while making new directory.")
        return False


def main():
    if create_item("test_folder") is True:
        print("New folder is successfully created!")
    else:
        print("A new directory was not created.")


if __name__ == "__main__":
    main()
