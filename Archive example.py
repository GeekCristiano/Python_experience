# Python ZIP file

import os
import shutil


def main():
    full_current_path = os.path.realpath(os.path.curdir)
    shutil.make_archive("test_archive", "zip", full_current_path)

    if (os.path.exists(os.path.realpath("test_archive.zip")) is True):
        print("The archive was successfully created.")
    else:
        print("An error occurred while creating the archive.")


if __name__ == "__main__":
    main()
