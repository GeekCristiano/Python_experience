# Lets' learn how copying file in python

import shutil
from os import path


def copy_file(file_name):
    if path.exists(file_name) and path.isfile(file_name):
        file_path = path.realpath(file_name)

        head, tail = path.split(file_path)
        print("Path to file:", head)
        print("File name:", tail)

        # full path to our backup of source file
        dst = file_path + ".bak"
        # get copy only with content of original file
        # shutil.copy(src=file_path, dst=dst)
        # get copy with metada of original file
        shutil.copystat(src=file_path, dst=dst)

        return True if path.exists(dst) else False
    else:
        print("Incorrect input!")
        return False


def main():
    if copy_file("file.txt") == True:
        print("File successfully copied.")
    else:
        print("An error occurred while copying.")


if __name__ == "__main__":
    main()
