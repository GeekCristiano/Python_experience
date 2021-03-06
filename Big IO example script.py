# In this script I create a test directory, and inside it is a file.
# In the test file, I record some data.
# Next, I rename the test directory and the file.
# After I copy the file.
# Finally I delete the created directory and all the files inside.

import os
import shutil


def create_folder(folder_path, name):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
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


def remove_folder(name):
    # Check that the directory exists
    if os.path.exists(name) and os.path.isdir(name):

        dir_path = os.path.realpath(name)

        try:
            os.rmdir(dir_path)
            return True
        except OSError:
            print("An error occurred while removing directory.")
            return False
    else:
        print("Incorrect argument!")
        return False


def create_file(folder_path, name):
    full_path = folder_path + os.path.sep + name

    if not os.path.exists(full_path):
        try:
            new_file = open(full_path, "x")
            new_file.close()
            print("File %s is successfully created!" % name)
            return True
        except:
            print("An error occurred while creating file.")
            return False
    else:
        print("File %s already exists." % name)
        return False


def remove_file(path_to_file):
    if os.path.exists(path_to_file) and os.path.isfile(path_to_file):
        try:
            os.remove(path_to_file)
            return True
        except:
            print("An error occurred while removing directory.")
            return False
    else:
        print("Invalid argument!")
        return False


def main():
    initial_folder_path = os.path.realpath(os.path.curdir)
    initial_file_name = "test_file.txt"
    copy_file_name = "test_file.txt.bak"
    renamed_file_name = "test_file_renamed.txt"
    initial_folder_name = "test_folder"
    renamed_folder_name = "test_folder_renamed"

    if create_folder(initial_folder_path, initial_folder_name) is True:
        print("New folder is successfully created!")

        new_folder_path = os.path.realpath(initial_folder_name)

        if create_file(new_folder_path, initial_file_name) is True:
            print("New file is successfully created!")
            # write some data to file
            file = open(new_folder_path + os.sep + initial_file_name, "w")

            for number in range(12):
                file.write("Line #%d\r\n" % number)

            file.close()

            # rename text file
            os.rename(new_folder_path + os.sep + initial_file_name,
                      new_folder_path + os.sep + renamed_file_name)

            # get copy of test_file.txt with full metadata
            shutil.copy(new_folder_path + os.sep + renamed_file_name,
                        new_folder_path + os.sep + copy_file_name)

            # rename test folder
            parent_folder, folder_name = os.path.split(new_folder_path)

            full_new_folder_path = parent_folder + os.sep + renamed_folder_name
            os.rename(new_folder_path, full_new_folder_path)

        else:
            print("New file is not created!")

        # try to remove all files in test directory
        if (remove_file(full_new_folder_path + os.sep + renamed_file_name) and
                remove_file(full_new_folder_path + os.sep + copy_file_name)) is True:
            print("Files are successfully removed!")
        else:
            print("Files are not removed!")

        if remove_folder(renamed_folder_name) is True:
            print("Folder is successfully removed!")
        else:
            print("Folder is not removed!")
    else:
        print("A new directory was not created.")


if __name__ == "__main__":
    main()
