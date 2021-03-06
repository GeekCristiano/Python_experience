# Lets' learn how copying file in python

import shutil
import time
from os import path
from os import rename
from os import sep


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


def get_info(file_name):
    if path.exists(file_name):
        creation_date = time.ctime(path.getctime(file_name))
        last_change_time = time.ctime(path.getmtime(file_name))
    else:
        return
    return (creation_date, last_change_time)


# code for rename source file
def rename_file(src, new_name):
    if path.exists(src) and path.isfile(src):
        file_path = path.realpath(src)
        src_path, old_file_name = path.split(file_path)
        rename(file_path, src_path + sep + new_name)

        return True if path.exists(src_path + sep + new_name) else False
    else:
        print("Incorrect input!")
        return False


def main():
    if copy_file("file.txt") is True:
        print("File successfully copied.")
    else:
        print("An error occurred while copying.")

        # unpacking tuple
    (creation_date, last_change_time) = get_info("file.txt")
    print("Creation time:", creation_date)
    print("Last modified time:", last_change_time)

    if rename_file("file.txt", "new_file.txt") is True:
        print("Source file renamed successfully.")
    else:
        print("An error occurred while renaming.")

if __name__ == "__main__":
    main()
