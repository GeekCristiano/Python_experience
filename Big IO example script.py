# In this script I create a test directory, and inside it is a file.
# In the test file, I record some data.
# Next, I rename the test directory and the file.
# After I copy the file.
# Finally I delete the created directory and all the files inside.

import os
from os import path


def create_item(folder_path, name):
    if path.exists(folder_path) and path.isdir(folder_path):
        # Try to create a new directory in the current folder
        try:
            os.mkdir(folder_path + os.sep + name)
            return True
        except OSError:
            print("An error occurred while making new directory.")
            return False
    else:
        print("Incorrect arguments!")
        return False


def remove_item(name):
    # Check that the directory exists
    if path.exists(name) and path.isdir(name):

        dir_path = path.realpath(name)

        try:
            os.rmdir(dir_path)
            return True
        except OSError:
            print("An error occurred while removing directory.")
            return False
    else:
        print("Incorrect argument!")
        return False


def main():
    initial_folder_pat = path.realpath(path.curdir)

    if create_item(initial_folder_pat, "test_folder") is True:
        print("New folder is successfully created!")
        new_folder_path = path.realpath("test_folder")
        print(new_folder_path)

        if remove_item("test_folder") is True:
            print("Folder is successfully removed!")
        else:
            print("Folder is not removed!")
    else:
        print("A new directory was not created.")


if __name__ == "__main__":
    main()
